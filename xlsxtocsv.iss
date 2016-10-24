; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "xlsxtocsv"
#define MyAppVersion "1.1"
#define MyAppPublisher "Harald von Waldow <harald.vonwaldow@eawag.ch>"
#define MyAppURL "https://github.com/eawag-rdm/xlsxtocsv"
#define MyAppExeName "MyProg.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{B1B42CF5-9F97-4818-9BDC-C6D92F994698}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
CreateAppDir=no
OutputBaseFilename=xlsxtocsv_setup
Compression=lzma
SolidCompression=yes
AlwaysRestart=yes
DisableWelcomePage=yes
DisableStartupPrompt=yes
PrivilegesRequired=lowest
UninstallFilesDir="{localappdata}/uninst"

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "C:\Users\vonwalha\xlsxtocsv.exe"; DestDir: "{localappdata}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKCU; Subkey: "Environment"; ValueType: expandsz; ValueName: PATH; ValueData: "{olddata};{localappdata}"; \
Check: NeedsAddPath('{localappdata}')

[Code]

function NeedsAddPath(Param: string): boolean;
var
  OrigPath: string;
begin
  if not RegQueryStringValue(HKEY_CURRENT_USER,
    'Environment',
    'PATH', OrigPath)
  then begin
    Result := True;
    exit;
  end;
  // look for the path with leading and trailing semicolon
  // Pos() returns 0 if not found
  Param := ExpandConstant(Param)
  Result := Pos(';' + Param + ';', ';' + OrigPath + ';') = 0;
end;