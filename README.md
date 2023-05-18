# TOTK-Mods-collection

Mod repo for TOTK on Yuzu emulator.
</br>

## **WARNING : Theses mods only work with version `1.1.0` of the game !**

</br>

### [Download latest release](https://github.com/HolographicWings/TOTK-Mods-collection/releases)

</br>Mod description & usage :

- **FPS** : Changes the game's framerate lock  
If you get under the framerate lock defined by the mod, the game will be in slow motion.  
Reverse if you get over the defined framerate lock.  
Cinematics will be sped up when you go over 30FPS.  
We recommend the 30fps version as the 60fps version is buggy, 15 and 20 FPS being experimental and potentially useless.  
Why should I use the 30fps mod ? : In vanilla, the game seems to lock to 25 or 20 fps when you hit 29fps (This remains to be proven).  
</br>

- **Dynamic FPS** : Sets the game clock to your framerate and fixes slow motion when under the framerate lock, works well when coupled with any of the FPS mods above.  
We recommend using it alongside the 30FPS mod and to uncheck the "Limit Speed Percent" in General settings as well as setting "VSync Mode" to OFF in Graphics settings (yuzu).  
This way, going over the framerate lock defined by the FPS mod will not 'speed up' your game.  
You can toggle the "Limit Speed Percent" with the "Ctrl + U" shortkey on yuzu.  
When you get a cinematic, enable back the "Limit Speed Percent" to avoid faster cutscenes.  
**BEWARE !** When you use Dynamic FPS mod under 15 FPS, the physics will break ! (Maybe fixed since v1.4, must check)
</br>

- **Cutscene Fix**: Sets the framerate lock to 30 FPS automatically during FMV cutscenes.  
You must have the Yuzu framerate lock enabled for this to work, and it needs to be paired with the FPS "60fps V3 - Cutscene-Fix-required" mod.
</br>

- Graphics - **Disable Internal FSR Downscaling** : This mod disables the game's FSR, Yuzu have it's own FSR in the "Window Adapting Filter" in Graphics settings.  
FSR is an optimisation method that reduces the game's internal resolution then upscales it using an algorithm (similar to DLSS but without advanced AI).  
FSR increases GPU performances, at the cost of some details and potential graphical artefacts on small geometry like leaves or grass.
</br>

- Graphics - **Disable Internal FSR Sharpening Shader** : This mod disables the sharpening effect post processing the FSR Downscaling.  
GPU Performances cost is extremely low so use it will not improve them but could do an ugly render if you use it without the FSR Downscaling.  
**BEWARE !** It seems that this mod could crashes Ryujinx.  
</br>

- Graphics - **Disable Internal FXAA** - Yuzu have it's own FXAA in the "Anti-Aliasing Method" in Graphics settings.  
FXAA smoothes certain edges to avoid aliasing (jagged edges) and costs very few GPU performances.  
Yuzu has SMAA too, which is a better implementation of anti-aliasing but uses a bit more GPU performances.  
Disable internal FXAA and change "Anti-Aliasing Method" to "None" in order to increase GPU performances (?).  

> We're starting to doubt the mod will change anything, if you get any proof of its effect please share a screenshot or video with us.

</br>

- Graphics - **Disable Dynamic resolution** when low FPS : Disables the resolution downscale when your framerate is low.
</br>

- Graphics - **Disable LOD decrease** when low FPS : Disables the LOD decrease when your framerate is low.  
LOD (Level Of Detail) displays higher quality models when you are close to them, and lower quality models when they are futher.  
By default, when your framerate is low, the game lowers the LOD to increase GPU performances.  
</br>

- Graphics - **LOD Patch** - We are unsure about it's effect : it appears to increase the LOD.  
Some people have reported this fixed 3D models popping suddenly into view (remains to be confirmed).
</br>

