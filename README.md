# TOTK-Mods-collection

## :exclamation:**WARNING : These mods only work with version `1.1.0` of the game !**:exclamation:

</br>

<div align="center">
  
### [Download latest release](https://github.com/HolographicWings/TOTK-Mods-collection/releases)
</div>

</br>Mod description & usage :

- **FPS** : Changes the game's framerate lock  
If you get under the framerate lock defined by the mod, the game will be in slow motion.  
Vice versa if you get over the defined framerate lock.  
Cinematics will be sped up when you go over 30FPS.  
We recommend the 30fps version as the 60fps version is still a work in progress, 15 and 20 FPS being experimental and potentially useless.  
*Why should I use the 30fps mod ?* : In vanilla, the game seems to lock to 25 or 20 fps when you hit 29fps (This remains to be proven).  
</br>

- **Dynamic FPS** : Matches the game clock to your framerate and fixes slow motion when under the framerate lock, works well when coupled with any of the FPS mods above.  
This allows using it alongside the 30FPS mod and to uncheck the "Limit Speed Percent" in General settings as well as setting "VSync Mode" to OFF in Graphics settings (yuzu).  
This way, going over the framerate lock defined by the FPS mod will not 'speed up' your game.  
You can toggle the "Limit Speed Percent" with the "Ctrl + U" shortkey on yuzu.  
When you get a cinematic, enable back the "Limit Speed Percent" to avoid faster cutscenes.  
**BEWARE !** When you use Dynamic FPS mod under 15 FPS, the physics will break ! (Maybe fixed since v1.4, must check)
</br>

- Fix - **Cutscene Fix**: Sets the framerate lock to 30 FPS automatically during FMV cutscenes.  
You must have the Yuzu framerate lock enabled for this to work, and it needs to be paired with the FPS "60fps V3 - Cutscene-Fix-required" mod.
</br>

- Fix - **Over 30FPS Blackscreen Fix**: Fix blackscreen menu bug when playing above 30fps.  
:exclamation:Overwrites "Common.Product.110.Nin_NX_NVN.blarc", don't install two mods overwriting the same file.
This mod is present in the Xbox UI and Playstation UI mods, and should be disabled if using either of those, to avoid issues.  
</br>


- Graphics - **Disable Internal FSR Downscaling** : This mod disables the game's FSR, Yuzu has its own FSR in the "Window Adapting Filter" in Graphics settings.  
FSR is an optimisation method that reduces the game's internal resolution, and then upscales it using an algorithm (similar to DLSS but without advanced AI).  
FSR increases GPU performance, at the cost of some details and potential graphical artifacts on small geometry like leaves or grass.
</br>

- Graphics - **Disable Internal FSR Sharpening Shader** : This mod disables the sharpening effect of post processed FSR Downscaling internally.  
GPU Performance cost is extremely low so use it will not improve it, but could do an ugly render if you use it without the FSR Downscaling.  
**BEWARE !** It seems that this mod could be responsible for crashes on Ryujinx.  
</br>

- Graphics - **Disable Internal FXAA** : Disable internal FXAA and change "Anti-Aliasing Method" to "None" in order to increase GPU performance (?).
FXAA smoothes certain edges to avoid aliasing (jagged edges) and costs very little GPU performance.
Yuzu has its own FXAA in the "Anti-Aliasing Method" in Graphics settings, however, it has color banding issues currently, so we recommend SMAA, which currently is a better implementation of anti-aliasing, but uses a bit more GPU performance.     

> We're starting to doubt the mod will change anything, if you get any proof of its effect please share a screenshot or video with us.

</br>

- Graphics - **Disable Dynamic resolution** when low FPS : Prevents the resolution being downscaled when your framerate is low.
</br>

- Graphics - **LOD Patch** when low FPS : Prevents the LOD decreasing when your framerate is low.  
LOD (Level Of Detail) displays higher quality models when you are close to them, and lower quality models when they are further away.  
By default, when your framerate is low, the game lowers the LOD to increase GPU performance.  
Reported to fix some graphical issues with LOD, but would like image evidence.  
</br>

