__author__ = 'marble_xu'

START_LEVEL_NUM = 1

ORIGINAL_CAPTION = 'Plant VS Zombies Game'

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

GRID_X_LEN = 9
GRID_Y_LEN = 5
GRID_X_SIZE = 80
GRID_Y_SIZE = 100


WHITE        = (255, 255, 255)
NAVYBLUE     = ( 60,  60, 100)
SKY_BLUE     = ( 39, 145, 251)
BLACK        = (  0,   0,   0)
LIGHTYELLOW  = (234, 233, 171)
RED          = (255,   0,   0)
PURPLE       = (255,   0, 255)
GOLD         = (255, 215,   0)
GREEN        = (  0, 255,   0)

SIZE_MULTIPLIER = 1.3

#GAME INFO DICTIONARY KEYS
CURRENT_TIME = 'current time'
LEVEL_NUM = 'level num'

#STATES FOR ENTIRE GAME (전체 게임에 대한 상태)
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'load screen'
GAME_LOSE = 'game los'
GAME_VICTORY = 'game victory'
LEVEL = 'level'

MAIN_MENU_IMAGE = 'MainMenu' # /resources/graphics/Screen/
OPTION_ADVENTURE = 'Adventure' # /resources/graphics/Screen/
GAME_LOOSE_IMAGE = 'GameLoose' # /resources/graphics/Screen/
GAME_VICTORY_IMAGE = 'GameVictory' # /resources/graphics/Screen/

#MAP COMPONENTS
BACKGROUND_NAME = 'Background'
BACKGROUND_TYPE = 'background_type'
INIT_SUN_NAME = 'init_sun_value'
ZOMBIE_LIST = 'zombie_list'

MAP_EMPTY = 0
MAP_EXIST = 1

BACKGROUND_OFFSET_X = 220
MAP_OFFSET_X = 35
MAP_OFFSET_Y = 100

#MENUBAR
CHOOSEBAR_TYPE = 'choosebar_type'
CHOOSEBAR_STATIC = 0
CHOOSEBAR_MOVE = 1
CHOSSEBAR_BOWLING = 2
MENUBAR_BACKGROUND = 'ChooserBackground' # /resources/graphics/Screen/
MOVEBAR_BACKGROUND = 'MoveBackground' # /resources/graphics/Screen/
PANEL_BACKGROUND = 'PanelBackground' # /resources/graphics/Screen/
START_BUTTON = 'StartButton' # /resources/graphics/Screen/
CARD_POOL = 'card_pool'

MOVEBAR_CARD_FRESH_TIME = 6000
CARD_MOVE_TIME = 60

#PLANT INFO 
PLANT_IMAGE_RECT = 'plant_image_rect'
CAR = 'car' # /resources/graphics/Screen/
SUN = 'Sun' # /resources/graphics/Plants/ dir
SUNFLOWER = 'SunFlower' # /resources/graphics/Plants/ dir
PEASHOOTER = 'Peashooter' # /resources/graphics/Plants/ dir
SNOWPEASHOOTER = 'SnowPea' # /resources/graphics/Plants/ dir
WALLNUT = 'WallNut' # /resources/graphics/Plants/ dir
CHERRYBOMB = 'CherryBomb'  # /resources/graphics/Plants/ dir
THREEPEASHOOTER = 'Threepeater' # /resources/graphics/Plants/ dir
REPEATERPEA = 'RepeaterPea' # /resources/graphics/Plants/ dir
CHOMPER = 'Chomper' # /resources/graphics/Plants/ dir
CHERRY_BOOM_IMAGE = 'Boom' # /resources/graphics/Screen/ 
PUFFSHROOM = 'PuffShroom' # /resources/graphics/Plants/ dir
POTATOMINE = 'PotatoMine' # /resources/graphics/Plants/ dir
SQUASH = 'Squash' # /resources/graphics/Plants/ dir
SPIKEWEED = 'Spikeweed' # /resources/graphics/Plants/ dir
JALAPENO = 'Jalapeno' # /resources/graphics/Plants/ dir
SCAREDYSHROOM = 'ScaredyShroom' # /resources/graphics/Plants/ dir
SUNSHROOM = 'SunShroom' # /resources/graphics/Plants/ dir
ICESHROOM = 'IceShroom' # /resources/graphics/Plants/ dir
HYPNOSHROOM = 'HypnoShroom' # /resources/graphics/Plants/ dir
WALLNUTBOWLING = 'WallNutBowling' # /resources/graphics/Plants/ dir
REDWALLNUTBOWLING = 'RedWallNutBowling' # /resources/graphics/Plants/ dir

