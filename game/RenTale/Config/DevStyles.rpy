# ========================= COLORS ========================= #
define rentale.style.color_bg_primary = "#13131B"
define rentale.style.color_bg_secondary = "#1C1C24"
define rentale.style.color_bg_tertiary = "#26262E"
define rentale.style.color_bg_dim = "#00000099"

define rentale.style.color_text_primary = "#F0F0F5"
define rentale.style.color_text_secondary = "#A0A0AA"
define rentale.style.color_text_muted = "#64646E"

define rentale.style.color_accent_primary = "#E4348D"
define rentale.style.color_accent_hover = "#FF50A0"
define rentale.style.color_accent_pressed = "#A6296D"

define rentale.style.color_separator = "#2D2D37"


# ========================= TYPOGRAPHY ========================= #
define rentale.style.align_left = 0.0
define rentale.style.align_right = 1.0
define rentale.style.font_size_h = 16
define rentale.style.font_size_p = 13

# ========================= PANEL ========================= #
style RenTale_dev_panel_frame:
    background rentale.style.color_bg_primary
    xysize (0.5, 0.5)
    align (0.5, 0.5)
    padding (0, 0)


# ========================= NAVBAR ========================= #
style RenTale_dev_topbar_frame:
    background rentale.style.color_bg_secondary
    xfill True
    yminimum 44
    padding (0, 0)


# ========================= NAV BUTTON ========================= #
style RenTale_dev_tab_button:
    background rentale.style.color_bg_secondary
    hover_background rentale.style.color_bg_tertiary
    selected_background rentale.style.color_bg_primary
    padding(14, 10)

style RenTale_dev_tab_button_text:
    color rentale.style.color_text_primary
    hover_color rentale.style.color_accent_hover
    selected_color rentale.style.color_accent_pressed
    size rentale.style.font_size_h


# ========================= NAV CLOSE BUTTON ========================= #
style RenTale_dev_close_button:
    background None
    hover_background None
    padding (14, 10)
    xalign rentale.style.align_right

style RenTale_dev_close_button_text:
    color rentale.style.color_text_primary
    hover_color rentale.style.color_accent_hover
    size rentale.style.font_size_h


# ========================= SIMPLE ROW (Time, Flags) ========================= #
style RenTale_dev_row_frame:
    background rentale.style.color_bg_secondary
    xfill True
    padding (0, 0)

style RenTale_dev_row_label_text:
    color rentale.style.color_text_secondary
    text_align rentale.style.align_left
    size rentale.style.font_size_p

style RenTale_dev_row_value_text:
    color rentale.style.color_text_primary
    text_align rentale.style.align_left
    size rentale.style.font_size_p


# ========================= CARD (complex tabs) ========================= #
style RenTale_dev_card_frame:
    background rentale.style.color_bg_secondary
    xfill True
    padding (0, 0)

style RenTale_dev_card_header_text:
    color rentale.style.color_text_primary
    size rentale.style.font_size_p
    bold True

style RenTale_dev_card_kvp_label_text:
    color rentale.style.color_text_secondary
    text_align rentale.style.align_left
    xalign rentale.style.align_left
    size rentale.style.font_size_p

style RenTale_dev_card_kvp_value_text:
    color rentale.style.color_text_primary
    text_align rentale.style.align_left
    xalign rentale.style.align_left
    size rentale.style.font_size_p


# ========================= HUD BUTTON ========================= #
style RenTale_dev_hud_button:
    background None
    hover_background None

style RenTale_dev_hud_button_text:
    color rentale.style.color_text_muted
    hover_color rentale.style.color_accent_hover
    size 32
