import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
import sys
import webbrowser
#import psutil
#import gpuinfo
#import pyglet
#import wmi

def get_yuzu_folder():
    if os.name == 'nt':  # Check if the operating system is Windows
        roaming_folder_path = os.getenv('APPDATA')
        yuzu_folder_path = os.path.join(roaming_folder_path, 'yuzu')
        if os.path.exists(yuzu_folder_path):
            return yuzu_folder_path
    else:  # Assume Linux
        home_folder = os.path.expanduser("~")
        yuzu_folder_path = os.path.join(home_folder, '.local', 'share', 'yuzu')
        if os.path.exists(yuzu_folder_path):
            return yuzu_folder_path

    return None

def open_folder_dialog():
    folder_path = filedialog.askdirectory(title="Select Yuzu Roaming/User Folder (Typically C:/Users/<Your Username>/AppData/Roaming/yuzu/) unless you use portable yuzu")
    if folder_path:
        yuzu_folder_path.set(folder_path)
        yuzu_folder_label.config(fg="green")
        yuzu_folder_entry.delete(0, tk.END)
        yuzu_folder_entry.insert(0, folder_path)  # Insert the path in the entry widget
        yuzu_folder_button.config(fg="green")
        update_folder_state_label()
    else:
        yuzu_folder_path.set("")
        yuzu_folder_label.config(fg="red")
        yuzu_folder_entry.delete(0, tk.END)
        yuzu_folder_button.config(fg="red")
        update_folder_state_label()



def copy_blackscreen_fix(romfs_folder):
    blackscreen_fix_option = blackscreen_var.get()

    if blackscreen_fix_option == 'Add Black-screen fix (Nintendo UI)':
        blackscreen_fix_folder = os.path.join(script_directory, 'data', 'blackscreenfix', 'UI')
        shutil.copytree(blackscreen_fix_folder, os.path.join(romfs_folder, 'UI'))
    elif blackscreen_fix_option == 'Add Black-screen fix (Playstation UI)':
        playstation_fix_folder = os.path.join(script_directory, 'data', 'Playstation UI Mod v12.2 - Normal - White', 'romfs', 'UI')
        shutil.copytree(playstation_fix_folder, os.path.join(romfs_folder, 'UI'))
        playstation_font_folder = os.path.join(script_directory, 'data', 'Playstation UI Mod v12.2 - Normal - White', 'romfs', 'Font')
        shutil.copytree(playstation_font_folder, os.path.join(romfs_folder, 'Font'))
    elif blackscreen_fix_option == 'Add Black-screen fix (Xbox UI)':
        xbox_fix_folder = os.path.join(script_directory, 'data', 'Xbox UI Mod v9 - Normal - White', 'romfs', 'UI')
        shutil.copytree(xbox_fix_folder, os.path.join(romfs_folder, 'UI'))
        xbox_font_folder = os.path.join(script_directory, 'data', 'Xbox UI Mod v9 - Normal - White', 'romfs', 'Font')
        shutil.copytree(xbox_font_folder, os.path.join(romfs_folder, 'Font'))
    elif blackscreen_fix_option == 'Remove Black-screen fix (UI Compatible)':
        romfs_ui_folder = os.path.join(romfs_folder, 'UI')
        shutil.rmtree(romfs_ui_folder, ignore_errors=True)
        romfs_font_folder = os.path.join(romfs_folder, 'Font')
        shutil.rmtree(romfs_font_folder, ignore_errors=True)



#def get_gpu_info():
#    c = wmi.WMI(namespace="root\\CIMV2")
#
#    gpu_info = []
#
#    for item in c.Win32_VideoController():
#        gpu_info.append({
#            'Name': item.Name,
#            'AdapterRAM': item.AdapterRAM,
#            'AdapterCompatibility': item.AdapterCompatibility
#        })

#    return gpu_info

#def bytes_to_gb(bytes_value):
#    bytes_value = int(bytes_value)
#    if bytes_value < 0:
#        bytes_value *= -1
#    if isinstance(bytes_value, str):
#       bytes_value = float(bytes_value)
#    return round(bytes_value / 1024**3 if bytes_value >= 1024**3 else bytes_value / 102400, 2)

# Get GPU information
#gpu_info = get_gpu_info()

# Print GPU information
#for gpu in gpu_info:
#    print("Name:", gpu['Name'])
#    print("Adapter RAM:", bytes_to_gb(gpu['AdapterRAM']), "GB")
#    print("Adapter Compatibility:", gpu['AdapterCompatibility'])
#    print()

# Get system RAM capacity
#system_ram_capacity = wmi.WMI().Win32_ComputerSystem()[0].TotalPhysicalMemory
#print("RAM Capacity:", bytes_to_gb(system_ram_capacity), "GB")


# Mapping of resolutions to shadow resolutions

