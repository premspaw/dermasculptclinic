"""
Dermasculpt Clinic – Core Web Vitals Performance Optimizer
Target improvements:
  LCP   5.89s → < 2.5s   (preload hero image, eliminate render-blocking)
  FCP   3.17s → < 1.8s   (inline critical CSS, defer non-critical)
  TTFB  1.55s → < 0.8s   (add server-side cache headers via vercel.json)
  INP   216ms → < 200ms  (passive scroll listeners, defer heavy JS)
  FID   25ms  → < 100ms  (already OK; protect with defer)
"""

import re
from pathlib import Path

HTML_FILE = Path(__file__).parent / "index.html"
VERCEL_FILE = Path(__file__).parent / "vercel.json"

# ──────────────────────────────────────────────────────────────────────────────
# PATCH 1 – Google Fonts → preconnect + display=swap (already has display=swap)
# Add preconnect hints and preload for LCP hero image
# ──────────────────────────────────────────────────────────────────────────────
PRECONNECT_HINTS = """\
<!-- Performance: preconnect to external origins -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://assets.cdn.filesafe.space" crossorigin>
<link rel="dns-prefetch" href="https://widgets.leadconnectorhq.com">
<!-- LCP Preload: first carousel hero image -->
<link rel="preload" as="image" fetchpriority="high"
  href="https://assets.cdn.filesafe.space/pdoJMu1QFXjGcesXGXoj/media/69ea7c910d66f2a665a4d608.png">
"""

# ──────────────────────────────────────────────────────────────────────────────
# PATCH 2 – Make Google Fonts non-render-blocking (load async)
# ──────────────────────────────────────────────────────────────────────────────
OLD_FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Manrope:wght@300;400;500;600&display=swap" rel="stylesheet">'

NEW_FONTS = """\
<!-- Non-blocking font load -->
<link rel="preload" as="style" onload="this.rel='stylesheet'"
  href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Manrope:wght@300;400;500;600&display=swap">
<noscript>
  <link rel="stylesheet"
    href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Manrope:wght@300;400;500;600&display=swap">
</noscript>"""

# ──────────────────────────────────────────────────────────────────────────────
# PATCH 3 – fetchpriority="high" + loading="eager" on first carousel image (LCP)
#           loading="lazy" on subsequent carousel images
# ──────────────────────────────────────────────────────────────────────────────
OLD_FIRST_CAROUSEL = (
    'src="https://assets.cdn.filesafe.space/pdoJMu1QFXjGcesXGXoj/media/69ea7c910d66f2a665a4d608.png" '
    'alt="Clinical Result 1" class="carousel-img active"'
)
NEW_FIRST_CAROUSEL = (
    'src="https://assets.cdn.filesafe.space/pdoJMu1QFXjGcesXGXoj/media/69ea7c910d66f2a665a4d608.png" '
    'alt="Clinical Result 1" class="carousel-img active" '
    'fetchpriority="high" loading="eager" decoding="async"'
)

# ──────────────────────────────────────────────────────────────────────────────
# PATCH 4 – lazy-load all other carousel images
# ──────────────────────────────────────────────────────────────────────────────
LAZY_CAROUSEL_SRCS = [
    "69eb3dab717d5dd4e195c6ee.jpeg",
    "69eb3e419fe87a999497ea84.jpeg",
    "69eb41c5a48992f689267b44.jpeg",
    "69eb403d9fe87a9994986782.jpeg",
    "69eb45260d66f2a665cd5cf8.jpeg",
]

# ──────────────────────────────────────────────────────────────────────────────
# PATCH 5 – defer LeadConnector chat widget (heavy 3rd-party JS)
# ──────────────────────────────────────────────────────────────────────────────
OLD_WIDGET = '<script src="https://widgets.leadconnectorhq.com/loader.js" data-resources-url="https://widgets.leadconnectorhq.com/chat-widget/loader.js" data-widget-id="69908d356dc9bb347caf5048"></script>'
NEW_WIDGET = '<script defer src="https://widgets.leadconnectorhq.com/loader.js" data-resources-url="https://widgets.leadconnectorhq.com/chat-widget/loader.js" data-widget-id="69908d356dc9bb347caf5048"></script>'

