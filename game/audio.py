import pygame
import os


class AudioEngine:

    def __init__(self):

        # initialize mixer safely
        try:
            pygame.mixer.init()
        except:
            print("Audio system not available")
            self.enabled = False
            return

        self.enabled = True

        # =========================
        # SOUND STORAGE
        # =========================
        self.sounds = {}

        self.load_sounds()

        # global volume tuning
        self.set_volume(0.5)


    # =========================
    # LOAD ALL SOUNDS
    # =========================
    def load_sounds(self):

        def safe_load(name, path):
            if os.path.exists(path):
                self.sounds[name] = pygame.mixer.Sound(path)
            else:
                self.sounds[name] = None

        # core gameplay sounds (you can add files later)
        safe_load("hit", "assets/audio/hit.wav")
        safe_load("combo", "assets/audio/combo.wav")
        safe_load("move", "assets/audio/move.wav")
        safe_load("game_over", "assets/audio/game_over.wav")
        safe_load("bg", "assets/audio/ambient.wav")


    # =========================
    # VOLUME CONTROL
    # =========================
    def set_volume(self, volume):

        self.volume = volume

        for sound in self.sounds.values():
            if sound:
                sound.set_volume(volume)


    # =========================
    # PLAY SAFE SOUND
    # =========================
    def play(self, name):

        if not self.enabled:
            return

        sound = self.sounds.get(name)

        if sound:
            sound.play()


    # =========================
    # GAME EVENTS
    # =========================
    def play_hit(self):
        self.play("hit")

    def play_combo(self):
        self.play("combo")

    def play_move(self):
        self.play("move")

    def play_game_over(self):
        self.play("game_over")


    # =========================
    # AMBIENT LOOP (OPTIONAL)
    # =========================
    def start_ambient(self):

        if not self.enabled:
            return

        sound = self.sounds.get("bg")

        if sound:
            sound.play(-1)  # loop forever