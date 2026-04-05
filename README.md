# Hart Beat Energy — hartbeat.solar

Production source for [hartbeat.solar](https://www.hartbeat.solar), Texas solar
installation and concierge maintenance.

## Architecture
- **Source:** `website/` (Python static-site generator)
- **Build command:** `cd website && python3 generate.py` → outputs `website/dist/`
- **Deploy:** GitHub Actions rebuilds and publishes to GitHub Pages on every push to `main`

## Adding a blog post
Use `website/scripts/publish_blog_post.py`:

```bash
python3 website/scripts/publish_blog_post.py \
  --slug "my-post" --title "My Post" \
  --excerpt "Short teaser." \
  --body-file /path/to/body.html \
  --push
```

The `--push` flag commits and pushes, which triggers the Pages deploy automatically.
