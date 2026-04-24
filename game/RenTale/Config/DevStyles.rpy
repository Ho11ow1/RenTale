# ========================= COLORS ========================= #
define RenTale_color_bg_primary = "#13131B"
define RenTale_color_bg_secondary = "#1C1C24"
define RenTale_color_bg_tertiary = "#26262E"
define RenTale_color_bg_dim = "#00000099"

define RenTale_color_text_primary = "#F0F0F5"
define RenTale_color_text_secondary = "#A0A0AA"
define RenTale_color_text_muted = "#64646E"

define RenTale_color_accent_primary = "#E4348D"
define RenTale_color_accent_hover = "#FF50A0"
define RenTale_color_accent_pressed = "#A6296D"

define RenTale_color_separator = "#2D2D37"


# ========================= TYPOGRAPHY ========================= #
define RenTale_align_left = 0.0
define RenTale_align_right = 1.0
define RenTale_font_size_h = 16
define RenTale_font_size_p = 13


# ========================= PANEL ========================= #
style RenTale_dev_panel_frame:
    background RenTale_color_bg_primary
    xysize (0.5, 0.5)
    align (0.5, 0.5)
    padding (0, 0)


# ========================= NAVBAR ========================= #
style RenTale_dev_topbar_frame:
    background RenTale_color_bg_secondary
    xfill True
    yminimum 44
    padding (0, 0)


# ========================= NAV BUTTON ========================= #
style RenTale_dev_tab_button:
    background RenTale_color_bg_secondary
    hover_background RenTale_color_bg_tertiary
    selected_background RenTale_color_bg_primary
    padding(14, 10)

style RenTale_dev_tab_button_text:
    color RenTale_color_text_primary
    hover_color RenTale_color_accent_hover
    selected_color RenTale_color_accent_pressed
    size RenTale_font_size_h


# ========================= NAV CLOSE BUTTON ========================= #
style RenTale_dev_close_button:
    background None
    hover_background None
    padding (14, 10)
    xalign RenTale_align_right

style RenTale_dev_close_button_text:
    color RenTale_color_text_primary
    hover_color RenTale_color_accent_hover
    size RenTale_font_size_h


# ========================= SIMPLE ROW (Time, Flags) ========================= #
style RenTale_dev_row_frame:
    background RenTale_color_bg_secondary
    xfill True
    padding (0, 0)

style RenTale_dev_row_label_text:
    color RenTale_color_text_secondary
    text_align RenTale_align_left
    size RenTale_font_size_p

style RenTale_dev_row_value_text:
    color RenTale_color_text_primary
    text_align RenTale_align_left
    size RenTale_font_size_p


# ========================= CARD (complex tabs) ========================= #
style RenTale_dev_card_frame:
    background RenTale_color_bg_secondary
    xfill True
    padding (0, 0)

style RenTale_dev_card_header_text:
    color RenTale_color_text_primary
    size RenTale_font_size_p
    bold True

style RenTale_dev_card_kvp_label_text:
    color RenTale_color_text_secondary
    text_align RenTale_align_left
    xalign RenTale_align_left
    size RenTale_font_size_p

style RenTale_dev_card_kvp_value_text:
    color RenTale_color_text_primary
    text_align RenTale_align_left
    xalign RenTale_align_left
    size RenTale_font_size_p


# ========================= HUD BUTTON ========================= #
style RenTale_dev_hud_button:
    background None
    hover_background None

style RenTale_dev_hud_button_text:
    color RenTale_color_text_muted
    hover_color RenTale_color_accent_hover
    size 32
