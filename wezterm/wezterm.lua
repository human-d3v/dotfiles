local wezterm = require 'wezterm'


local config = wezterm.config_builder()

-- colors
-- config.color_scheme = 'PaperColor Dark (Gogh)'
config.color_scheme = 'fideloper'
config.window_background_opacity = .8
config.colors = {background = "black"}

-- fonts
config.font = wezterm.font 'MonaspaceNeon-Regular'
config.harfbuzz_features = {"calt", "ss01", "ss02", "ss03", "ss04"}

--disable defaults
config.keys = {
	{
		key = "-",
		mods = "CTRL",
		action = wezterm.action.SendKey { key = "-", mods = "CTRL"},
	},
	{
		key = ">",
		mods = "CTRL",
		action = wezterm.action.SendKey { key = ">", mods = "CTRL"},
	}
}


return config
