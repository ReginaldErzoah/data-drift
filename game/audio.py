import pygame
import os


class AudioEngine:

    def __init__(self):

        self.enabled = False
        self.volume = 0.25

       
        self.ambient_volume = 0.25

        self.sounds = {}
        self.ambient_channel = None

        # =========================
        # SAFE MIXER INIT
        # =========================
        try:
            pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
            self.enabled = True
        except Exception as e:
            print("[AudioEngine] Mixer init failed:", e)
            self.enabled = False
            return

        self.load_sounds()
        self.set_volume(self.volume)


    # =========================
    # LOAD SOUNDS
    # =========================
    def load_sounds(self):

        def safe_load(name, path):
            try:
                if os.path.exists(path):
                    self.sounds[name] = pygame.mixer.Sound(path)
                else:
                    self.sounds[name] = None
                    print(f"[AudioEngine] Missing file: {path}")
            except Exception as e:
                print(f"[AudioEngine] Failed loading {name}: {e}")
                self.sounds[name] = None

        base = "assets/sounds/"

        safe_load("hit", base + "hit.wav")
        safe_load("game_over", base + "game_over.wav")
        safe_load("ui_click", base + "ui_click.wav")
        safe_load("ambient", base + "ambient.wav")


    # =========================
    # VOLUME CONTROL
    # =========================
    def set_volume(self, volume):

        self.volume = volume

        for name, sound in self.sounds.items():

            if sound:

                # ambient is intentionally quieter
                if name == "ambient":
                    sound.set_volume(volume * self.ambient_volume)
                else:
                    sound.set_volume(volume)


    # =========================
    # SAFE PLAY
    # =========================
    def play(self, name):

        if not self.enabled:
            return

        sound = self.sounds.get(name)

        if sound:
            try:
                sound.play()
            except Exception as e:
                print(f"[AudioEngine] Play error ({name}):", e)


    # =========================
    # GAME EVENT WRAPPERS
    # =========================
    def play_hit(self):
        self.play("hit")

    def play_game_over(self):
        self.play("game_over")

    def play_ui(self):
        self.play("ui_click")


    # =========================
    # AMBIENT LOOP
    # =========================
    def start_ambient(self):

        if not self.enabled:
            return

        sound = self.sounds.get("ambient")

        if sound:
            try:
                # avoid stacking loops
                if self.ambient_channel is None or not self.ambient_channel.get_busy():
                    self.ambient_channel = sound.play(-1)

                    # enforce low volume even after playback starts
                    if self.ambient_channel:
                        self.ambient_channel.set_volume(
                            self.volume * self.ambient_volume
                        )

            except Exception as e:
                print("[AudioEngine] Ambient error:", e)


    # =========================
    # STOP ALL SOUND
    # =========================
    def stop_all(self):

        if self.enabled:
            try:
                pygame.mixer.stop()
            except Exception:
                pass

        self.ambient_channel = None


    # =========================
    # RESET (SAFE FOR RESTART)
    # =========================
    def reset(self):

        self.stop_all()