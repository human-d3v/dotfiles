## Import Modules
from __future__ import annotations
from typing import Callable, Any

import os
import pwd
import time
import logging
import random

from newm.layout import Layout

from pywm import (
    PYWM_MOD_LOGO,
    PYWM_MOD_ALT,
    PYWM_TRANSFORM_90,
    PYWM_TRANSFORM_180,
    PYWM_TRANSFORM_270,
    PYWM_TRANSFORM_FLIPPED,
    PYWM_TRANSFORM_FLIPPED_90,
    PYWM_TRANSFORM_FLIPPED_180,
    PYWM_TRANSFORM_FLIPPED_270,
)

logger = logging.getLogger(__name__)

##Startup services
def on_startup():
    init_service = (
        "systemctl --user import-environment \
        DISPLAY WAYLAND_DISPLAY XDG_CURRENT_DESKTOP",
        "hash dbus-update-activation-environment 2>/dev/null && \
        dbus-update-activation-environment --systemd \
        DISPLAY WAYLAND_DISPLAY XDG_CURRENT_DESKTOP",
        "thunar --daemon",
        "nm-applet --indicator",
        "/usr/lib/xfce-polkit/xfce-polkit",
        "~/.config/newm/scripts/notifications",
        "~/.config/newm/scripts/gtkthemes",
        "mpd",
    )

    for service in init_service:
        service = f"{service} &"
        os.system(service)

##reconfiguration
def on_reconfigure():
    os.system("notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i ~/.config/newm/mako/icons/desktop.png NEWM \"Configuration Reloaded\" & ")
    gnome_schema = 'org.gnome.desktop.interface'
    gnome_peripheral = 'org.gnome.desktop.peripherals'
    wm_service_extra_config = (
        f"gsettings set {gnome_schema} gtk-theme 'Nordic'",
        f"gsettings set {gnome_schema} icon-theme 'Qogir-Dark'",
        f"gsettings set {gnome_schema} cursor-theme 'Qogirr-Dark'",
        f"gsettings set {gnome_schema} font-name 'Noto Sans 9'",
        f"gsettings set {gnome_peripheral}.keyboard repeat-interval 30",
        f"gsettings set {gnome_peripheral}.keyboard delay 500",
        f"gsettings set {gnome_peripheral}.mouse natural-scroll false"
        f"gsettings set {gnome_peripheral}.mouse speed 0.0",
        f"gsettings set {gnome_peripheral}.mouse accel-profile 'default'",
        f"gsettings set {gnome_peripheral}.touchpad natural-scroll true",
        f"gsettings set {gnome_peripheral}.touchpad speed 0.0",
        "gsettings set org.gnome.desktop.wm.preferences buttonlayout :",
    )

    for config in wm_service_extra_config:
        config = f"{config} &"
        os.system(config)

## wallpapers
background = {
    'path': os.environ["HOME"] + f"/.config/newm/wallpapers/wallpaper-{random.randrange(6,13)}.jpg",
    'time_scale': 0.125,
    'anim': True,
}

## Outputs
outputs = [
        {
         'name':    'eDP-1', 
         'scale':   1.0,
         'width':   1920,
         'height':  1080,
         'mHz':     60,
         'pos_x':   0,
         'pos_y':   0,
         'anim':    True,
        },
]

##settings
corner_radius = 0
anim_time = 0.30
blend_time = 1.0
pywm = {
    'xkb_model':        "",
    'xkb_layout':       "",
    'xkb_variant':      "",
    'xkb_options':      "caps:super",
    'enable_xwayland':  True,
    'xcursor_theme':    'Qogirr-Dark',
    'xcursor_size':     16,
    'tap_to_click':     True,
    'natural_scroll':   True,
    'focus_follows_mouse': True,
    'constrain_popups_to_toplevel': True,
    'encourage_csd':    False,
    'renderer_mode':    'pywm',
}