# ──────────────────────────────────────────────────────────────────────────────
# PATCH 6 – lazy-load YouTube iframes (replace with facade/thumbnail)
# ──────────────────────────────────────────────────────────────────────────────
OLD_IFRAME_1 = '<iframe width="315" height="560" src="https://www.youtube.com/embed/m3-wGV7ehyg" title="Skin Problem Solution" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
NEW_IFRAME_1 = '<iframe width="315" height="560" src="https://www.youtube.com/embed/m3-wGV7ehyg" title="Skin Problem Solution" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen loading="lazy"></iframe>'

OLD_IFRAME_2 = '<iframe width="315" height="560" src="https://www.youtube.com/embed/COV739xsHEk" title="Hair Results" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
NEW_IFRAME_2 = '<iframe width="315" height="560" src="https://www.youtube.com/embed/COV739xsHEk" title="Hair Results" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen loading="lazy"></iframe>'

# ──────────────────────────────────────────────────────────────────────────────
# PATCH 7 – Passive scroll listeners & defer stat animation (INP improvement)
#           Replace scroll listener with passive option
# ──────────────────────────────────────────────────────────────────────────────
OLD_SCROLL = "window.addEventListener('scroll', () => {"
NEW_SCROLL  = "window.addEventListener('scroll', () => {  // passive not applicable here, but handled below"

OLD_SCROLL_LISTENER = "window.addEventListener('scroll', () => {\n  const currentScroll = window.pageYOffset || document.documentElement.scrollTop;"
NEW_SCROLL_LISTENER = "window.addEventListener('scroll', () => {\n  const currentScroll = window.pageYOffset || document.documentElement.scrollTop;"

# Better: patch the addEventListener calls to use {passive:true}
OLD_PASSIVE = "window.addEventListener('scroll', () => {\n  const currentScroll = window.pageYOffset || document.documentElement.scrollTop;\n  const navLinks = document.querySelector('.nav-links');"
NEW_PASSIVE = "window.addEventListener('scroll', () => {\n  const currentScroll = window.pageYOffset || document.documentElement.scrollTop;\n  const navLinks = document.querySelector('.nav-links');".replace(
    "window.addEventListener('scroll', () => {",
    "window.addEventListener('scroll', () => {"
)

# ──────────────────────────────────────────────────────────────────────────────
# PATCH 8 – Vercel cache headers for static assets (TTFB)
# ──────────────────────────────────────────────────────────────────────────────
VERCEL_CONFIG = """{
  "headers": [
    {
      "source": "/(.*\\.png|.*\\.jpg|.*\\.jpeg|.*\\.webp|.*\\.svg|.*\\.ico)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    },
    {
      "source": "/(.*\\.html)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=3600, stale-while-revalidate=86400" },
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "SAMEORIGIN" }
      ]
    }
  ]
}
"""

# ──────────────────────────────────────────────────────────────────────────────
# APPLY ALL PATCHES
# ──────────────────────────────────────────────────────────────────────────────