resolution_shadow_mapping = {
    '960x540': 512,
    '1280x720': 512,
    '1366x768': 512,
    '1600x900': 1024,
    '1920x1080': 1024,
    '2560x1440': 2048,
    '3840x2160': 4096,
    '5120x2880': 4096,
    '5760x3240': 4096,
    '7680x4320': 4096
}

def generate_config():
    resolution = resolution_var.get().split(' (')[0]
    framerate = framerate_var.get().split(' ')[0]
    blackscreen_fix = blackscreen_var.get()

    yuzu_folder_path_value = yuzu_folder_path.get()

    if not yuzu_folder_path_value:
        appdata_path = get_yuzu_folder()
        if appdata_path:
            yuzu_folder_path.set(appdata_path)
            yuzu_folder_label.config(fg="green")
            yuzu_folder_entry.delete(0, tk.END)
            yuzu_folder_entry.insert(0, appdata_path)
            yuzu_folder_button.config(fg="green")
            yuzu_folder_path_value = appdata_path
        else:
            messagebox.showinfo("Yuzu Folder", "Yuzu folder not selected. Please select it manually.")
            yuzu_folder_label.config(fg="red")
            return

    source_folder = os.path.join(script_directory, 'data', 'source')
    result_folder = os.path.join(os.getcwd(), 'result')

    if os.path.exists(result_folder):
        confirm = messagebox.askyesno("Confirmation", "The 'result' folder already exists. Do you want to delete it and continue?")
        if confirm:
            shutil.rmtree(result_folder)
        else:
            return

    shutil.copytree(source_folder, result_folder)

    romfs_folder = os.path.join(result_folder, 'romfs')
    dfps_folder = os.path.join(romfs_folder, 'dfps')
    os.makedirs(dfps_folder, exist_ok=True)

    resolution_ini_path = os.path.join(dfps_folder, 'resolution.ini')
    with open(resolution_ini_path, 'w') as f:
        f.write('[Graphics]\n')
        f.write('ResolutionWidth = {}\n'.format(resolution.split('x')[0]))
        f.write('ResolutionHeight = {}\n'.format(resolution.split('x')[1]))

        # Check if the chosen resolution is in the mapping, and set the appropriate shadow resolution
        shadow_resolution = resolution_shadow_mapping.get(resolution, -1)
        if shadow_resolution != -1:
            f.write('ResolutionShadows = {}\n'.format(shadow_resolution))
        else:
            f.write('ResolutionShadows = -1\n')


    

    framerate_ini_path = os.path.join(dfps_folder, 'framerate.ini')
    with open(framerate_ini_path, 'w') as f:
        f.write('[dFPS]\n')
        f.write('MaxFramerate = {}\n'.format(framerate))
        f.write('EnableCameraQualityImprovement = false\n')

    copy_blackscreen_fix(romfs_folder)

    config_folder_paths = [
        os.path.join(yuzu_folder_path_value, 'config', 'custom'),
    ]

    # Create the base 0100F2C0115B6000.ini content with the specified settings
    config_content = f"""[Controls]
vibration_enabled\\use_global=true
enable_accurate_vibrations\\use_global=true
motion_enabled\\use_global=true

[Core]
use_multi_core\\use_global=true
memory_layout_mode\\use_global=false
speed_limit\\use_global=true
memory_layout_mode\\default=true
memory_layout_mode=0

[Cpu]
cpu_accuracy\\use_global=false
cpuopt_unsafe_unfuse_fma\\use_global=true
cpuopt_unsafe_reduce_fp_error\\use_global=true
cpuopt_unsafe_ignore_standard_fpcr\\use_global=true
cpuopt_unsafe_inaccurate_nan\\use_global=true
cpuopt_unsafe_fastmem_check\\use_global=true
cpuopt_unsafe_ignore_global_monitor\\use_global=true
cpu_accuracy\\default=true
cpu_accuracy=0

[Renderer]
backend\\use_global=false
shader_backend\\use_global=true
vulkan_device\\use_global=false
use_disk_shader_cache\\use_global=false
use_asynchronous_gpu_emulation\\use_global=false
accelerate_astc\\use_global=true
nvdec_emulation\\use_global=true
fullscreen_mode\\use_global=true
aspect_ratio\\use_global=true
resolution_setup\\use_global=false
scaling_filter\\use_global=true
anti_aliasing\\use_global=true
fsr_sharpening_slider\\use_global=false
bg_red\\use_global=true
bg_green\\use_global=true
bg_blue\\use_global=true
gpu_accuracy\\use_global=false
max_anisotropy\\use_global=false
astc_recompression\\use_global=true
async_presentation\\use_global=false
force_max_clock\\use_global=true
use_reactive_flushing\\use_global=false
use_asynchronous_shaders\\use_global=false
use_fast_gpu_time\\use_global=false
use_vulkan_driver_pipeline_cache\\use_global=false
enable_compute_pipelines\\use_global=true
use_video_framerate\\use_global=false
barrier_feedback_loops\\use_global=false
backend\\default=true
backend=1
vulkan_device\\default=true
vulkan_device=0
use_disk_shader_cache\\default=true
use_disk_shader_cache=true
use_asynchronous_gpu_emulation\\default=true
use_asynchronous_gpu_emulation=true
resolution_setup\\default=true
resolution_setup=2
fsr_sharpening_slider\\default=false
fsr_sharpening_slider=200
gpu_accuracy\\default=false
gpu_accuracy=0
max_anisotropy\\default=false
max_anisotropy=5
async_presentation\\default=true
async_presentation=false
use_reactive_flushing\\default=true
use_reactive_flushing=true
use_asynchronous_shaders\\default=true
use_asynchronous_shaders=false
use_fast_gpu_time\\default=true
use_fast_gpu_time=true
use_vulkan_driver_pipeline_cache\\default=true
use_vulkan_driver_pipeline_cache=true
use_video_framerate\\default=false
use_video_framerate=true
barrier_feedback_loops\\default=true
barrier_feedback_loops=true

[Audio]
volume\\use_global=true

[System]
language_index\\use_global=true
region_index\\use_global=true
time_zone_index\\use_global=true
custom_rtc_enabled\\use_global=true
custom_rtc\\use_global=true
rng_seed_enabled\\use_global=true
rng_seed\\use_global=true
use_docked_mode\\use_global=true
sound_index\\use_global=true
"""


    # Save the additional config content to 0100F2C0115B6000.ini
    config_file_path = os.path.join(yuzu_folder_path_value, 'config', 'custom', '0100F2C0115B6000.ini')

    with open(config_file_path, 'w') as f:
        f.write(config_content)

    for config_folder_path in config_folder_paths:
        ini_file_path = os.path.join(config_folder_path, '0100F2C0115B6000.ini')

        if os.path.exists(ini_file_path):
            with open(ini_file_path, 'r') as f:
                lines = f.readlines()

            with open(ini_file_path, 'w') as f:
                for line in lines:
                    if line.startswith(r'memory_layout_mode\use_global='):
                        f.write('memory_layout_mode\\use_global=false\n')
                    elif line.startswith(r'memory_layout_mode\default='):
                        if resolution in ['960x540', '1280x720', '1366x768', '1600x900', '1920x1080']:
                            f.write('memory_layout_mode\\default=true\n')
                        else:
                            f.write('memory_layout_mode\\default=false\n')
                    elif line.startswith(r'memory_layout_mode='):
                        if resolution in ['960x540', '1280x720', '1366x768', '1600x900', '1920x1080']:
                            f.write('memory_layout_mode=0\n')
                        else:
                            f.write('memory_layout_mode=2\n')
                    elif line.startswith(r'resolution_setup\use_global='):
                        f.write('resolution_setup\\use_global=false\n')
                    elif line.startswith(r'resolution_setup\default='):
                        f.write('resolution_setup\\default=true\n')
                    elif line.startswith(r'resolution_setup='):
                        f.write('resolution_setup=2\n')
                    else:
                        f.write(line)



    folder_name = f"Custom Lazy Pack - {resolution} - {framerate} FPS - {blackscreen_fix}"
    lazy_pack_folder = os.path.join(yuzu_folder_path_value, 'load', '0100F2C0115B6000', folder_name)
    shutil.rmtree(lazy_pack_folder, ignore_errors=True)
    shutil.copytree(result_folder, lazy_pack_folder)

    update_folder_state_label()

    # Clean up the result folder
    shutil.rmtree(result_folder)

    messagebox.showinfo("Success", "Lazy Pack generated successfully.")