#rules for applications
def app_rules(view):
    common_float = {"float":True}
    common_blur = {"blur": {"radius": 6, "passes": 4}}
    float_apps = ("yad", "nm-connection-editor", "pavucontrol",
        "xfce_polkit","kvatummanager", "qt5ct", "feh", "Viewnior",
        "Gpicview","Gimp","MPlayer","VirtualBox Manager", "gemu",
        "Qemu-system-x86_64")
    blur_apps = ("kitty", "foot", "rofi", "waybar", "mako")

    if view.app_id in float_apps:
        return common_float
    if view.app_id in blur_apps:
        return common_blur
    #logout screen
    if view.app_id == "wlogout":
        return {"float": True, "float_size": (1920, 1080), "blur": {'radius': 6, 'passes': 4}}
    #wofi
    if view.app_id == "wofi":
        return {"float": True, "blur": {"radius":6, "passes": 4}}
    #foot
    if view.app_id == "foot-float":
        return {"float": True, "blur": {"radius":6, "passes": 4}}
    return None

#view
view = {
    'corner_radius':        -5,
    'padding':              8,
    'fullscreen_padding':   0,
    'send_fullscreen':      True,
    'accept_fullscreen':    True,
    'floating_min_size':    False,
    'debug_scaling':        True,
    'border_ws_switch':     100,
    'rules':                app_rules,
    'ssd':  {
        'enabled': False,
        'color': '#FAE3B0FF',
        'width': 2,
    },
}

interpolation = {
        'size_adjustment': 0.5
}

#focus
focus = {
    'enabled':      True,
    'color':        '#96CDFBFF',
    'distance':     4,
    'width':        2,
    'animate_on_change': False,
    'anim_time':    0.25,
}

#panels
panels = {
    'bar': {
        'cmd': os.environ["HOME"] + "/.config/newm/scripts/statusbar",
        'visible_fullscreen': False,
        'visible_normal': True
    },
    'lock': {
        'cmd': 'alacritty -e newm-panel-basic lock',
        'w': 0.5,
        'h': 0.5,
        'corner_radius': 20,
    },
}

#keybindings
terminal = '~/.config/newm/scripts/terminal'
colorpicker = '~/.config/newm/scripts/colorpicker'
wlogout = '~/.config/newm/scripts/wlogout'
screenshot = '~/.config/newm/scripts/screenshot'
brightness = '~/.config/newm/scripts/brightness'
volume = '~/.config/newm/scripts/volume'
rofi_launcher = '~/.config/newm/scripts/rofi_launcher'
rofi_music = '~/.config/newm/scripts/rofi_music'
rofi_network = '~/.config/newm/scripts/rofi_network'
rofi_powermenu = '~/.config/newm/scripts/rofi_powermenu'
rofi_runner = '~/.config/newm/scripts/rofi_runner'
rofi_screenshot = '~/.config/newm/scripts/rofi_screenshot'
wofi_menu = '~/.config/newm/scripts/wofi_menu'
wofi_powermenu = '~/.config/newm/scripts/wofi_powermenu'