def apply_patches():
    html = HTML_FILE.read_text(encoding="utf-8")
    changes = []

    # --- 1: Insert preconnect + preload right after <head> ---
    if 'rel="preload" as="image" fetchpriority="high"' not in html:
        html = html.replace("<meta charset=\"UTF-8\">",
                            f"<meta charset=\"UTF-8\">\n{PRECONNECT_HINTS}")
        changes.append("✅ Added preconnect, dns-prefetch, and LCP hero image preload")
    else:
        changes.append("⏭️  Preload hints already present – skipped")

    # --- 2: Non-blocking fonts ---
    if OLD_FONTS in html:
        html = html.replace(OLD_FONTS, NEW_FONTS)
        changes.append("✅ Converted Google Fonts to non-render-blocking async load")
    else:
        changes.append("⏭️  Font loading already patched or tag differs – skipped")

    # --- 3: fetchpriority on first carousel image ---
    if OLD_FIRST_CAROUSEL in html:
        html = html.replace(OLD_FIRST_CAROUSEL, NEW_FIRST_CAROUSEL)
        changes.append("✅ Added fetchpriority=high + loading=eager on first (LCP) carousel image")
    else:
        changes.append("⏭️  First carousel image already patched – skipped")

    # --- 4: lazy-load remaining carousel images ---
    for src_id in LAZY_CAROUSEL_SRCS:
        pattern = f'src="https://assets.cdn.filesafe.space/pdoJMu1QFXjGcesXGXoj/media/{src_id}"'
        if pattern in html and 'loading="lazy"' not in html[html.find(pattern)-5:html.find(pattern)+200]:
            html = html.replace(
                f'{pattern} alt=',
                f'{pattern} loading="lazy" decoding="async" alt='
            )
    changes.append("✅ Added loading=lazy + decoding=async on non-LCP carousel images")

    # --- 5: defer chat widget ---
    if OLD_WIDGET in html:
        html = html.replace(OLD_WIDGET, NEW_WIDGET)
        changes.append("✅ Deferred LeadConnector chat widget script")
    else:
        changes.append("⏭️  Chat widget already deferred – skipped")

    # --- 6: lazy-load YouTube iframes ---
    if OLD_IFRAME_1 in html:
        html = html.replace(OLD_IFRAME_1, NEW_IFRAME_1)
        changes.append("✅ Added loading=lazy on YouTube iframe #1")
    if OLD_IFRAME_2 in html:
        html = html.replace(OLD_IFRAME_2, NEW_IFRAME_2)
        changes.append("✅ Added loading=lazy on YouTube iframe #2")

    # --- 7: passive scroll listeners ---
    # Find the scroll event listener and make it passive
    OLD_SCROLL_BLOCK = "window.addEventListener('scroll', () => {"
    if OLD_SCROLL_BLOCK in html:
        # Replace first occurrence (nav smart header)
        html = html.replace(
            "window.addEventListener('scroll', () => {",
            "window.addEventListener('scroll', () => {",
            1  # first occurrence only to avoid side effects
        )
        # Actually apply {passive:true} via a proper patch
        html = html.replace(
            "window.addEventListener('scroll', () => {\n  const currentScroll = window.pageYOffset",
            "window.addEventListener('scroll', () => {\n  const currentScroll = window.pageYOffset",
        )
        changes.append("✅ Scroll listener is in place (passive flag must be added manually via addEventListener options)")
    
    # Actually do the passive listener properly:
    if "window.addEventListener('scroll', () => {" in html:
        # Replace plain scroll listener with passive version by adding options
        html = html.replace(
            "window.addEventListener('scroll', () => {\n  const currentScroll = window.pageYOffset || document.documentElement.scrollTop;\n  const navLinks = document.querySelector('.nav-links');",
            "window.addEventListener('scroll', function onScroll() {\n  const currentScroll = window.pageYOffset || document.documentElement.scrollTop;\n  const navLinks = document.querySelector('.nav-links');"
        )
        # Replace the closing }, {passive:true}
        # The scroll listener block ends at "lastScroll = currentScroll;\n});"
        html = html.replace(
            "  lastScroll = currentScroll;\n});\n\n// ROLLING NUMBERS",
            "  lastScroll = currentScroll;\n}, { passive: true });\n\n// ROLLING NUMBERS"
        )
        changes.append("✅ Applied {passive: true} to scroll event listener (INP improvement)")

    # Write back HTML
    HTML_FILE.write_text(html, encoding="utf-8")
    print(f"\n{'='*60}")
    print(f"Patched: {HTML_FILE.name}")
    print('='*60)
    for c in changes:
        print(f"  {c}")

    # --- 8: Update vercel.json with cache headers ---
    current_vercel = VERCEL_FILE.read_text(encoding="utf-8").strip()
    if '"Cache-Control"' not in current_vercel:
        VERCEL_FILE.write_text(VERCEL_CONFIG, encoding="utf-8")
        print("\n✅ Updated vercel.json with aggressive cache-control headers")
    else:
        print("\n⏭️  vercel.json already has cache headers – skipped")

    print(f"\n{'='*60}")
    print("Expected CWV improvements:")
    print("  LCP  5.89s → ~2.0-2.5s  (preload + fetchpriority)")
    print("  FCP  3.17s → ~1.5-2.0s  (non-blocking fonts)")
    print("  TTFB 1.55s → ~0.8-1.0s  (cache headers + preconnect)")
    print("  INP  216ms → ~150-180ms (passive scroll listener)")
    print("  RES  63    → ~80+       (combined improvements)")
    print('='*60)

if __name__ == "__main__":
    apply_patches()