- Graphics - **Shadows** : changes the resolution of shadows.  
1024 being vanilla resolution, it is useless by default, but it fixes some graphical issues on certain setups.  
[Shadow stuttering issue took by Lux using a Radeon RX 580 8Gb - with & without Shadow x512](https://imgsli.com/MTc5MTM1)  
[Gloom issue took by Red_BY using a RTX 2080 at 3x render scale - with & without Shadow x1024](https://imgsli.com/MTc5MTYx)  
256 and 512 would increase GPU performance a lot.  
</br>

- Graphics - **Anisotropic Filtering fix** : Fixes Anisotropic Filtering issues ( black line artifacts on textures viewed at oblique angles).  
Set Anisotropic Filtering to 16 in Yuzu advanced graphics settings.  
[Difference Off/On](https://imgsli.com/MTc5MzQ0)
</br>

- **Resolution** : Changes internal render resolution, Vanilla is 1600x900 when the switch is docked.  
1080p (1920x1080) breaks Ambiant Occlusion (AO) but increases GPU performance.  
Ambiant occlusion is a way to increase lightning quality by simulating light exposure in objects hollows. It has a GPU performances cost.  
1008p is the highest resolution found to work without breaking the game's AO.  
360p, 540p and 720p require to change the "Resolution" Scaling in Graphics yuzu settings (This setting is just called Resolution), but they look a bit blurry.  
  - 540p and x2 = 1080p
  - 540p and x4 = 4K
  - 540p and x8 = 8K
  - 720p and x2 = 1440p
  - 720p and x3 = 4K
  - 720p and x6 = 8K
For best quality we advise you to use the double of your monitor's resolution.  
You can use them with x1 Resolution scale to increase GPU performance.
</br>

- **Ratio** : Experimentally change the aspect ratio from 16:9.
  - You have to change "Aspect Ratio" in Graphics Yuzu settings to 21:9, 16:10 or "Stretch to Window" if the desired ratio doesn't exist.  
  - Will work for scene render but will stretch the HUD.
</br>

- **Combos** : They are all-in-one mods, don't combine then with unspecified mods if you don't know what you are doing.
  - **30/60fps + Dynamic FPS** are a simple Combo of theses two mods in one.
  - **Light pack and Unlimited FPS** : Pack made by HolographicWings, combine Dynamic FPS, 1008p and FSR Disabler, it's a minimal pack for cleaner experience.  
You can use it with any Graphics other pack, ratio and cheats but it's not recommended.  
It is important to press Ctrl + U in game to unlock your framerate and play over 30fps, like that you can play at 60 or more with normal game speed, don't forget to press Ctrl + U again to lock back your framerate to 30fps when you get a cutscene.
</br>

- Cheats :
  - The Movement Speed cheats breaks the game time (time will be wrong when saving)
  - Stamina cheat doesn't seem to work.
  - Infinite amiibo usage is pointless since yuzu has a similar feature, go in Yuzu settings → Controls → Advanced and check "Use random Amiibo ID".

</br>
</br>The main TOTK performances issue from now comes from the CPU and not the GPU, but unfortunately we don't have any easy way of increasing CPU performance.  
</br>
</br>
</br>Other good mods :

- [Xbox UI](https://gamebanana.com/mods/443354) by Alerion921

</br>Useful links :

- [Save Editor](https://www.marcrobledo.com/savegame-editors/zelda-totk/) by Marc Robledo
</br>

> Thanks to [ChucksFeedAndSeed](https://www.reddit.com/user/ChucksFeedAndSeed/) for the *majority* of the mods in this collection.

</br>Copyright and source of mods :

- [20/30 and 60 fps v3](https://gbatemp.net/download/loz-tears-of-the-kingdom-20fps-30fps-60fps-patch.37996/) : Authors are "ChucksFeedAndSeed, patchanon and somerandompeople"

- [DynamicFPS v1.31 & 1.4](https://www.reddit.com/r/NewYuzuPiracy/comments/13fjv8r/totk_dynamic_fps_mod_beta_has_some_issues/) : ChucksFeedAndSeed

- [1008p resolution](https://www.reddit.com/r/NewYuzuPiracy/comments/13deav1/comment/jjk9m60/) : ChucksFeedAndSeed

- [Combo - VisualFixes](https://gbatemp.net/download/loz-tears-of-the-kingdom-20fps-30fps-60fps-patch.37996/) : Authors are "ChucksFeedAndSeed, patchanon and somerandompeople"

- All Graphic pactches : Authors are "ChucksFeedAndSeed, patchanon and somerandompeople", theses patches are split from the VisualFixes, FSR Disabler is especially from patchanon

- [Aspect Ratio](https://gamebanana.com/mods/443462) : From Fayaz

- [Graphics - Anisotropic filtering fix](https://github.com/Wollnashorn/switch-mods/tree/master/0100F2C0115B6000) : @Wollnashorn

- FPS - Cutscene-fix : theboy181

- Others : A real mystery. We gather mods found on the yuzu reddit and discord, if you are the owner of one of them, contact us so we can credit you.
