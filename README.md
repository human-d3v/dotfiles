# Dotfiles for Fedora Linux Hyprland Config
### Dependencies
* [rofi](https://github.com/davatorium/rofi)
* [waybar](https://github.com/Alexays/Waybar)
* [nautilus](https://apps.gnome.org/Nautilus/)
* [hyprlock](https://github.com/hyprwm/hyprlock)
* [hypridle](https://github.com/hyprwm/hypridle)
* [hyprpaper](https://github.com/hyprwm/hyprpaper)

##### Install Required dependencies
```bash
sudo dnf install rofi waybar kitty nautilus hyprlang-devel pam-devel sdbus-cpp-devel cairo-devel libdrm-devel mesa-libgbm-devel
```
_____
##### Build hyprlock & hypridle from source

```bash
# hyprlock
cd ~/Downloads && 
git clone https://github.com/hyprwm/hyprlock &&
cd hyprlock &&
cmake --no-warn-unused-cli -DCMAKE_BUILD_TYPE:STRING=Release -S . -B ./build
cmake --build ./build --config Release --target hyprlock -j`nproc 2>/dev/null || getconf NPROCESSORS_CONF` &&
sudo cmake --install ./build
``` 
_____
```bash
# hypridle
cd ~/Downloads &&
git clone https://github.com/hyprwm/hypridle &&
cd hypidle &&
cmake --no-warn-unused-cli -DCMAKE_BUILD_TYPE:STRING=Release -S . -B ./build
cmake --build ./build --config Release --target hypridle -j`nproc 2>/dev/null || getconf NPROCESSORS_CONF` &&
sudo cmake --install ./build
```
_____

##### Clone this repository and create symlinks
```bash
#clone repo
cd ~/Downloads && 
git clone https://github.com/human-d3v/dotfiles &&
ln -s ./dotfiles/hypr ~/.config/hypr &&
ln -s ./dotfiles/kitty ~/.config/kitty &&
ln -s ./dotfiles/waybar ~/.config/waybar &&
ln -s ./dotfiles/wezterm ~/.config/wezterm &&
```
