import pygame.display


class Settings:
	"""Класс для хранения всех настроек игры Alien Invasion."""

	def __init__(self):
		"""Инициализирует настройки игры."""
		# Параметры экрана
		infoObject = pygame.display.Info()  # Возвращает параметры дисплея
		self.screen_width = infoObject.current_w
		self.screen_height = infoObject.current_h

		# Основной цвет всех надписей
		self.bg_color = (255, 255, 255)

		# Задний фон
		self.bg_image = pygame.image.load('images/bg_image.jpg')
		self.bg_image = pygame.transform.scale(self.bg_image, (self.screen_width, self.screen_height))

		# Настройки корабля
		self.ship_speed_factor = 1.5
		self.ship_limit = 3
		# Параметры пули
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15

		# Цвет пули
		self.bullet_color = 0, 255, 127

		self.bullets_allowed = 3

		# Настройки пришельцев
		self.alien_speed_factor = 1
		# Величина снижения по вертикали при достижении края экрана
		self.fleet_drop_speed = 10
		# fleet_direction = 1 - движение вправо, -1 - движение влево
		self.fleet_direction = 1

		# Темп ускорения игры
		self.speedup_scale = 1.1
		# Темп роста стоимости пришельцев
		self.score_scale = 1.5
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Инициализирует настройки, изменяющиеся в ходе игры."""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		# fleet_direction = 1 - движение вправо, -1 - движение влево.
		self.fleet_direction = 1

		# Подсчет очков
		self.alien_points = 50

	def increase_speed(self):
		"""Увеличивает настройки скорости."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)

