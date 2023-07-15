# Mods collection for Zelda: Tears of the Kingdom (TOTK)

#  [SURVEY of your Emulation performance and Recommended configuration, Please reply.](https://github.com/HolographicWings/TOTK-Mods-collection/issues/72)👍

## :exclamation:**WARNING : Read the "Compatible version.txt" in every mod to know which game version it is compatible with.**

## Download page : [![Downloads badge](https://img.shields.io/github/downloads/HolographicWings/TOTK-Mods-collection/total.svg?style=for-the-badge)](https://github.com/HolographicWings/TOTK-Mods-collection/releases)

[![Recommended Settings](https://raw.githubusercontent.com/HolographicWings/TOTK-Mods-collection/main/Guide/YuzuRecommendedSettings_Light.webp)](https://github.com/HolographicWings/TOTK-Mods-collection/blob/main/SETUP.md#gh-light-mode-only)
[![Recommended Settings](https://raw.githubusercontent.com/HolographicWings/TOTK-Mods-collection/main/Guide/YuzuRecommendedSettings_Dark.webp)](https://github.com/HolographicWings/TOTK-Mods-collection/blob/main/SETUP.md#gh-dark-mode-only)

## Mod description & usage:

- FPS - **Dynamic FPS:** Matches the game clock to your framerate and fixes slow motion/speed up. Recommended to use with FPS mods above.
</br>Alternativelly you can uncheck the Yuzu's "Limit Speed Percent" in General settings (Ctrl + U) as well as setting "VSync Mode" to OFF without 'speed up' your game.
</br>**BEWARE!** When you use Dynamic FPS mod under 15 FPS, the physics will break!. Some issues also can happen above 60fps.
</br>**BEWARE!** On version 1.5.5 or higher, use with **Dynamic FPS - 20/30/45/60FPS AND Resolutions!**
</br>**BEWARE!** On version 1.5.4 or higher, use with **Dynamic FPS - 20/30/45/60FPS**.
</br>**BEWARE!** On version 1.5.3 or below, use with **20fps/30fps/60fps Static**.

- FPS - **Dynamic FPS - 20/30/45/60FPS:** Configuration files for DynamicFPS 1.5.4 or newer. Use only one of the options with DynamicFPS 1.5.4. You can edit the .ini file inside to whathever FPS you want! :D (may cause issues bellow 20fps and above 60fps)
</br>*Why use the 30fps mod?* : The game locks to 20 fps if your framerate is anything lower than 30, the mod corrects this.

- FPS - **20fps/30fps/60fps Static:** Changes the game's framerate lock. Use with DynamicFPS 1.5.3 or bellow.
</br>The game will be in slow motion if you are under the framerate indicated and speed up if you are over, including cutscenes. Combine with a dynamic fps mod to fix this behavior.
</br>*Why use the 30fps mod?* : The game locks to 20 fps if your framerate is anything lower than 30, the mod corrects this.

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

- Graphics - **Disable Internal FXAA ExeFS:** uses the exefs method instead of romfs, which FXAA v2 uses. This should have less compatibility issues with other mods.

- Graphics - **LOD Improvement:** Increases the Level of Detail on certain models.
</br>LOD (Level Of Detail) shows higher quality models when you are close to them, and lower quality models when they are further away.
</br>Has a minor performance improvement (we spent days testing on different hardware to believe it). Our theory is that less model swappings helps the emulator because there's less things changing at the same time.
</br>[Comparison On/Off](https://imgsli.com/MTgyMzE5)

- Graphics - **Disable Quality Reduction:** Prevents graphics quality decreasing when your framerate is under 30fps.
</br>LOD (Level Of Detail) shows higher quality models when you are close to them, and lower quality models when they are further away.
</br>By default, when your framerate is low, the game lowers the LOD to increase GPU performance, causing textures and models to visibly get worse.
</br>When this happens the game also reduce the resolution, causing pixelated images.
</br>**BEWARE!** Mandatory if using Chucks Resolution Mods (Or another Pchtxt resolution Mod). Not necessary with Sweetmini resolution Mods, especially if you use LOD Improvement Mod.

- Graphics - **Sky Island Fix for XX Resolution:** Fix bugged Outline edges around distant Sky Islands  over 2x Resolution scaling.
</br>Use only one option, corresponding to the resolution scale currently being used.
</br>Only required if your Resolution scale in "Graphics settings" is over 1x. May cause edge artifacts.
</br>[Comparison Off/On](https://i.imgur.com/M01IPBw.png)

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

- Graphics - **First Person +**: Changes camera to first person view. Different versions offer different fields of view (FOV)
</br>  For 16:9 or 16:10 screens we recommend either (Narrow 70 FOV) or (Normal 90 FOV)
</br>  For 21:9 and upwards, we recommend either (Normal 90 FOV) or (Wide 110 FOV)

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


**Aspect Ratio:** Applies changes to the 3D scene render and UI elements to fit different aspect ratios
- Set "Aspect Ratio" in Graphics Yuzu settings to "Stretch to Window"
- Disable BlackscrenFix (already included)
- Incompatible with controller mods (can be merged using custom tool)
- UI rescaling only works for 16:10 and ultrawide (>16:9) aspect ratios
</br>

### Performance
The main TOTK performance issue comes from the CPU and not the GPU, but unfortunately we don't have an easy way of increasing CPU performance.

### "Lazy Pack Generator"

**A script containing over a dozen fixes and mods, with the intent of "just making it work like its supposed to".**</br>
"Lazy pack generator" is a script made by Hoverbike.
Simply run the exe, select your desired resolution, framerate, and preferred controller UI, and click "Generate!"

<details><summary> Click to view how to use the lazy pack generator</summary>
<a href="https://github.com/HolographicWings/TOTK-Mods-collection/blob/main/Guide/Guide.pdf">Follow this guide to configure Yuzu correctly for Tears of the Kingdom.</a><br>
Update your Tears of the Kingdom - I recommend 1.1.2, however, the patches work on all versions of the game.<br>
Select a resolution.<br>
Select a framerate.<br>
Select your preferred controller user interface.<br>
Click "Generate!"<br>
Thats it! The patch has been installed in Yuzu's mod directory, it has been enabled by default, and your settings has been changed to reflect your choices made in the generator.
If you experience any issues with the Lazy Pack Generator, please feel free to contact me on discord at Hoverbike#8377 or @hoverbike1, or simply create an issue on our issue tracker.
</details>

<details>
<summary>Click to view the patches included in the lazy pack generator </summary>

// Credit: @ChucksFeedAndSeed
// Disable LOD Reduction 1.1.0/1.1.1/1.1.2
// Disable FSR Scaling 1.1.0/1.1.1/1.1.2
// DynamicFPS 1.5.5 beta 1
<br>

// Credit: @Patchanon
// Disable FSR Scaling 1.0.0
// Disable LOD Reduction 1.0.0
<br>

// Credit: @Sweetmini
// LOD Improvement 1.1.1/1.1.2 ports
<br>
  
// Credit: @OldManKain & @theboy181
// Disable FXAA
<br>

// Credit: @theboy181
// LOD Improvement
<br>
  
// Credit: @Marethyu
// Blackscreen-fix
<br>

// Credit: @StevensND
// Porting many patches to 1.2.0
<br>

</details>

## Cheats
  - 10x Durability overwrites all Weapons, Bows, Shields, don't install two mods overwriting the same file.
  - The Movement Speed cheats breaks the game time (time will be wrong when saving)
  - Stamina cheat doesn't seem to work.
  - Infinite amiibo usage is pointless since yuzu has a similar feature, go in Yuzu settings → Controls → Advanced and check "Use random Amiibo ID".
  - **Beware, all cheats can cause unwanted side effects.**

## Other good mods

- [Controller UI Mods (Playstation/Xbox/SteamDeck)](https://gamebanana.com/members/1944248) by Alerion921
- [Amiibo Anti-RNG](https://gamebanana.com/mods/443894) by JordanBTucker
- [Updated 1.1.1 and 1.1.2 Cheat Codes](https://github.com/bad1dea/NXCheats/tree/main/The%20Legend%20of%20Zelda%20Tears%20of%20the%20Kingdom) by bad1dea.
- [21'9 V2/HUD Fix v7 + Controller UI (Xbox&PS)](https://gamebanana.com/mods/447208) by Jaddey
- [32'9 V2/HUD Fix V7 + Controller UI (Xbox&PS)](https://gamebanana.com/mods/449128) by Jaddey

## Useful links

- [Save Editor](https://www.marcrobledo.com/savegame-editors/zelda-totk/) by Marc Robledo

## Copyright and source of mods

- [20/30 and 60 fps v3](https://gbatemp.net/download/loz-tears-of-the-kingdom-20fps-30fps-60fps-patch.37996/) : Authors are "ChucksFeedAndSeed, patchanon and somerandompeople"
- [DynamicFPS](https://www.reddit.com/user/ChucksFeedAndSeed/) : ChucksFeedAndSeed
- FPS - UI Blackscreen Fix : by MarethyuX
- SweetMini 1008p and 1080p Resolution : SweetMini, contribution by Socats and Darktalon
- [1080p Resolution](https://www.reddit.com/user/ChucksFeedAndSeed/comments/13sofgg/) : ChucksFeedAndSeed
- [Graphic patches](https://www.reddit.com/user/ChucksFeedAndSeed/comments/13sofgg/) : Authors are "ChucksFeedAndSeed, patchanon and somerandompeople", theses patches are split from the VisualFixes, FSR Disabler is from patchanon
- [Aspect Ratio](https://github.com/Fruithapje21/TOTK-Ultrawide) : From Fruithapje21 and Fayaz
- [Graphics - Anisotropic filtering fix](https://github.com/Wollnashorn/switch-mods/tree/master/0100F2C0115B6000) : @Wollnashorn
- [FPS - Cutscene-fix](https://github.com/theboy181/switch-ptchtxt-mods/tree/main/The%20Legend%20of%20Zelda%3A%20Tears%20of%20the%20Kingdom) : theboy181
- [Graphics - Disable Targeting DOF](https://github.com/theboy181/switch-ptchtxt-mods/tree/main/The%20Legend%20of%20Zelda%3A%20Tears%20of%20the%20Kingdom) : theboy181
- [Graphics - LOD Improvement](https://github.com/theboy181/switch-ptchtxt-mods/tree/main/The%20Legend%20of%20Zelda%3A%20Tears%20of%20the%20Kingdom) : theboy181
- [Graphics - Remove Lens Flare](https://github.com/theboy181/switch-ptchtxt-mods/tree/main/The%20Legend%20of%20Zelda%3A%20Tears%20of%20the%20Kingdom) : theboy181
  - Ports to 1.1.1/1.1.2 by Sweetmini
- [Graphics - Sky Island Fix for XX Resolution](https://www.reddit.com/user/PixelKiri/comments/14u57mr/) : PixelKiri
- Graphics - First Person + (Narrow/Wide FOV XX) : [MaxLastBreath](https://www.reddit.com/user/Maxlastbreath)
- [Cheat - 1.1.1 & 1.1.2 Cheats](https://github.com/bad1dea/NXCheats/tree/main/The%20Legend%20of%20Zelda%20Tears%20of%20the%20Kingdom) : By bad1dea
- [Cheat - 1.1.0 & 1.1.1 Cheats](https://gbatemp.net/threads/the-legend-of-zelda-tears-of-the-kingdom-nintendo-switch-cheats.632193/)
- Cheat - Durability (10x) : SweetMini
- Cheat - Time of day : FrostedMint
  </br>Unknown compatibily with FPS and Dynamic FPS mods, testing is required, open an issue to report the result if you tried.
- Graphics - Disable Internal FXAA v2 : SweetMini
- Graphics - Vertical Sensitivity Fix: igoticecream
- Resolution - 1026p : Zeikken
- Thanks to MaxLastBreath for providing us with ports to 1.0.0 of Island Fix, LOD Improvements, Lens Flare Removal, 1080p & 1008p resolution patches, and FPV+ mods!
- Thanks to StevenssND for provinding us with ports to 1.2.0 of Disable FSR downscaling, Resolution 1080p, Resolution 1008p, Disable LOD Quality Reduction, Shadows 256/512/1024x, LOD Improvement v2, Island Fix, Removes the DOF effect when targeting, Lensflare Removal, Disable FXAA, 20/30/60fps Static, Increased Camera Speed and Anisotropic Filtering Fix.
- Thanks to Father Of Egg for providing us with several game version ports of Infinite Rupees, Show All Korok Seed Locations, Swimming Speed 2x and 3x.
- Thanks to Pixelkiri / @alexkiri for the improved sky island fixes! The timing might have been unfortunate, but we recognise your efforts nonetheless!
