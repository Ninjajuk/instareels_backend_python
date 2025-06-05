def extract_shortcode(url):
    try:
        if "/reel/" in url:
            return url.split("/reel/")[1].split("/")[0]
        elif "/p/" in url:
            return url.split("/p/")[1].split("/")[0]
    except Exception:
        return None
