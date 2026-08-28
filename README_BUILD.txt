MARIO GAME - APK BUILD PROJECT

This project keeps the game's main.py and game assets intact. Only Android packaging support was adjusted.

BUILD:
1. Upload this project to a GitHub repository.
2. Use the main branch.
3. Open GitHub -> Actions -> Build Mario Game APK.
4. Run the workflow with "Run workflow" if it is not triggered automatically.
5. Wait for the build to finish.
6. Open the completed workflow run and download the "MarioGame-APK" artifact.

The workflow uses Buildozer and includes ffpyplayer because the game uses Kivy VideoPlayer for MP4 files.
