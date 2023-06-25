# Mods collection for Zelda: Tears of the Kingdom (TOTK)

#  [SURVEY of your Emulation performance and Recommended configuration, Please reply.](https://github.com/HolographicWings/TOTK-Mods-collection/issues/72)👍

## :exclamation:**WARNING : Read the "Compatible version.txt" in every mod to know which game version it is compatible with.**

## Download page : [![Downloads badge](https://img.shields.io/github/downloads/HolographicWings/TOTK-Mods-collection/total.svg?style=for-the-badge)](https://github.com/HolographicWings/TOTK-Mods-collection/releases)

[![Recommended Settings](https://raw.githubusercontent.com/HolographicWings/TOTK-Mods-collection/main/Guide/YuzuRecommendedSettings_Light.webp)](https://github.com/HolographicWings/TOTK-Mods-collection/blob/main/SETUP.md#gh-light-mode-only)
[![Recommended Settings](https://raw.githubusercontent.com/HolographicWings/TOTK-Mods-collection/main/Guide/YuzuRecommendedSettings_Dark.webp)](https://github.com/HolographicWings/TOTK-Mods-collection/blob/main/SETUP.md#gh-dark-mode-only)

## Mod description & usage:

- FPS - **20fps/30fps/60fps Static:** Changes the game's framerate lock. Use with DynamicFPS.
</br>The game will be in slow motion if you are under the framerate indicated and speed up if you are over, including cutscenes. Combine with a dynamic fps mod to fix this behavior.
</br>*Why use the 30fps mod?* : The game locks to 20 fps if your framerate is anything lower than 30, the mod corrects this.

- FPS - **Dynamic FPS:** Matches the game clock to your framerate and fixes slow motion/speed up. Recommended to use with FPS mods above.
</br>Alternativelly you can uncheck the Yuzu's "Limit Speed Percent" in General settings (Ctrl + U) as well as setting "VSync Mode" to OFF without 'speed up' your game.
</br>**BEWARE!** When you use Dynamic FPS mod under 15 FPS, the physics will break!.
</br>**BEWARE!** Incompatible with DynamicFPS++.

- FPS - **DynamicFPS++:** An alternative version of the Dynamic FPS mod by "somerandompeople", do not use 20, 30 or 60 FPS mods (its included already).
</br>This mod may have less stuttering depending on your hardware. We recommend to test by yourself and compare with the combo Dynamic FPS and FPS 30/60 mods.
</br>**BEWARE!** Incompatible with Dynamic FPS.

- FPS - **Fix - UI Blackscreen Fix:** Fixes black background on weapon switch UI when playing above 30fps.
</br>:exclamation:Overwrites "Common.Product.110.Nin_NX_NVN.blarc", don't install two mods overwriting the same file.
</br>This mod overwrite the Xbox UI and Playstation UI mods. Use the version "fix" of these mods instead (they include the Blackscreen-fix).

- Graphics - **Disable Internal FSR Downscaling:** This mod disables the game's internal FSR. Do not mistake with Yuzu's own FSR on the "Window Adapting Filter" in Graphics settings.
</br>FSR is an optimisation method that upscales the game resolution using several algorithms (similar to DLSS but without advanced AI or temporal information). It can increase GPU performance at the cost of some details and potential graphical artifacts.
</br>Disable FSR if you are using better methods like Yuzu's FSR or even better: using real improved resolution.

- Graphics - **Disable Internal FXAA v2:** Disables TotK's internal FXAA.
</br>FXAA smoothes edges to avoid aliasing (jagged edges) and costs very little GPU performance.
</br>If you want a better anti aliasing, we recommend using SMAA on the "Anti-Aliasing Method" in Graphics settings (at a slightly cost on GPU performance). Using a resolution above your monitor can also work as anti-alising, but have high cost on your GPU (see the **Resolution** section).
</br>:exclamation:Overwrites "Bootup.Nin_NX_NVN.pack.zs", don't install two mods overwriting the same file!

- Graphics - **Disable Internal FXAA ExeFS:** uses the exefs method instead of romfs, which FXAA v2 uses, which should have less issue with incompatibility with other mods.

- Graphics - **LOD Improvement:** Increases the Level of Detail on certain models.
</br>LOD (Level Of Detail) shows higher quality models when you are close to them, and lower quality models when they are further away.
</br>Has a minor performance improvement (we spent days testing on different hardware to believe it). Our theory is that less model swappings helps the emulator because there's less things changing at the same time.
</br>[Comparison On/Off](https://imgsli.com/MTgyMzE5)

- Graphics - **Disable LOD Quality Reduction:** Prevents the LOD decreasing when your framerate is under 30fps.
</br>LOD (Level Of Detail) shows higher quality models when you are close to them, and lower quality models when they are further away.
</br>By default, when your framerate is low, the game lowers the LOD to increase GPU performance, causing textures and models to visibly get worse.
</br>**BEWARE!** Mandatory if using Chucks Resolution Mods (Or another Pchtxt resolution Mod). Not necessary with Sweetmini resolution Mods, especially if you use LOD Improvement Mod.

- Graphics - **Island Fix:** Fix the Outline edges around the Sky Islands bugged over 2x resolution scaling.
</br>Only required if your Resolution scale in Graphics settings" is over 1x. May cause edge artifacts.
</br>[Comparison On/Off](https://i.imgur.com/M01IPBw.png)

- Graphics - **Disable Targeting DOF:** Disables the Depth-of-Field blurring effect when targeting enemies or NPCs.
</br>DOF (Depth-of-Field) is an effect that blurs the background when an object is focused by the camera. Install if you don't like the effect.

- Graphics - **Shadows:** Changes the resolution of shadows.
</br>256 and 512 could possibly increase your game performance if you are GPU bounded, but sacrifices shadow quality.
</br>Original game has shadow quality at 960 or below.
</br>1024 will improve shadow quality, and it can fix some graphical issues on certain setups.
</br>[Shadow stuttering issue took by Lux using a Radeon RX 580 8Gb - with & without Shadows x512](https://imgsli.com/MTc5MTM1)
</br>[Gloom issue took by Red_BY using a RTX 2080 at 3x render scale - with & without Shadows x1024](https://imgsli.com/MTc5MTYx)

- Graphics - **Anisotropic Filtering fix:** Fixes Anisotropic Filtering.
</br>Anisotropic Filtering increase the texture quality when textures are viewed at oblique angles, like the floor at distance.
</br>It's not needed on new Yuzu versions anymore! Use only if you are stuck with old versions (Before mainline 1473 of EA 3580)
</br>Set Anisotropic Filtering to 16 in Yuzu advanced graphics settings.
</br>[Difference Off/On](https://imgsli.com/MTc5MzQ0)

- Graphics - **Camera JPEG Quality Increase:** Enhance the picture quality allowing camera photos to look much better quality & less compressed.
</br>:exclamation: If you disable this mod & then play the game with any photos saved from using this mod, your albums tab will likely hang the game while any larger photos are still around.
You can clear the photos by just going into your savegame album folder & deleting them, anything larger than 64KB was likely taken from this mod.
</br>**BEWARE!** "Camera JPEG Quality Increase" overwrites "Bootup.Nin_NX_NVN.pack.zs", don't install two mods overwriting the same file like **Sweetmini resolution mods and FXAA Disabler**.

- Graphics - **Increased Camera Speed:** Increases in-game camera speeds, which can be adjusted ingame using the control settings in the menu.

- **Resolution:** Changes internal rendering resolution. Original is 1600x900 in Docked mode and 1280x720 in Handheld mode.
</br>:exclamation:Don't confuse 10**8**0p and 100**8**p, they aren't the same number!
  
  - Chuck's 10**8**0p (1920x1080) resolution.
  
  - Chuck's 100**8**p (1792x1008) resolution.
  
  - SweetMini's 100**8**p (1792x1008) Automatically disables FSR, disables dynamic resolution, and exists in two versions for FXAA on or off.
  </br>:exclamation:"SweetMini 1008p" overwrites "Bootup.Nin_NX_NVN.pack.zs", don't install two mods overwriting the same file.
  
  - SweetMini's 10**8**0p (1920x1080) Automatically disables FSR, disables dynamic resolution, and exists in two versions for FXAA on or off.
  </br>:exclamation:"SweetMini 1008p" overwrites "Bootup.Nin_NX_NVN.pack.zs", don't install two mods overwriting the same file.
  
  - 1026p (1824x1026) Automatically disables FSR, disables dynamic resolution, and exists in two versions for FXAA On or Off. Can cause artifacts in shadows, we don't recommend this option anymore.
  </br>:exclamation:"1026p" overwrites "Bootup.Nin_NX_NVN.pack.zs", don't install two mods overwriting the same file.
  
  - 10**8**0p OldManKain - Disable FSR-FXAA : From OldManKain based and theboy181.
    - As written in the name, this mod disables FSR and FXAA too.
    - Uses code editing instead of game file editing.
  
  - 540p and 720p require to change the "Resolution" scaling in Yuzu Graphics Settings to reach your monitor resolution or better. Use the table bellow:  
    - 540p and x2 = 1080p.
    - 540p and x4 = 4K.
    - 540p and x8 = 8K.
    - 720p and x2 = 1440p.
    - 720p and x3 = 4K.
    - 720p and x6 = 8K.
    
    :exclamation:Some elements like the UI and Ambient Occlusion may not scale and can look worse than other resolution mods.</br>

You can use resolution mods with x1 Resolution scale or lower to increase GPU performance.
To experience the best visual quality, we advise using an internal rendering resolution of double the monitor's resolution.
</br></br>


- **Aspect Ratio:** Applies changes to the 3D scene render and UI elements to fit different aspect ratios
</br>Set "Aspect Ratio" in Graphics Yuzu settings to "Stretch to Window"
</br>Disable BlackscrenFix (already included)
</br>Incompatible with controller mods (can be merged using custom tool)
</br>UI rescaling only works for 16:10 and ultrawide (>16:9) aspect ratios
</br>

### Performance
The main TOTK performance issue comes from the CPU and not the GPU, but unfortunately we don't have an easy way of increasing CPU performance.

### "Lazy Packs"

**A patch containing over a dozen fixes and mods, with the intent of "just making it work like its supposed to".**</br>
"Lazy packs" are are made by Hoverbike and merge several useful mods. They are customized according to resolution, framerate, and UI mod compatibility.
UI compatibility means that the patch is compatible with mods such as the Xbox UI mod below.
Otherwise, blackscreenfix is enabled in the non-compatible versions, for use with normal Nintendo UI.
Using an non-compatible version, along with a UI mod, will result in the UI mod largely not functioning, or not at all.
Please see below for details on how to use, and below that, the exact contents of the patch, and credits to the developers of them.

<details><summary> Click to view how to use the lazy pack</summary>
<a href="https://github.com/HolographicWings/TOTK-Mods-collection/blob/main/Guide/Guide.pdf">Follow this guide to configure Yuzu correctly for Tears of the Kingdom.</a><br>
Update your Tears of the Kingdom - I recommend 1.1.2, however, the patches work on all versions of the game.<br>
Pick a single Lazy Pack that suits your needs.
Decide on a framerate. 30 or 60?<br>
Decide on a resolution. 720p, 1080p, 1440p, 4K or 8K?<br>
Decide if you want to use the Nintendo controller UI, or a UI mod, such as the Xbox and Playstation mods linked below, some of which we also ship in the archive.<br>
<br>

Here are some examples:
<b>60 FPS</b> -  <b>1440p 2X</b> - <b>2880p 4X</b> - <b>UI Mod compatible</b>
- This patch caps at 60 FPS.
- It is intended to scale between 1440p and 2880p (supersampled 1440p for those <b>crisp</b> visuals) depending on what resolution scaling you choose in Yuzu's graphics settings, as shown in picture 7 in the guide below, for reference.
- And it features compatibility with UI controller mods, such as the Xbox, Playstation and Steam Deck UI Mods.

If you were to decide to target <b>30 FPS</b>, <b>1080p</b>, and you would like the <b>Xbox UI</b>, you should choose:
<b>30 FPS</b> - <b>1080P 1X</b> - <b>UI Mod Compatible</b> - and set the scaling in Yuzu to X1, in order to achieve 1080p - and enable the Xbox UI Mod.

If you were to decide to play on a beefy <b>1080p</b> PC at <b>60 FPS</b>, using your Switch Pro controller, and you would like the <b>Normal, Nintendo controller UI</b>, you should choose:
<b>60 FPS</b> - <b>1080P 1X</b> - and set the scaling in Yuzu to X1, in order to achieve 1080p - with no controller mod, to use the default nintendo icons and layout, and blackscreen-fix prepackaged in this non-ui compatible lazy patch.

If you were to decide to play on a <b>SUPER</b> beefy <b>4K</b> PC at <b>60 FPS</b>, using your Playstation controller, and you would like the <b>Playstation controller UI</b>, you should choose:
<b>60 FPS</b> - <b>4K 2X</b> - <b>8K 4X</b> - <b>UI Mod Compatible</b> - and set the scaling in Yuzu to X2, in order to achieve 1080p x 2 = 2160p - along with enabling the Playstation UI Mod.

The non-UI compatible versions contain Blackscreen-fix, which is incompatible with UI mods, and must be combined correctly, to avoid issues that arise from conflicting fixes. The UI Mods make changes to the same files as blackscreen-fix - so make sure to combine/avoid combining these according to what you're trying to do.
  
If you experience any issues with Lazy Packs, please feel free to contact me on discord at Hoverbike#8377 or @hoverbike1 
</details>

<details>
<summary>Click to view the patches included in the lazy pack </summary>

// Credit: @Wollnashorn<br>
// Force bilinear terrain samplers to be trilinear<br>
// Set mipmap filter to nearest on shadow map sampler<br>
<br>

// Credit: @ChucksFeedAndSeed<br>
// Shadow Resolution set to 1024<br>
// Disable LOD Reduction 1.1.0/1.1.1/1.1.2<br>
// Disable FSR Scaling 1.1.0/1.1.1/1.1.2<br>
// DynamicFPS 1.5.2<br>
<br>

// Credit: @Patchanon<br>
// 1080p Resolution 1.1.0<br>
// Disable FSR Scaling 1.0.0<br>
// Disable LOD Reduction 1.0.0<br>
<br>

// Credit: @somerandompeople<br>
// SOURCED FROM https://gbatemp.net/download/loz-tears-of-the-kingdom-20fps-30fps-60fps-patch.37996/<br>
// 30/60 FPS Static<br>
<br>

// Credit: @bad1dea<br>
// 720p resolution 1.1.0/1.1.1/1.1.2<br>
<br>

// Credit: @Sweetmini<br>
// Sky Island Fix 1.1.1/1.1.2<br>
// LOD Improvement 1.1.1/1.1.2<br>
// Lens Flare Removal 1.1.1/1.1.2<br>
<br>
  
// Credit: @StevensND<br>
// Blackscreen-fix 1.0.0 <br>
<br>

// Credit: @MaxLastBreath<br>
// Sky Island Fix 1.0.0<br>
// Lens Flare Removal 1.0.0<br>
// 1080p resolution 1.0.0<br>
// 720p resolution 1.0.0<br>
<br>

// Credit: @OldManKain & @theboy181<br>
// 1080p Resolution 1.1.1/1.1.2<br>
// Disable FXAA<br>
<br>

// Credit: @theboy181 <br>
// DOF Removal <br>
// Sky Island Fix <br>
// LOD Improvement <br>
// Lens Flare Removal <br>
<br>
  
// Credit: @Marethyu<br>
// Blackscreen-fix<br>
<br>

</details>

## Cheats
  - 10x Durability overwrites all Weapons, Bows, Shields, don't install two mods overwriting the same file.
  - The Movement Speed cheats breaks the game time (time will be wrong when saving)
  - Stamina cheat doesn't seem to work.
  - Infinite amiibo usage is pointless since yuzu has a similar feature, go in Yuzu settings → Controls → Advanced and check "Use random Amiibo ID".
  - **Beware, all cheats can cause unwanted side effects.**

## Other good mods

- [Controller UI Mods (Playstation/Xbox/SteamDeck](https://gamebanana.com/members/1944248) by Alerion921
- [Amiibo Anti-RNG](https://gamebanana.com/mods/443894) by JordanBTucker
- [Updated 1.1.1 and 1.1.2 Cheat Codes](https://github.com/bad1dea/NXCheats/tree/main/The%20Legend%20of%20Zelda%20Tears%20of%20the%20Kingdom) by bad1dea.
- [21'9 V2/HUD Fix v7 + Controller UI (Xbox&PS)](https://gamebanana.com/mods/447208) by Jaddey
- [32'9 V2/HUD Fix V7 + Controller UI (Xbox&PS)](https://gamebanana.com/mods/449128) by Jaddey

## Useful links

- [Save Editor](https://www.marcrobledo.com/savegame-editors/zelda-totk/) by Marc Robledo

## Copyright and source of mods

- [20/30 and 60 fps v3](https://gbatemp.net/download/loz-tears-of-the-kingdom-20fps-30fps-60fps-patch.37996/) : Authors are "ChucksFeedAndSeed, patchanon and somerandompeople"
- [DynamicFPS](https://gbatemp.net/download/loz-tears-of-the-kingdom-fps-static-fps-and-visual-fixes-patch-collection.37996/) : ChucksFeedAndSeed
- [DynamicFPS++](https://gbatemp.net/download/loz-tears-of-the-kingdom-fps-static-fps-and-visual-fixes-patch-collection.37996/) : somerandompeople
- SweetMini 1008p and 1080p Resolution : SweetMini, contribution by Socats and Darktalon
- 1080p Resolution : ChucksFeedAndSeed
- Graphic patches : Authors are "ChucksFeedAndSeed, patchanon and somerandompeople", theses patches are split from the VisualFixes, FSR Disabler is from patchanon
- [Aspect Ratio](https://gamebanana.com/mods/443462) : From Fayaz
- [Graphics - Anisotropic filtering fix](https://github.com/Wollnashorn/switch-mods/tree/master/0100F2C0115B6000) : @Wollnashorn
- FPS - Cutscene-fix : theboy181
- Graphics - Disable Targeting DOF : theboy181
- Graphics - Island Fix : theboy181
- Graphics - LOD Improvement : theboy181
- Graphics - Remove Lens Flare : theboy181
- Ports to 1.1.1/1.1.2 by Sweetmini
- Fix - UI Blackscreen Fix : by MarethyuX
- [Cheat - 1.1.1 & 1.1.2 Cheats](https://github.com/bad1dea/NXCheats/tree/main/The%20Legend%20of%20Zelda%20Tears%20of%20the%20Kingdom) : By bad1dea
- [Cheat - 1.1.0 & 1.1.1 Cheats](https://gbatemp.net/threads/the-legend-of-zelda-tears-of-the-kingdom-nintendo-switch-cheats.632193/)
- Cheat - Durability (10x) : SweetMini
- Cheat - Time of day : FrostedMint
  </br>Unknown compatibily with FPS, Dynamic FPS and DynamicFPS++ mods, testing is required, open an issue to report the result if you tried.
- Graphics - Disable Internal FXAA v2 : SweetMini
- Graphics - Vertical Sensitivity Fix: igoticecream
- Resolution - 1026p : Zeikken
- Thanks to MaxLastBreath for providing us with ports to 1.0.0 of Island Fix, LOD Improvements, Lens Flare Removal and 1080p & 1008p resolution patches.
- [Thanks to Fruithapje for providing us with every aspect ratio mod we could need!](https://github.com/Fruithapje21/TOTK-Ultrawide)