def open_github_project():
    webbrowser.open("https://github.com/HolographicWings/TOTK-Mods-collection")

# Create the main window
window = tk.Tk()
window.title("Lazy Pack Generator by TOTK-Mods-Collection crew")
window.geometry("480x480")
window.resizable(False, False)

# Add padding to the top and left side
window['padx'] = 10
window['pady'] = 10

# Get the directory path of the script file
script_directory = Path(__file__).resolve().parent

# Set the background image path
background_image_path = script_directory / 'data' / 'background' / 'background.gif'

# Create the background label
background_image = tk.PhotoImage(file=background_image_path)
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create the dropdown menus
resolutions = ['960x540 (qHD)', '1280x720 (HD)', '1366x768 (HD)', '1600x900 (HD+)', '1920x1080 (FHD)', '2560x1440 (QHD)', '3840x2160 (4K)', '5120x2880 (QQHD)', '5760x3240 (3xFHD)', '7680x4320 (8K)']
framerates = ['20 FPS', '30 FPS', '35 FPS', '36 FPS', '40 FPS', '45 FPS', '60 FPS', '72 FPS', '75 FPS', '80 FPS', '90 FPS', '120 FPS']
blackscreen_options = ['Add Black-screen fix (Nintendo UI)', 'Add Black-screen fix (Playstation UI)', 'Add Black-screen fix (Xbox UI)', 'Remove Black-screen fix (UI Compatible)']

