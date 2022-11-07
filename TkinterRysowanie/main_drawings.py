import platform

# information about which platforms support this application
info_supported_os = "This program does not support platforms other than Windows 7 or 10"

if __name__ == "__main__":
    os_system = platform.system()
    os_release = platform.release()
    if os_system.lower() != "windows":
        print(info_supported_os)
        exit()
    else:
        if os_release == "7":
            import win_7_drawings as drawings
        elif os_release == "10":
            import win_10_drawings as drawings
        else:
            print(info_supported_os)
            exit()
    application = drawings.Drawings()
    application.mainloop()
