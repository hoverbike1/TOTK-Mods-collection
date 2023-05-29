# Mods collection for Zelda: Tears of the Kingdom  

#  [SURVEY of your Emulation performance and Recommended configuration, Please reply.](https://github.com/HolographicWings/TOTK-Mods-collection/issues/72)👍  

## :exclamation:**WARNING : Read the "Compatible version.txt" in every mod to know which game version it is compatible with.**  

### [![Downloads badge](https://img.shields.io/github/downloads/HolographicWings/TOTK-Mods-collection/total.svg?style=for-the-badge)](https://github.com/HolographicWings/TOTK-Mods-collection/releases)  

### Compatibility chart (for mods with another version than your game) : 
![Compatibility guide](https://raw.githubusercontent.com/HolographicWings/TOTK-Mods-collection/main/Guide/Compatibility_chart.webp)

### Recommended setup :  

- Mods :  
  - Resolution - SweetMini 1008p - FXAA Off (or On, this is personal preference) - Includes FSR and DynRes Disabler - Zero AO Bugs
  - FPS - 60fps Static  
  - FPS - DynamicFPS v1.5.1 - Includes Cutscene Fix, Ultrahand Fix- Do not mix with fps++
  - Fix - Over 30FPS Blackscreen Fix (unless you are using a controller UI mod, which already has this)
  - Graphics - Anisotropic Filtering Fix - Set AF to 16 in Yuzu advanced graphics settings
  - Graphics - Disable LOD Quality Reduction
  - Graphics - LOD Improvement
  - Graphics - Shadows - 1024x - highest stable  
  
- Yuzu Graphics :  
  - Render API : Vulkan  
  - Use Disk Pipeline Cache: On  
  - Use asynchronous GPU emulation : On  
  - Accelerate ASTC Texture Decoding : On  
  - Vsync Mode: Mailbox (Or off if you don't mind frame tearing or use any alternate method for avoid it)  
  - NVDEC emulation : GPU Video Decoding (This is for cutscenes, try CPU Video Decoding if you have a weak gpu)  
  - Fullscreen Mode : Exclusive Fullscreen or Borderless Windowed and press F11  
  - Aspect Ratio : Default (16:9) (Use Strech to Window if using an aspect ratio mod)
  - Resolution : 2x or higher depending on your PC specs. This will multiply the render resolution, in vanilla ToTK it's 1600x900.
  - Window Adapting Filter : 
    - Bicubic if the render resolution is above your monitor resolution  
    - Bilinear if the render resolution is equal to your monitor resolution  
    - FSR if the render resolution is under your monitor resolution  
  - Anti-Aliasing Method : No AA or SMAA (FXAA break colors in darkness)  
  - FSR Sharpness : Set to taste, this setting only functions when Window Adapting Filter is set to FSR.  

- Yuzu Advanced Graphics :  
  - Accuracy Level : Normal (High has worse GPU performance, but with a lower risk of visual bugs, TotK does not currently need High except for debugging.)
  - ASTC recompression : Uncompressed (BC3 and BC1 lower the VRAM usage so it depend of your GPU VRAM amount, (BC3 for 4GB-8GB, BC1 for 2GB))  
  - Enable asynchronous presentation (Vulkan only): Off (framepacing is negatively impacted if you enable, only use if you are 1-2 fps from your locked fps target)  
  - Force maximum clocks (Vulkan only) : Off (possible small benefit if using very slow or fast hardware, but will waste power efficency)  
  - Decode ASTC textures asynchronously : Off ("On" may reduce texture loading stutters, but causes black squares and glitched loading screens)  
  - Enable Reactive Flushing : On (Improves syncing of memory)  
  - Use asynchronous shader building : On (Greatly reduces stuttering when shaders are compiling)  
  - Use Fast GPU Time : Off ("Off" has Higher Accuracy with "Dynamic FPS" and "FPS++" but for some reason "On" fixed a rare issue where FPS was extremely low and GPU usage extremely High, if you get that issue, try On and report the result to us please)  
  - Use Vulkan Pipeline Cache : On (Immense reduction in initial game loading time for AMD, improves shader compilation stutter for NVIDIA and Intel as well)  
  - Anisotropic Filtering : x8 or x16 (Will only work if you use the "Anisotropic Filtering Fix" mod, if you experience graphical bugs with an AMD card, switch back to Default)  
- Ryujinx settings :  
  - Need more documentation  

### Mod description & usage :  

- **FPS** : Changes the game's framerate lock  
If you are under the framerate lock defined by the mod, the game will be in slow motion, and sped up if you are over the defined framerate lock.  
Cinematics will be sped up when you go over 30FPS. You need to combine with a dynamic fps mod to fix this behavior.
*Why should I use the 30fps mod ?* : In vanilla, the game locks to 20 fps when you hit even 29fps, the mod corrects this.
</br>

- **Dynamic FPS** : Matches the game clock to your framerate and fixes slow motion when under the framerate lock, works well when coupled with any of the FPS mods above.  
This allows using it alongside the 30FPS mod and to uncheck the "Limit Speed Percent" in General settings as well as setting "VSync Mode" to OFF in Graphics settings (yuzu).  
This way, going over the framerate lock defined by the FPS mod will not 'speed up' your game.  
You can toggle the "Limit Speed Percent" with the "Ctrl + U" shortkey on yuzu.  
When you get a cinematic, enable back the "Limit Speed Percent" to avoid faster cutscenes.  
**BEWARE !** When you use Dynamic FPS mod under 15 FPS, the physics will break!.  
**BEWARE !** Incompatible with FPS++.
</br>

- **FPS++** : An edited version of the Dynamic FPS mod by "somerandompeople", fix cinematics above 30fps, do not use 30 or 60 FPS mods.
This mod is to fix the game slowing down or speeding up, its not something that increases your game performance.  
**BEWARE !** Incompatible with Dynamic FPS.
</br>

- Fix - **Cutscene Fix**: Sets the framerate lock to 30 FPS automatically during FMV cutscenes.  
You must have the Yuzu framerate lock enabled for this to work, and it needs to be paired with the 60FPS mod.
**BEWARE !** OBSOLETE if you are using Dynamic FPS or FPS++.
</br>

- Fix - **Over 30FPS Blackscreen Fix**: Fixes blackscreen menu bug when playing above 30fps.  
:exclamation:Overwrites "Common.Product.110.Nin_NX_NVN.blarc", don't install two mods overwriting the same file.  
This mod is already included in the Xbox UI and Playstation UI mods, and should be disabled if using either of those because they overwrite the same file.
</br>

- Graphics - **Disable Internal FSR Downscaling** : This mod disables the game's FSR, Yuzu has its own FSR in the "Window Adapting Filter" in Graphics settings.  
FSR is an optimisation method that reduces the game's internal resolution, and then upscales it using an algorithm (similar to DLSS but without advanced AI or temporal information).  
FSR increases GPU performance, at the cost of some details and potential graphical artifacts on small geometry like leaves or grass.  
It's recommended to use this mod with "Graphics - Disable Internal FSR Sharpening Shader" if you are on Yuzu.  
</br>

- Graphics - **Disable Internal FSR Sharpening Shader** : This mod disables the sharpening effect of post processed FSR Downscaling internally.  
GPU Performance cost is already extremely low so disabling it will not improve it.
Don't use this mod without "Graphics - Disable Internal FSR Downscaling".  
It's recommended to use this mod with "Graphics - Disable Internal FSR Sharpening Shader" if you are on Yuzu.  
**BEWARE !** It seems that this mod could be responsible for crashes on Ryujinx.  
</br>

- Graphics - **Disable Internal FXAA v2** : Disables TotK's internal FXAA.
FXAA smoothes edges to avoid aliasing (jagged edges) and costs very little GPU performance.  
Yuzu has its own FXAA in the "Anti-Aliasing Method" in Graphics settings, however, it has color banding issues currently, so we recommend SMAA, which currently is a better implementation of anti-aliasing, but uses a bit more GPU performance.   
:exclamation:Overwrites "Bootup.Nin_NX_NVN.pack.zs", don't install two mods overwriting the same file!
</br>

- Graphics - **Disable Dynamic resolution when low FPS** : Prevents the resolution being reduced when your framerate is under 30fps.
</br>

- Graphics - **LOD Improvement** : Increases the Level of Detail on certain models.  
LOD (Level Of Detail) shows higher quality models when you are close to them, and lower quality models when they are further away.  
Potentially has a minor performance impact.  
Compatible with "Disable LOD Quality Reduction" mod.  
https://imgsli.com/MTgyMzE5  
</br>

- Graphics - **Disable LOD Quality Reduction** when low FPS : Prevents the LOD decreasing when your framerate is under 30fps.  
LOD (Level Of Detail) shows higher quality models when you are close to them, and lower quality models when they are further away.  
By default, when your framerate is low, the game lowers the LOD to increase GPU performance, causing textures and models to visibly get worse.  
Compatible with "LOD Improvement" mod.  
</br>

- Graphics - **Island Fix** Fix the Outline edges around islands bugged over 2x resolution scalling.  
Only required if your resolution scale is over 1x.  
[Comparaison On/Off](https://i.imgur.com/M01IPBw.png)  
</br>

- Graphics - **Disable Targeting DOF** Disables the DOF blurring effect when targeting enemies or NPCs.  
DOF (Depth-of-Field is an effect that blur the background when an object is focused by the camera. This particular effect does not scale graphically with higher resolutions, so it may be desirable to disable it if you play at 2x or higher.  
</br>

- Graphics - **Shadows** : changes the resolution of shadows.  
256 and 512 would increase GPU performance a lot.  
1024 is the vanilla resolution, so it's useless by default, but it can fix some graphical issues on certain setups.  
[Shadow stuttering issue took by Lux using a Radeon RX 580 8Gb - with & without Shadows x512](https://imgsli.com/MTc5MTM1)  
[Gloom issue took by Red_BY using a RTX 2080 at 3x render scale - with & without Shadows x1024](https://imgsli.com/MTc5MTYx)  
</br>

- Graphics - **Anisotropic Filtering fix** : Fixes Anisotropic Filtering.  
Anisotropic Filtering is a render method that increase the texture quality in low angles.  
Set Anisotropic Filtering to 16 in Yuzu advanced graphics settings.  
[Difference Off/On](https://imgsli.com/MTc5MzQ0)  
</br>

- **Resolution** : Changes internal render resolution, Vanilla is 1600x900 when the switch is docked.  
:exclamation:Beware to don't confuse 1080p and 1008p !  
  - 1080p (1920x1080) when scaled over 1x resolution will break Ambient Occlusion (AO).  
  Ambient occlusion is a rendering technique that simulates the exposure of ambient light on an object.  
  [AO vs no AO](https://imgsli.com/MTc5MTI4/2/3)  
  Chuck done a fix about that, but require a custom yuzu build until a merge from the yuzu team.  
  - Chuck's 1008p (1792x1008) will not break AO over x1 resolution.  
  - Sweetmini's 1008p (1792x1008) will not break AO over x1 resolution, disable FSR and exist in two versions for FXAA on or off.  
  - 1026p (1824x1026) will not break AO over x1 resolution, disable FSR and exist in two versions for FXAA on or off but is known to break several things, we don't advice it.  
  :exclamation: the "New 1008p" overwrites "Bootup.Nin_NX_NVN.pack.zs", don't install two mods overwriting the same file.  
  - 360p, 540p and 720p require to change the "Resolution" scaling in Yuzu graphics settings (This setting is just called 'resolution'), but they look a bit blurry.  
    - 540p and x2 = 1080p.  
    - 540p and x4 = 4K.  
    - 540p and x8 = 8K.  
    - 720p and x2 = 1440p.  
    - 720p and x3 = 4K.  
    - 720p and x6 = 8K.  

You can use them with x1 Resolution scale or lower to increase GPU performance.  
To experience the best quality, we advise you to use the double of your monitor's resolution.  
</br>

- Resolution - 1080p OldManKain - Disable FSR-FXAA : From OldManKain based and theboy181.  
  - Break AO over 1x scale on Yuzu.  
  - As written in the name, this mod disable FSR and FXAA too.  
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
  - Lazy Pack are made by Hover and merge several useful mods.  
:exclamation:The versions without "UI Mod compatible" in their name Overwrites "Common.Product.110.Nin_NX_NVN.blarc.zs", don't install two mods overwriting the same file.  
</br>

#### "Lazy Packs"  

**A patch containing over a dozen fixes and mods, with the intent of "just making it work like its supposed to".**</br>  
"Lazy packs" are customized according to resolution, framerate, and UI mod compatibility.  
UI compatibility means that the patch is compatible with mods such as the Xbox UI mod below.  
Otherwise, blackscreenfix is enabled in the non-compatible versions, for use with normal Nintendo UI.  
Using an non-compatible version, along with a UI mod, will result in the UI mod largely not functioning, or not at all.  
Please see below for details on how to use, and below that, the exact contents of the patch, and credits to the developers of them.  
</br>

<details><summary> Click to view how to use the lazy pack</summary>

[Follow this guide to configure Yuzu correctly for Tears of the Kingdom.](https://github.com/HolographicWings/TOTK-Mods-collection/tree/main/Guide)

- Install Tears of the Kingdom Patch 1.1.0. or 1.1.1.
- Decide on a framerate. 30 or 60?
- Decide on a resolution. 720p, 1080, 1440p, 4K or 8K?
- Decide if you want to use the Nintendo controller UI, or a UI mod, such as the Xbox and Playstation mods linked above.

Take this pack as an example:
1.1.0 - Lazy Pack - **60 FPS** - **720P 1X** - **1440P 2X** - **4K 3X** - **8K 6X** - scaling - **UI Mod compatible**

- This patch features 60 FPS.
- It scales between 720p, 1440p, 4K and 8K, depending on what resolution scaling you choose in Yuzu's graphics settings, as shown in picture 7 in the guide below, for reference.
- And it features compatibility with UI controller mods, such as the Xbox or Playstation mods linked above.

If you were to decide to target **30 FPS**, **1080p**, and you would like the **Steam Deck UI**, you should choose:
1.1.0 - Lazy Pack - **30 FPS** - **1080P 1X scaling** - **UI Mod compatible**

And, if you were to decide to play on a beefy **1080p** PC at **60 FPS**, using your Switch Pro controller, and you would like the **Normal, Nintendo controller UI**, you should choose:
1.1.0 - Lazy Pack - **60 FPS** - **1080P 1X scaling**

The non-compatible versions contain Blackscreen-fix, which is incompatible with UI mods.
</details>

<details><summary>Click to view the patches included in the lazy pack </summary>

// Credit: @Wollnashorn
// Force bilinear terrain samplers to be trilinear
// Set mipmap filter to nearest on shadow map sampler

// Credit: @Marethyu
// Blackscreen-fix

// Credit: @ChucksFeedAndSeed
// Disable Dynamic Resolution
// Disable FSR sharpening filter
// Shadow Resolution set to 1024
// FXAA disabled
// LOD fix

// Credit: @Patchanon
// Disable FSR up/downscaling
// 1080p v1.1.0
// Disable LOD reduction when framerate dips v1.1.0

// Credit: @somerandompeople
// SOURCED FROM [HERE](https://gbatemp.net/download/loz-tears-of-the-kingdom-20fps-30fps-60fps-patch.37996/)
// 30/60 FPS++
// Disable LOD reduction when framerate dips v1.1.1

// Credit: @ChanseyIsTheBest
// Docked 720p

// Credit: @OldManKain
// 1080p, Disabled FXAA and FSR scaler v1.1.1
</details>
</br>

- Cheats :
  - 10x Durability overwrites all Weapons, Bows, Shields, don't install two mods overwriting the same file.
  - The Movement Speed cheats breaks the game time (time will be wrong when saving)
  - Stamina cheat doesn't seem to work.
  - Infinite amiibo usage is pointless since yuzu has a similar feature, go in Yuzu settings → Controls → Advanced and check "Use random Amiibo ID".
  - Beware, all cheats can cause unwanted side effects.

</br>
</br>The main TOTK performance issue comes from the CPU and not the GPU, but unfortunately we don't have an easy way of increasing CPU performance.  
</br>
</br>
</br>Other good mods :

- [Xbox / Steam Deck UI + Blackscreenfix](https://gamebanana.com/mods/443354) by Alerion921

- [Playstation UI + Blackscreenfix](https://gamebanana.com/mods/443201) by Alerion921

- [Amiibo Anti-RNG](https://gamebanana.com/mods/443894) by JordanBTucker

- [Updated 1.1.1 Cheat Codes](https://github.com/bad1dea/NXCheats/tree/main/The%20Legend%20of%20Zelda%20Tears%20of%20the%20Kingdom/0100F2C0115B6000%20for%20Yuzu) by bad1dea

</br>Useful links :

- [Save Editor](https://www.marcrobledo.com/savegame-editors/zelda-totk/) by Marc Robledo
</br>

> Thanks to [ChucksFeedAndSeed](https://www.reddit.com/user/ChucksFeedAndSeed/) for the *majority* of the mods in this collection.

</br>Copyright and source of mods :

- [20/30 and 60 fps v3](https://gbatemp.net/download/loz-tears-of-the-kingdom-20fps-30fps-60fps-patch.37996/) : Authors are "ChucksFeedAndSeed, patchanon and somerandompeople"

- [DynamicFPS v1.31 & 1.4](https://gbatemp.net/download/loz-tears-of-the-kingdom-fps-static-fps-and-visual-fixes-patch-collection.37996/) : ChucksFeedAndSeed

- [FPS++](https://gbatemp.net/download/loz-tears-of-the-kingdom-fps-static-fps-and-visual-fixes-patch-collection.37996/) : somerandompeople

- New 1008p Resolution : SweetMini, contribution by Socats and Darktalon

- 1080p resolution : ChucksFeedAndSeed

- [Combo - VisualFixes](https://gbatemp.net/download/loz-tears-of-the-kingdom-20fps-30fps-60fps-patch.37996/) : Authors are "ChucksFeedAndSeed, patchanon and somerandompeople"

- All Graphic pactches : Authors are "ChucksFeedAndSeed, patchanon and somerandompeople", theses patches are split from the VisualFixes, FSR Disabler is especially from patchanon

- [Aspect Ratio](https://gamebanana.com/mods/443462) : From Fayaz

- [Graphics - Anisotropic filtering fix](https://github.com/Wollnashorn/switch-mods/tree/master/0100F2C0115B6000) : @Wollnashorn

- FPS - Cutscene-fix : theboy181

- Graphic - Disable Targeting DOF : theboy181

- Fix - Over 30FPS Blackscreen Fix : by MarethyuX

- Cheat - Durability (10x) : SweetMini

- Cheat - Time of day : FrostedMint  
Unknown compatibily with FPS, Dynamic FPS and FPS++ mods, testing is required, open an issue to report the result if you tried.  

- Graphics - Disable Internal FXAA v2 : SweetMini

- Resolution - 1026p : Zeikken

- Others : A real mystery. We gather mods found on the yuzu reddit and discord, if you are the owner of one of them, please contact us, so we can give you the credit that you deserve!