# Create custom style for the OptionMenu and TCombobox
s = ttk.Style()
s.theme_create("custom_style", parent="alt", settings={
    "TCombobox": {
        "configure": {"selectbackground": "#4D4D4E", "fieldbackground": "#4D4D4E", "background": "#4D4D4E", "foreground": "white", "arrowcolor": "white"},
    },
    "TCombobox.Button": {
        "configure": {"background": "#4D4D4E", "foreground": "white", "bordercolor": "#4D4D4E", "lightcolor": "#4D4D4E", "darkcolor": "#4D4D4E"},
    },
    "TCombobox.Label": {
        "configure": {"background": "#4D4D4E", "foreground": "white"},
    },
})
s.theme_use("custom_style")

resolution_var = tk.StringVar(window)
resolution_var.set(resolutions[0])
resolution_label = tk.Label(window, text="Resolution:", fg="white", bg="#4D4D4E")
resolution_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
resolution_dropdown = ttk.Combobox(window, textvariable=resolution_var, values=resolutions, state="readonly", width=36)
resolution_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

framerate_var = tk.StringVar(window)
framerate_var.set(framerates[0])
framerate_label = tk.Label(window, text="Framerate:", fg="white", bg="#4D4D4E")
framerate_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
framerate_dropdown = ttk.Combobox(window, textvariable=framerate_var, values=framerates, state="readonly", width=36)
framerate_dropdown.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

blackscreen_var = tk.StringVar(window)
blackscreen_var.set(blackscreen_options[0])
blackscreen_label = tk.Label(window, text="Blackscreen Fix:", fg="white", bg="#4D4D4E")
blackscreen_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
blackscreen_dropdown = ttk.Combobox(window, textvariable=blackscreen_var, values=blackscreen_options, state="readonly", width=36)
blackscreen_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

# Create the 'Yuzu Folder' selection button
yuzu_folder_path = tk.StringVar(window)
yuzu_folder_label = tk.Label(window, text="Yuzu Folder:")
yuzu_folder_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
yuzu_folder_button = tk.Button(window, text="Select Folder", command=open_folder_dialog)
yuzu_folder_button.grid(row=3, column=2, padx=18, pady=5, sticky=tk.W)

# Autofill Yuzu folder path
appdata_path = get_yuzu_folder()
if appdata_path:
    yuzu_folder_path.set(appdata_path)
    yuzu_folder_label.config(fg="#FFEE00", bg="#4D4D4E")
    yuzu_folder_path_value = tk.StringVar(window, value=appdata_path)  # Define yuzu_folder_path_value
    yuzu_folder_entry = tk.Entry(window, textvariable=yuzu_folder_path_value, width=38, fg="white", bg="#4D4D4E")
    yuzu_folder_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
    yuzu_folder_button.config(fg="#FFEE00", cursor="hand2", bg="#4D4D4E")

# Create the 'Generate' button
generate_button = tk.Button(window, text="Generate!",fg="white", cursor="hand2", bg="#4D4D4E", command=generate_config)
generate_button.grid(row=5, column=0, columnspan=3, padx=5, pady=10, sticky="ew", rowspan=1)

def update_folder_state_label():
    folder_path = yuzu_folder_path.get()

    if not folder_path:
        folder_state_label.config(text="Warning: No folder selected!", fg="red")
        yuzu_folder_label.config(fg="red")
        yuzu_folder_button.config(fg="red")

    else:
        folder_state_label.config(text="Folder selected by user!", fg="#00FF00")
        yuzu_folder_label.config(fg="#00FF00")
        yuzu_folder_button.config(fg="#00FF00")

# Add the folder state label
folder_state_label = tk.Label(window, text="Warning: Folder path autofilled! \n Portable Yuzu / Linux users \n please check the directory selected \n and adjust it by clicking 'Select Folder' above", fg="#FFEE00", bg="#4D4D4E",)
folder_state_label.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

# Create the GitHub link label
github_link_label = tk.Button(window, text="Visit our website!", fg="cyan", cursor="hand2", bg="#4D4D4E")
github_link_label.grid(row=0, column=2, padx=10, pady=10, sticky=tk.E)
github_link_label.bind("<Button-1>", lambda e: open_github_project())

# Hide the command line window
window.iconify()
window.update_idletasks()
window.deiconify()

# Start the main event loop
window.mainloop()

# Compile using "pyinstaller --onefile --noconsole --add-data "data;data" lazy_pack.py"