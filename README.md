# TOTK-Mods-collection
</br>Mod repo for TOTK on Yuzu emulator.
</br><h2><b>WARNING : Theses mods only work with version `1.1.0` of the game !</b></h2>
</br>
</br>Download link : https://github.com/HolographicWings/TOTK-Mods-collection/releases
</br>
</br>Mod description & usage :
- FPS : Changes the game framerate lock
	</br>If you get under the framerate lock defined by the mod, the game will be in slow motion.
	</br>Reverse if you get over the defined framerate lock.
	</br>Cinematics will be sped up when you go over 30FPS
	</br>We recommend the 30fps version as the 60fps version is buggy, 15 and 20 FPS being experimental and potentially useless.
- Dynamic FPS : Sets the game clock to your framerate and fix slow motion when under the framerate lock, works well when coupled with any of the FPS mods above.
	</br>We recommend using it alongside the 30FPS mod and to uncheck the "Limit Speed Percent" in General settings and set "VSync Mode" to OFF in Graphics settings (yuzu).
	</br>This way, going over the framerate lock defined by the FPS mod will not 'speed up' your game.
	</br>You can toggle the "Limit Speed Percent" with the "Ctrl + U" shortkey on yuzu.
	</br>When you get a cinematic, enable back the "Limit Speed Percent" to avoid faster cutscenes.
	</br>Beware ! When you use Dynamic FPS mod under 15 FPS, the physics will break.
- Graphics - Disable Internal FSR : This mod disable the game's FSR, Yuzu have it's own FSR in the "Window Adapting Filter" in Graphics settings.
	</br>FSR is an optimisation method that reduce the game resolution then upscale it using an algorithm (similar to DLSS but without advanced AI).
	</br>FSR increase GPU performances, at the cost of some details and potential graphical artefacts on small details like leaves or grass.
- Graphics - Disable Internal FXAA - May not do anything : Yuzu have it's own FXAA in the "Anti-Aliasing Method" in Graphics settings.
	</br>FXAA smoothes certain edges to avoid aliasing (pixelated render) and costs very few GPU performances.
	</br>Yuzu has SMAA too, which is a better implementation but uses a bit more GPU performances.
	</br>Disable internal FXAA and change "Anti-Aliasing Method" to "None" in order to increase GPU performances
- Graphics - Disable Dynamic resolution when low FPS : Disables the resolution downscale when your framerate is low.
- Graphics - Disable LODs decrease when low FPS : Disables the LOD decrease when your framerate is low.
	</br>LOD (Level Of Detail) displays higher quality models when you are close to them, and lower quality models when they are futher.
	</br>By default, when your framerate is low, the game lowers the LOD to increase GPU performances.
- Graphics - LOD Patch - We are unsure about it's effect : sounds like it increase the LOD.
- Graphics - Shadows : Changes the shadows resolution.
	</br>1024 is recommended but has a cost on the GPU.
- Resolution : Changes internal render resolution, Vanilla is 1600x900 when the switch is docked.
	</br>1080p (1920x1080) breaks Ambiant Occlusion (AO) so increase GPU performances.
	</br>Ambiant occlusion is a way to increase lightning quality by simulating light exposure in objects hollows. It has a GPU performances cost.
	</br>1008p is the highest resolution found to work without breaking the game's AO.
	</br>540p and 720p require to change the "Resolution" Scaling in Graphics yuzu settings (This setting is just called Resolution), but they look a bit blurry.
	- 540p and x2 = 1080p
	- 540p and x4 = 4K
	- 540p and x8 = 8K
	- 720p and x2 = 1440p
	- 720p and x3 = 4K
	- 720p and x6 = 8K
	</br>For best quality we advise to use the double of your monitor's resolution.
	</br>You can use them with x1 Resolution scale to increase GPU performances.
- Ratio : Experimentally change the game ratio from 16:9.
	- You have to change "Aspect Ratio" in Graphics Yuzu settings to 21:9, 16:10 or "Stretch to Window" if the desired ratio doesn't exist.
	- Will work for scene render but will stretch the HUD.
- Combos : They are all in one mods, don't combine then with unspecified mods if you don't know what you are doing.
	- VisualFixes apply all graphics patches and 1024x shadows in one. You can enable FPS, Resolution, Dynamic FPS and Cheats with it.
	- Potato Patch is made by Hoverbike, it combines every graphics patches (1024x shadows, 1008p resolution and 30fps). You can enable Dynamic FPS and Cheats with it.
- Cheats :
	- The Movement Speed cheats break the game time (time will be wrong when saving)
</br>
</br>The main TOTK performances issue from now comes from the CPU and not the GPU, but unfortunately we don't have any way of increasing CPU performance.
</br>
</br>
</br>
</br>Other good mods :
</br>- https://gamebanana.com/mods/443354 (Xbox UI)
</br>
</br>Useful links :
</br>- https://www.marcrobledo.com/savegame-editors/zelda-totk/ (Save Editor)
</br>Thanks to ChucksFeedAndSeed for the majority of the mods in this collection.
</br>
</br>Copyright and source of mods :
</br>- 20/30 and 60 fps v3 : Authors are "ChuckFeedAndSeed, patchanon and somerandompeople" https://gbatemp.net/download/loz-tears-of-the-kingdom-20fps-30fps-60fps-patch.37996/
</br>- 15fps v3 : From HolographicWings, based on the 20/30 and 60 ones.
</br>- DynamicFPS v1.31 : ChucksFeedAndSeed https://www.reddit.com/r/NewYuzuPiracy/comments/13fjv8r/totk_dynamic_fps_mod_beta_has_some_issues/
</br>- 1008p resolution : ChucksFeedAndSeed https://www.reddit.com/r/NewYuzuPiracy/comments/13deav1/comment/jjk9m60/
</br>- Combo - VisualFixes : Authors are "ChuckFeedAndSeed, patchanon and somerandompeople" https://gbatemp.net/download/loz-tears-of-the-kingdom-20fps-30fps-60fps-patch.37996/
</br>- All Graphic pactchs : Authors are "ChuckFeedAndSeed, patchanon and somerandompeople", theses patches are split from the VisualFixes
</br>- Ratio : From Fayaz https://gamebanana.com/mods/443462
</br>- Others : a real mistery, we gather mods found on the yuzu reddit and discord, if you are the owner of one of them, tell us.
