#!/usr/bin/env python3
"""
Publishes a new blog post to the Hart Beat Energy website and triggers
a GitHub Pages deploy.

Called by the hbs-blog-writer scheduled task (or manually).

Usage:
  python3 publish_blog_post.py --slug "my-post-slug" \\
      --title "My Post Title" \\
      --category "News" \\
      --excerpt "Short excerpt for the blog index." \\
      --body-file path/to/post-body.html \\
      [--author "Hart Beat Energy Team"] \\
      [--read-min 6] \\
      [--date YYYY-MM-DD] \\
      [--push]          # commit + git push to origin/main to trigger Pages deploy

Required env:
  HBS_WEBSITE_DIR  — absolute path to the website/ directory (defaults to repo layout)
"""
from __future__ import annotations
import argparse, datetime, os, re, subprocess, sys, pathlib

THIS = pathlib.Path(__file__).resolve()
WEBSITE_DIR = pathlib.Path(os.environ.get("HBS_WEBSITE_DIR", THIS.parents[1]))
CONTENT_BLOG = WEBSITE_DIR / "content_blog.py"


def slugify(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9\s-]", "", text).strip().lower()
    return re.sub(r"[\s_-]+", "-", s)


def append_post(args):
    assert CONTENT_BLOG.exists(), f"content_blog.py not found at {CONTENT_BLOG}"
    src = CONTENT_BLOG.read_text(encoding="utf-8")

    # Guard against duplicate slug (check both POSTS entries and POST_BODIES keys)
    if f'"slug": "{args.slug}"' in src or f'"{args.slug}":' in src:
        print(f"[publish_blog_post] Slug '{args.slug}' already exists — skipping.")
        return False

    body_html = pathlib.Path(args.body_file).read_text(encoding="utf-8")

    date = args.date or datetime.date.today().isoformat()

    # --- 1) Prepend entry to POSTS list (metadata used by the blog index card) ---
    post_dict = f'''    {{
        "slug": "{args.slug}",
        "title": {args.title!r},
        "category": {args.category!r},
        "excerpt": {args.excerpt!r},
        "author": {args.author!r},
        "date": "{date}",
        "read_min": {args.read_min},
    }},
'''
    m = re.search(r"POSTS\s*=\s*\[", src)
    if not m:
        raise SystemExit("Could not find POSTS = [ in content_blog.py")
    insert_at = m.end()
    src = src[:insert_at] + "\n" + post_dict + src[insert_at:]

    # --- 2) Prepend entry to POST_BODIES dict (HTML rendered on the post detail page) ---
    # The site template wraps bodies in <section class="section"><div class="container prose">...</div></section>
    # Escape triple single-quotes so the body can live inside a ''' literal
    wrapped_body = (
        '\n<section class="section"><div class="container prose">\n'
        + body_html.strip()
        + '\n</div></section>\n'
    )
    body_safe = wrapped_body.replace("'''", "\\'\\'\\'")
    body_entry = f'    "{args.slug}": \'\'\'{body_safe}\'\'\',\n'
    mb = re.search(r"POST_BODIES\s*=\s*\{", src)
    if not mb:
        raise SystemExit("Could not find POST_BODIES = { in content_blog.py")
    insert_at_b = mb.end()
    src = src[:insert_at_b] + "\n" + body_entry + src[insert_at_b:]

    CONTENT_BLOG.write_text(src, encoding="utf-8")
    print(f"[publish_blog_post] Inserted post '{args.slug}' into POSTS and POST_BODIES")
    return True


def git_commit_push(args):
    """Commit + push so GitHub Actions builds and deploys to Pages."""
    repo = WEBSITE_DIR.parent  # assume repo root is parent of website/
    try:
        subprocess.run(["git", "-C", str(repo), "add", "website/content_blog.py"], check=True)
        msg = f"blog: publish {args.slug}"
        subprocess.run(["git", "-C", str(repo), "commit", "-m", msg], check=True)
        subprocess.run(["git", "-C", str(repo), "push", "origin", "main"], check=True)
        print(f"[publish_blog_post] Pushed to origin/main — GitHub Actions will deploy.")
    except subprocess.CalledProcessError as e:
        print(f"[publish_blog_post] git step failed: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--slug", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--category", default="Solar Insights")
    p.add_argument("--excerpt", required=True)
    p.add_argument("--body-file", required=True)
    p.add_argument("--author", default="Hart Beat Energy Team")
    p.add_argument("--read-min", type=int, default=6)
    p.add_argument("--date", default=None)
    p.add_argument("--push", action="store_true", help="git commit + push after inserting")
    args = p.parse_args()

    if append_post(args) and args.push:
        git_commit_push(args)


if __name__ == "__main__":
    main()