PLANT_HEALTH = 5
WALLNUT_HEALTH = 30
WALLNUT_CRACKED1_HEALTH = 20
WALLNUT_CRACKED2_HEALTH = 10
WALLNUT_BOWLING_DAMAGE = 10

PRODUCE_SUN_INTERVAL = 7000
FLOWER_SUN_INTERVAL = 22000
SUN_LIVE_TIME = 7000
SUN_VALUE = 25

ICE_SLOW_TIME = 2000

FREEZE_TIME = 7500
ICETRAP = 'IceTrap'

#PLANT CARD INFO
CARD_SUNFLOWER = 'card_sunflower' # /resources/graphics/Cards/
CARD_PEASHOOTER = 'card_peashooter' # /resources/graphics/Cards/
CARD_SNOWPEASHOOTER = 'card_snowpea' # /resources/graphics/Cards/
CARD_WALLNUT = 'card_wallnut' # /resources/graphics/Cards/
CARD_CHERRYBOMB = 'card_cherrybomb' # /resources/graphics/Cards/
CARD_THREEPEASHOOTER = 'card_threepeashooter' # /resources/graphics/Cards/
CARD_REPEATERPEA = 'card_repeaterpea' # /resources/graphics/Cards/
CARD_CHOMPER = 'card_chomper' # /resources/graphics/Cards/
CARD_PUFFSHROOM = 'card_puffshroom' # /resources/graphics/Cards/
CARD_POTATOMINE = 'card_potatomine' # /resources/graphics/Cards/
CARD_SQUASH = 'card_squash' # /resources/graphics/Cards/
CARD_SPIKEWEED = 'card_spikeweed' # /resources/graphics/Cards/
CARD_JALAPENO = 'card_jalapeno' # /resources/graphics/Cards/
CARD_SCAREDYSHROOM = 'card_scaredyshroom' # /resources/graphics/Cards/
CARD_SUNSHROOM = 'card_sunshroom' # /resources/graphics/Cards/
CARD_ICESHROOM = 'card_iceshroom' # /resources/graphics/Cards/
CARD_HYPNOSHROOM = 'card_hypnoshroom' # /resources/graphics/Cards/
CARD_REDWALLNUT = 'card_redwallnut' # /resources/graphics/Cards/ +'_move'

#BULLET INFO (+Explode 2개)
BULLET_PEA = 'PeaNormal' # /resources/graphics/Bullets/
BULLET_PEA_ICE = 'PeaIce' # /resources/graphics/Bullets/
BULLET_MUSHROOM = 'BulletMushRoom' # /resources/graphics/Bullets/
BULLET_DAMAGE_NORMAL = 1

#ZOMBIE INFO
ZOMBIE_IMAGE_RECT = 'zombie_image_rect'
ZOMBIE_HEAD = 'ZombieHead' # /resources/graphics/Zombies/NormalZombie
NORMAL_ZOMBIE = 'Zombie' # /resources/graphics/Zombies/NormalZombie
CONEHEAD_ZOMBIE = 'ConeheadZombie' # /resources/graphics/Zombies/
BUCKETHEAD_ZOMBIE = 'BucketheadZombie' # /resources/graphics/Zombies/
FLAG_ZOMBIE = 'FlagZombie' # /resources/graphics/Zombies/
NEWSPAPER_ZOMBIE = 'NewspaperZombie' # /resources/graphics/Zombies/
BOOMDIE = 'BoomDie' # /resources/graphics/Zombies/NormalZombie
FLYING_ZOMBIE = 'FlyingZombie'

LOSTHEAD_HEALTH = 5
NORMAL_HEALTH = 10
FLAG_HEALTH = 15
CONEHEAD_HEALTH = 20
BUCKETHEAD_HEALTH = 30
NEWSPAPER_HEALTH = 15
FLYING_HEALTH = 35

ATTACK_INTERVAL = 1000
ZOMBIE_WALK_INTERVAL = 70

ZOMBIE_START_X = SCREEN_WIDTH + 50

#STATE
IDLE = 'idle'
FLY = 'fly'
EXPLODE = 'explode'
ATTACK = 'attack'
ATTACKED = 'attacked'
DIGEST = 'digest'
WALK = 'walk'
DIE = 'die'
CRY = 'cry'
FREEZE = 'freeze'
SLEEP = 'sleep'

#LEVEL STATE
CHOOSE = 'choose'
PLAY = 'play'

#BACKGROUND
BACKGROUND_DAY = 0
BACKGROUND_NIGHT = 1