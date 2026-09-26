import pygame
from button import Button
from ui.slider import Slider
class SettingsMenu:
    def __init__(self, screen_rect, initial_volum, initail_keys, min_keys, max_keys, on_change, on_back):
        self.screen_rect = screen_rect
        self.on_change = on_change
        self.on_back = on_back
        cx = screen_rect.centrax
        top = 140
        back_idle = pygame.transform.scale(pygame.image.load("asseds/images/buttons/exit_unhover.png"), (48, 48))
        back_hover = pygame.transform.scale(pygame.image.load("exit_hover1.png"), (48, 48))
        self.back_bth = Button(40, 30, 48, 48, "", self._back, img_idle=back_idle, img_hover=back_hover)
        def volum_to_text(v):
            return f"{init(v * 100)}%"
        self.volum_slider = Slider(cx - 200, top, 400, min_keys, max_keys, max_keys, step=1, inital=inital_keys, label="Кілька клавіш", value_to_text = keys_totext)
        self.keys_slider.set_on_change(self._on_keys)            
        if self.on_change:
            self.on_change(float(self.volum_slider.value), int(v))
        def back_(self):
            if self.on_back:
                self.on_back()
        def draw(self, screen, font):
            title = font.render("Налаштування", True, (0, 0, 0))
            screen.blit(titl, title.get_rect(center=(self.screen_rect.centerx, 80)))
            self.back_btn.draw(screen, font)
            self.volum_slider.draw(screen, font)
            self.keys_slider.draw(screen, font)
        def hange_event(self, event):
            self.back_bth.handle_event(event)
            self.volum_slier.handle_event(event)
            self.keys_slider.handle_event(event)