def key_bindings(layout: Layout) -> list[tuple[str, Callable[[], Any]]]:
    return [
        #terminals
        ("L-Return", lambda: os.system(f"{terminal} &")),
        ("L-S-Return", lambda: os.system(f"{terminal} -f &")),
        ("L-A-Return", lambda: os.system(f"{terminal} -s &")),
        ("C-A-t", lambda: os.system("alacritty &")),

        #apps
        ("L-f", lambda: os.system("thunar &")),
        ("L-e", lambda: os.system("geany &")),
        ("L-w", lambda: os.system("firefox &")),

        #rofi
        ("A-F1", lambda: os.system(f"{rofi_launcher} &")),
        ("L-d", lambda: os.system(f"{rofi_launcher} &")),
        ("L-m", lambda: os.system(f"{rofi_music} &")),
        ("L-n", lambda: os.system(f"{rofi_network} &")),
        ("L-x", lambda: os.system(f"{rofi_powermenu} &")),
        ("L-r", lambda: os.system(f"{rofi_runner} &")),
        ("L-s", lambda: os.system(f"{rofi_screenshot} &")),

        ("L-p", lambda: os.system(f"{colorpicker} &")),

        #focus
        ("L-h", lambda: layout.move(-1,0)),
        ("L-j", lambda: layout.move(0,1)),
        ("L-k", lambda: layout.move(0,-1)),
        ("L-k", lambda: layout.move(1,0)),

        ("L-a", lambda: layout.move_in_stack(1)),
        ("L-space", lambda: layout.toggle_fullscreen()),
        ("L-S-space", lambda: layout.toggle_focused_view_floating()),

        #scale
        ("L-equal", lambda: layout.basic_scale(1)),
        ("L-minus", lambda: layout.basic_scale(-1)),

        #move
        ("L-S-h", lambda: layout.move_focused_view(-1, 0)),
        ("L-S-j", lambda: layout.move_focused_view(0, 1)),
        ("L-S-k", lambda: layout.move_focused_view(0, -1)),
        ("L-S-l", lambda: layout.move_focused_view(1,0)),

        #resize
        ("L-C-l", lambda: layout.resize_focused_view(-1,0)),
        ("L-C-k", lambda: layout.resize_focused_view(0,1)),
        ("L-C-j", lambda: layout.resize_focused_view(0,-1)),
        ("L-C-h", lambda: layout.resize_focused_view(1,0)),

        #other
        ("L-", lambda: layout.toggle_overview(only_active_workspace=True))
        ("L-q", lambda: layout.close_focused_view()),
        ("L-c", lambda: layout.close_focused_view()),
        ("L-C", lambda: layout.update_config()),
        ("L-Q", lambda: layout.terminate()), #important
        ("C-A-Delete", lambda: layout.terminate()),
        ("C-A-l", lambda: layout.ensure_locked(dim=True)),
        
        #function ksys
        ("XF86MonBrightnessUp", lambda: os.system(f"{brightness} --inc &")),
        ("XF86MonBrightnessDown", lambda: os.system(f"{brightness} --dec &")),
        ("XF86AudioRaiseVolume", lambda: os.system(f"{volume} --inc &")),
        ("XF86AudioLowerVolume", lambda: os.system(f"{volume} --dec &")),
        ("XF86AudioMute", lambda: os.system(f"{volume} --toggle &")),
        ("XF86AudioMicMute", lambda: os.system(f"{volume} --toggle-mic &")),

        ("Print", lambda: os.system(f"{screenshot} --now &")),
        ("A-Print", lambda: os.system(f"{screenshot} --in5 &")),
        ("S-Print", lambda: os.system(f"{screenshot} --in10 &")),
        ("L-Print", lambda: os.system(f"{screenshot} --area &")),
    ]

##gestures
gesture_bindings =  {
        'launcher': (None, "swipe-5"),
        'move_resize': ("L", "move-1", "swipe-2"),
        'swipe': (None, "swipe-3"),
        'swipe_to_zoom': (None, "swipe-4"),   
}

gestures = {
    'lp_freq': 60,
    'lp_inertia': 0.8,
    'two_finger_min_dist': 0.1,
    'validate_threshold': 0.02,

    'c': {
        'enabled': True,
        'scale_px': 800,
    },

    'dbus': {
        'enabled': True,
    },

    'pyevdev': {
        'enabled': False,
        'two_finger_min_dist': 0.1,
        'validate_threshold': 0.02,
    },
}

swipe = {
    'gesture_factor': 3,
    'grid_m': 1,
    'grid_ovr': 0.2,
    'lock_dist': 0.01,
}

swipe_zoom = {
    'gesture_factor': 3,
    'grid_m': 1,
    'grid_ovr': 0.2,
    'hyst': 0.2,
},

grid = {
    'min_dist': .05,
    'throw_ps': [2,10],
    'time_scale': 0.3,
}

resize = {
    'grid_m': 3,
    'grid_ovr': 0.1,
    'hyst': 0.2,
}

move = {
    'grid_m': 3,
    'grid_ovr': 0.1,
}

move_resize = {
    'gesture_factor':2   
}