- Graphics - **Shadows** : changes the resolution of shadows. 
256 and 512 would increase GPU performance a lot.   
1024 being vanilla resolution, it is useless by default, but it can fix some graphical issues on certain setups.

  <div>
    <a href="https://imgsli.com/MTc5MTM1">
      Shadow stuttering issue took by Lux using a Radeon RX 580 8Gb - with & without Shadows x512
      <img src="https://imgsli.com/i/4f323aa4-343b-48b8-8744-e2126e89a011.jpg">
    </a>
    <a href="https://imgsli.com/MTc5MTYx">
      Gloom issue took by Red_BY using a RTX 2080 at 3x render scale - with & without Shadows x1024
      <img src="https://imgsli.com/i/7a0a0a8a-9ce2-4968-bcce-8d00741c70ed.jpg">
    </a>
  </div>
</br>

- Graphics - **Anisotropic Filtering fix** : Fixes Anisotropic Filtering issues ( black line artifacts on textures viewed at oblique angles). Set Anisotropic Filtering to 16 in Yuzu advanced graphics settings.  
[Difference Off/On](https://imgsli.com/MTc5MzQ0)
</br>

- **Resolution** : Changes internal render resolution, Vanilla is 1600x900 when the switch is docked.  
1080p (1920x1080) can only be scaled in 'doubles', or it will break Ambient Occlusion (AO) but increases GPU performance, which is useful for Reshade MXAO.  
Ambient occlusion is a shading and rendering technique used to calculate how exposed each point in a scene is to ambient lighting.
For example, the interior of a tube is typically more occluded (and hence darker) than the exposed outer surfaces, and becomes darker the deeper inside the tube one goes. It has a GPU performance cost.  
1008p is the highest resolution found to work without breaking the game's AO at any scaling settings, from our testing.  
360p, 540p and 720p require to change the "Resolution" scaling in Yuzu graphics settings (This setting is just called 'resolution'), but they look a bit blurry.  
  - 540p and x2 = 1080p
  - 540p and x4 = 4K
  - 540p and x8 = 8K
  - 720p and x2 = 1440p
  - 720p and x3 = 4K
  - 720p and x6 = 8K
To experience the best quality, we advise you to use the double of your monitor's resolution.  
You can use them with x1 Resolution scale to increase GPU performance.
</br>

- **Ratio** : Experimental - change the aspect ratio from 16:9.
  - You have to change "Aspect Ratio" in Graphics Yuzu settings to 21:9, 16:10 or "Stretch to Window" if the desired ratio doesn't exist.  
  - Fixes the 3D scene render, but will stretch the HUD.
</br>

- **Combos** : They are all-in-one mods, don't combine then with unspecified mods, if you don't know what you are doing.
  - **30/60fps + Dynamic FPS** are a simple Combo of these two mods, into one.
  - **Light pack and Unlimited FPS** : Pack made by HolographicWings, combine Dynamic FPS, 1008p and Disable FSR, it's a minimal pack for a clean experience.  
You can use it with any Graphics other pack, ratio and cheats but it's not recommended.  
In order to play above 30 FPS, press Ctrl + U in game to unlock your framerate, like that you can play at 60, or more, with normal game speed.
Don't forget to press Ctrl + U again, to lock back your framerate to 30fps, when you get a cutscene.
</br>

- Cheats :
  - 10x Durability overwrites all Weapons, Bows, Shields, don't install two mods overwriting the same file.
  - The Movement Speed cheats breaks the game time (time will be wrong when saving)
  - Stamina cheat doesn't seem to work.
  - Infinite amiibo usage is pointless since yuzu has a similar feature, go in Yuzu settings → Controls → Advanced and check "Use random Amiibo ID".

</br>
</br>The main TOTK performance issue comes from the CPU and not the GPU, but unfortunately we don't have an easy way of increasing CPU performance.  
</br>
</br>
</br>Other good mods :

- [Xbox UI + Blackscreenfix] (https://gamebanana.com/mods/443354) by Alerion921

- [Playstation UI + Blackscreenfix] https://gamebanana.com/mods/443201 by Alerion921

- [Amiibo Anti-RNG] https://gamebanana.com/mods/443894 by JordanBTucker


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

- [FPS - Cutscene-fix] : theboy181

- [Fix - Over 30FPS Blackscreen Fix](https://www.reddit.com/r/NewYuzuPiracy/comments/13hq70a/60_fps_mod_black_screen_fix_not_thoroughly_tested/) : by MarethyuX

- [Cheat - Durability (10x)] : SweetMini

- Others : A real mystery. We gather mods found on the yuzu reddit and discord, if you are the owner of one of them, please contact us, so we can give you the credit that you deserve!