import os
import sys
import glfw
import OpenGL.GL as gl
import imgui
from imgui.integrations.glfw import GlfwRenderer
import webbrowser
import time
import pyperclip
import pystyle
from pystyle import Colors, Colorate

# solo per test
if os.getenv("XDG_SESSION_TYPE") == "wayland":
    os.environ["XDG_SESSION_TYPE"] = "x11"


active = {
    "Tools": False,
    "Changelog": False,
    "Comandi": False,
    "AutoScanner": False,
    "MacroCheck": False
}

# SolarSS made by Creeper215.
                                                               
os.system('cls')
print(Colorate.Horizontal(Colors.yellow_to_green, "SolarSS 0.8 | by Creeper215\n"))
time.sleep(2)

opened_state = True

path_to_font = None

def frame_commands():
    gl.glClearColor(0.1, 0.1, 0.1, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    io = imgui.get_io()

    if io.key_ctrl and io.keys_down[glfw.KEY_Q]:
        sys.exit(0)


    if imgui.begin_main_menu_bar():
        if imgui.begin_menu("Opzioni", True):
            clicked_quit, selected_quit = imgui.menu_item("Esci", "Ctrl+Q", False, True)

            if clicked_quit:
                sys.exit(0)
        

            imgui.end_menu()
        imgui.end_main_menu_bar()

os.system('cls')

def render_frame(impl, window, font):
    glfw.poll_events()
    impl.process_inputs()
    imgui.new_frame()

    gl.glClearColor(0.1, 0.1, 0.1, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    if font is not None:
        imgui.push_font(font)
    frame_commands()
    if font is not None:
        imgui.pop_font()

    imgui.begin("Menu")
    for label, enabled in active.copy().items():
        _, enabled = imgui.checkbox(label, enabled)
        active[label] = enabled
    imgui.end()

    if active["Changelog"]:
        imgui.begin("Changelog - v0.8")
        imgui.text("""SolarSS 0.8
                   
[+] Fixata la conversione .exe""")
        imgui.end()

    if active["Tools"]:
        imgui.begin("Seleziona Tool")
        if imgui.button("Selezione Tool"):
            imgui.open_popup("Scegli Tool")
        imgui.same_line()
        if imgui.begin_popup_modal("Scegli Tool")[0]:
            imgui.text("Scegli:")
            imgui.separator()
            clicked_everything, selected_everything = imgui.selectable("Everything (Cerca)")
            clicked_hacker, selected_hacker = imgui.selectable("System Informer (Fork Process Hacker)")
            clicked_pf, selected_pf = imgui.selectable("WinPrefetchView")
            clicked_liveinfo, selected_liveinfo = imgui.selectable("Win10LiveInfo (Easy BAM)")
            if clicked_everything:
                os.system("curl -o EverythingInstaller.exe https://www.voidtools.com/Everything-1.4.1.1024.x86-Setup.exe")
                os.system("EverythingInstaller.exe")
                os.system("cls")
                os.system("del EverythingInstaller.exe")
            if clicked_hacker:
                siurl = "https://github.com/winsiderss/si-builds/releases/download/3.0.7422/systeminformer-3.0.7422-setup.exe"
                webbrowser.open(siurl, new=0, autoraise=True)
            if clicked_pf:
                os.system("curl -o WPFVx64.zip https://www.nirsoft.net/utils/winprefetchview-x64.zip")
                os.system("WPFVx64.zip")
                os.system("cls")
            if clicked_liveinfo:
                liveinfourl = "https://github.com/kacos2000/Win10LiveInfo/releases/download/v.1.0.23.0/WinLiveInfo.exe"
                webbrowser.open(liveinfourl, new=0, autoraise=True)
            imgui.end_popup()
        imgui.end()
    if active["Comandi"]:
        imgui.begin("Seleziona Comando")
        if imgui.button("Selezione Comando"):
            imgui.open_popup("Scegli Comando")
        imgui.same_line()
        if imgui.begin_popup_modal("Scegli Comando")[0]:
            imgui.text("Scegli:")
            imgui.separator()
            clicked_jn1, selected_jn1 = imgui.selectable("Journal (Eliminazione File)")
            clicked_jn2, selected_jn2 = imgui.selectable("Journal (jnativehook.dll)")
            clicked_jn3, selected_jn3 = imgui.selectable("Journal (Modifica File)")
            clicked_jn4, selected_jn4 = imgui.selectable("Journal (Replace)")
            clicked_jn5, selected_jn5 = imgui.selectable("Journal (Log Eliminati)")
            clicked_tree1, selected_tree1 = imgui.selectable("Tree/f (Programmi nel PC)")
            clicked_sysmain, selected_sysmain = imgui.selectable("Sysmain Query (Stato Prefetch)")
            clicked_pcasvc, selected_pcasvc = imgui.selectable("Pcasvc Query (Stato Pcaclient)")
            clicked_pwsh1, selected_pwsh1 = imgui.selectable("ChildItem .EXE PWSH")
            clicked_pwsh2, selected_pwsh2 = imgui.selectable("ChildItem .DLL PWSH")
            clicked_pwsh3, selected_pwsh3 = imgui.selectable("ChildItem .JAR PWSH")
            clicked_pwsh4, selected_pwsh4 = imgui.selectable("ChildItem .RAR PWSH")

            if clicked_jn1:
                pyperclip.copy('fsutil usn readjournal c: | findstr /i /C:"Eliminazione" > eliminati1.txt')
                print(Colorate.Horizontal(Colors.yellow_to_green, "Copiato nella clipboard!"))
            if clicked_jn2:
                pyperclip.copy('fsutil usn readjournal c: csv | findstr /i /R /C:JNativeHook-[0-9] /i /C:0x80000200 /i /C:regsvr32 /i /C:java | findstr /i /C:%date% | findstr /i /C:.exe\^" /i /C:.pf\^" /i /C:.com\^" /i /C:.cmd\^" /i /C:.pif\^" /i /C:.bat\^" /i /C:.dll\^" /i /C:"?" > %userprofile%\desktop\journal.txt')
                print(Colorate.Horizontal(Colors.yellow_to_green, "Copiato nella clipboard!"))
            if clicked_jn3:
                pyperclip.copy('fsutil usn readjournal c: | findstr /i "Modifica sicurezza" > prova123.txt')
                print(Colorate.Horizontal(Colors.yellow_to_green, "Copiato nella clipboard!"))
            if clicked_jn4:
                pyperclip.copy('fsutil usn readjournal c: csv | findstr /i /C:"0x00002000" > Replace 1.txt')
                print(Colorate.Horizontal(Colors.yellow_to_green, "Copiato nella clipboard!"))
            if clicked_jn5:
                pyperclip.copy('fsutil usn readjournal C: csv | findstr /i /C:"0x00000000" | findstr /i /C:"0x00000020" | findstr /i /C:.log\^" > a.txt')
                print(Colorate.Horizontal(Colors.yellow_to_green, "Copiato nella clipboard!"))
            if clicked_tree1:
                pyperclip.copy('Tree/f')
                print(Colorate.Horizontal(Colors.yellow_to_green, "Copiato nella clipboard!"))
            if clicked_sysmain:
                os.system("sc query sysmain")
                print(Colorate.Horizontal(Colors.yellow_to_green, "Fatto!"))
            if clicked_pcasvc:
                os.system("sc query pcasvc")
                print(Colorate.Horizontal(Colors.yellow_to_green, "Fatto!"))
            if clicked_pwsh1:
                pyperclip.copy('Get-ChildItem -recurse *.exe*')
                print(Colorate.Horizontal(Colors.yellow_to_green, "Copiato nella clipboard!"))
            if clicked_pwsh2:
                pyperclip.copy('Get-ChildItem -recurse *.dll*')
                print(Colorate.Horizontal(Colors.yellow_to_green, "Copiato nella clipboard!"))
            if clicked_pwsh3:
                pyperclip.copy('Get-ChildItem -recurse *.jar*')
                print(Colorate.Horizontal(Colors.yellow_to_green, "Copiato nella clipboard!"))
            if clicked_pwsh4:
                pyperclip.copy('Get-ChildItem -recurse *.rar*')
                print(Colorate.Horizontal(Colors.yellow_to_green, "Copiato nella clipboard!"))
            
            imgui.end_popup()
        imgui.end()
    if active["AutoScanner"]:
        imgui.begin("Seleziona Scanner")
        if imgui.button("Selezione Scanner"):
            imgui.open_popup("Scegli Scanner")
        imgui.same_line()
        if imgui.begin_popup_modal("Scegli Scanner")[0]:
            imgui.text("Scegli:")
            imgui.separator()
            clicked_echopaid, selected_echopaid = imgui.selectable("Echo Paid")
            clicked_echofree, selected_echofree = imgui.selectable("Echo Free")
            clicked_oceanss, selected_oceanss = imgui.selectable("OceanSS")
            clicked_avenge, selected_avenge = imgui.selectable("AvengeAC")
            if clicked_echofree:
                echofff = "dl.echo.ac/free"
                webbrowser.open(echofff, new=0, autoraise=True)
            if clicked_oceanss:
                oceanss = "anticheat.ac"
                webbrowser.open(oceanss, new=0, autoraise=True)
            if clicked_avenge:
                avengeac = "dl.avenge.ac"
                webbrowser.open(avengeac, new=0, autoraise=True)
            if clicked_echopaid:
                echopaidd = "dl.echo.ac"
                webbrowser.open(echopaidd, new=0, autoraise=True)
            imgui.end_popup()
        imgui.end()
    if active["MacroCheck"]:
        imgui.begin("Seleziona Software Mouse")
        if imgui.button("Selezione Software Mouse"):
            imgui.open_popup("Scegli Software Mouse")
        imgui.same_line()
        if imgui.begin_popup_modal("Scegli Software Mouse")[0]:
            imgui.text("Scegli:")
            imgui.separator()
            clicked_lghub, selected_lghub = imgui.selectable("Logitech G-Hub")
            clicked_rzsnyp, selected_rzsnyp = imgui.selectable("Razer Synapse")
            clicked_trust, selected_trust = imgui.selectable("Trust Mouse Software")
            clicked_oliva, selected_olive = imgui.selectable("Quilive Mouse Software")
            clicked_reddragon, selected_reddragon = imgui.selectable("Reddragon Mouse")
            
            if clicked_lghub:
                os.system("explorer %userprofile%\AppData\Local\LGHUB")
            if clicked_rzsnyp:
                os.system("explorer C:\ProgramData\Razer\GameManager\Logs")
            if clicked_trust:
                os.system('explorer "C:\Program Files (x86)\Trust GXT 155 Gaming Mouse"')
            if clicked_oliva:
                os.system('explorer "C:\Program Files (x86)\Qilive Gaming Mouse"')
            if clicked_reddragon:
                os.system('explorer "%userprofile%\Documents\M711 Gaming Mouse\MacroDB"')
            
            imgui.end_popup()
        imgui.end()

    imgui.render()
    impl.render(imgui.get_draw_data())
    glfw.swap_buffers(window)




def impl_glfw_init():
    width, height = 650, 650
    window_name = "SolarSS"

    if not glfw.init():
        print("Impossibile inizializzare il contesto OpenGL")
        sys.exit(1)

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    window = glfw.create_window(int(width), int(height), window_name, None, None)
    glfw.make_context_current(window)

    if not window:
        glfw.terminate()
        print("Impossibile inizializzare finestra!")
        sys.exit(1)

    return window


def main():
    imgui.create_context()
    window = impl_glfw_init()

    impl = GlfwRenderer(window)

    io = imgui.get_io()
    jb = io.fonts.add_font_from_file_ttf(path_to_font, 30) if path_to_font is not None else None
    impl.refresh_font_texture()

    while not glfw.window_should_close(window):
        render_frame(impl, window, jb)

    impl.shutdown()
    glfw.terminate()


if __name__ == "__main__":
    main()
