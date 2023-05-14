# TOTK-Mods-collection
</br>Mod repo for TOTK on Yuzu emulator.
</br>
</br>Download link : https://github.com/HolographicWings/TOTK-Mods-collection/releases
</br>
</br>Mods usage :
- FPS : Change the game framerate lock
	</br>If you get under the framerate lock defined by the mod, game will slow motion.
	</br>Reverse if you get over the defined framerate lock.
	</br>Cinematics are fast motion when you get over 30FPS anyway
	</br>We recommend the 30fps version, the 60fps version being buggy, 15 and 20 being experimental and useless.
- Dynamic FPS : Set the game clock to your framerate and fix slow motion when you are under the framerate lock, work well in couple with any FPS mods above.
	</br>We recommend to use it in couple with the 30FPS mod and uncheck the "Limit Speed Percent" in General yuzu settings and change "VSync Mode" to OFF in Graphics yuzu settings.
	</br>Like that, if you get over the framerate lock defined by the FPS mod, your game will not fast motion.
	</br>You can toggle the "Limit Speed Percent" with the "Ctrl + U" shortkey.
	</br>When you get a cinematic, enable back the "Limit Speed Percent" to avoid fast motion.
	</br>Beware ! When you use Dynamic FPS mod under 15 FPS, the physics will brake.
- Graphics - Disable Internal FSR : Yuzu have it's own FSR in the "Window Adapting Filter" in Graphics settings.
	</br>FSR is an optimisation method that reduce the game resolution then upscale it with an algorythm (like DLSS but without advanced AI).
	</br>FSR increase GPU performances, but you lose some details and can get graphical artefacts on small details like leaves or grass.
- Graphics - Disable Internal FXAA - Maybe does nothing : Yuzu have it's own FXAA in the "Anti-Aliasing Method" in Graphics settings.
	</br>FXAA smooth the edges to avoid pixelated render and cost a very few GPU performances.
	</br>Yuzu have SMAA too, which is better but use a bit more GPU performances.
	</br>Disable internal FXAA and change "Anti-Aliasing Method" to "None" increase GPU performances
- Graphics - Disable Dynamic resolution when low FPS : Disable the resolution downscale when you are low FPS.
- Graphics - Disable LODs decrease when low FPS : Disable the LOD decrease when you are low FPS.
	</br>LOD level choices to display better models when you are close to them, and lower quality models when they are futher.
	</br>By default, when you are low FPS, the game lower the LOD level to increase GPU performances.
- Graphics - LOD Patch - We are unsure about it's effect : sound like it increase the LOD level.
- Graphics - Shadows : Change the shadows resolution.
	</br>1024 is recommended but have a GPU performances cost.
- Resolution : Change render resolution. Vanilla is 1600x900.
	</br>The 1080p break Ambiant Occlusion so increase GPU performances.
	</br>Ambiant occlusion is a way to increase graphics by simulating the light exposure in objects hollows. It have a GPU performances cost.
	</br>The 1008p is the highter resolution found to work without breaking Ambiant Occlusion.
	</br>540p and 720p require to change the "Resolution" Scaling in Graphics yuzu settings (This setting is just called Resolution), but they look a bit blurry.
	- 540p and x2 = 1080p
	- 540p and x4 = 4K
	- 540p and x8 = 8K
	- 720p and x2 = 1440p
	- 720p and x3 = 4K
	- 720p and x6 = 8K
	</br>For best quality we advice to use the double of your monitor resolution.
	</br>You can use them with x1 Resolution scale to increase GPU performances.
- Combos : They are all in one mods, don't combine then with unspecified mods if you don't know what you are doing.
	- VisualFixes apply all graphics patchs and 1024x shadows in once. You can enable FPS, Resolution, Dynamic FPS and Cheats with it.
	- Potato Patch is made by Hoverbike, it combine every graphics patchs, 1024x shadows, 1008p resolution and 30fps. You can enable Dynamic FPS and Cheats with it.
- Cheats :
	- The Movement Speed cheats break the game time (time will be wrong when saving)
</br>
</br>The main TOTK performances issue from now is from CPU and not GPU, but unfortunately we don't have any way to increase CPU performances.
</br>
</br>
</br>
</br>Other good mods :
</br>- https://gamebanana.com/mods/443354 (Xbox UI)
</br>- https://gamebanana.com/mods/443462 (Ultrawide and Steam Deck 21:9 and 32:9 and 16:10)
</br>You have to change "Aspect Ratio" in Graphics Yuzu settings to 21:9 or 16:10 or "Stretch to Window" if the desired ratio doesn't exist.
</br>Will work for scene render but will stretch the HUD.
</br>
</br>Usefull links :
</br>- https://github.com/lchmagKekse/TOTK-SaveGame-Editor (Save Editor)
</br>Thanks to ChucksFeedAndSeed for the majority of mods of this collection.
</br>
</br>Copyright and source of mods :
</br>- 20/30 and 60 fps v3 : Authors are "ChuckFeedAndSeed, patchanon and somerandompeople" https://gbatemp.net/download/loz-tears-of-the-kingdom-20fps-30fps-60fps-patch.37996/
</br>- 15fps v3 : From HolographicWings, based on the 20/30 and 60 ones.
</br>- DynamicFPS v1.31 : ChucksFeedAndSeed https://www.reddit.com/r/NewYuzuPiracy/comments/13fjv8r/totk_dynamic_fps_mod_beta_has_some_issues/
</br>- 1008p resolution : ChucksFeedAndSeed https://www.reddit.com/r/NewYuzuPiracy/comments/13deav1/comment/jjk9m60/
</br>- Combo - VisualFixes : Authors are "ChuckFeedAndSeed, patchanon and somerandompeople" https://gbatemp.net/download/loz-tears-of-the-kingdom-20fps-30fps-60fps-patch.37996/
</br>- All Graphic pactchs : Authors are "ChuckFeedAndSeed, patchanon and somerandompeople", theses patchs are splited from the VisualFixes
</br>- Others : a real mistery, we gather mods found on the yuzu reddit and discord, if you are owner of one of them, tell us.
