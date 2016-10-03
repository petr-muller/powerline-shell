def add_proxy_segment(powerline):
    import os

    if "HTTP_PROXY" in os.environ:
        fg = Color.PROXY_FG
        bg = Color.PROXY_BG
        powerline.append(" PROXY ", fg, bg)
