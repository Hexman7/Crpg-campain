import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Troop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below... 
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n
   
def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

#Skills
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
knows_common_multiplayer = knows_trade_10|knows_inventory_management_10|knows_prisoner_management_10|knows_leadership_10|knows_spotting_10|knows_pathfinding_10|knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10
def_attrib = str_7 | agi_5 | int_4 | cha_4
def_attrib_multiplayer = int_30 | cha_30



knows_lord_1 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

lord_attrib = str_20|agi_20|int_20|cha_20|level(38)

knight_attrib_1 = str_12|agi_12|int_8|cha_16|level(22)
knight_attrib_2 = str_15|agi_15|int_10|cha_18|level(26)
knight_attrib_3 = str_18|agi_18|int_12|cha_20|level(30)
knight_attrib_4 = str_21|agi_21|int_13|cha_22|level(35)
knight_attrib_5 = str_24|agi_24|int_15|cha_25|level(41)
knight_skills_1 = knows_riding_3|knows_shield_6|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3
knight_skills_2 = knows_riding_4|knows_shield_6|knows_ironflesh_3|knows_power_strike_4|knows_athletics_3|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5|knows_trainer_2
knight_skills_3 = knows_riding_5|knows_shield_6|knows_ironflesh_4|knows_power_strike_5|knows_athletics_4|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6|knows_trainer_4
knight_skills_4 = knows_riding_6|knows_shield_6|knows_ironflesh_5|knows_power_strike_6|knows_athletics_5|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7|knows_trainer_6
knight_skills_5 = knows_riding_7|knows_shield_6|knows_ironflesh_6|knows_power_strike_7|knows_athletics_6|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9|knows_trainer_8

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

swadian_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
swadian_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
swadian_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
swadian_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
swadian_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

swadian_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

vaegir_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
vaegir_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
vaegir_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
vaegir_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
vaegir_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

vaegir_face_younger_2 = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_young_2   = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_middle_2  = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_old_2     = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_older_2   = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000

khergit_face_younger_1 = 0x0000000009003109207000000000000000000000001c80470000000000000000
khergit_face_young_1   = 0x00000003c9003109207000000000000000000000001c80470000000000000000
khergit_face_middle_1  = 0x00000007c9003109207000000000000000000000001c80470000000000000000
khergit_face_old_1     = 0x0000000b89003109207000000000000000000000001c80470000000000000000
khergit_face_older_1   = 0x0000000fc9003109207000000000000000000000001c80470000000000000000

khergit_face_younger_2 = 0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_young_2   = 0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_middle_2  = 0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_old_2     = 0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_older_2   = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000

nord_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
nord_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
nord_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
nord_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
nord_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

nord_face_younger_2 = 0x00000000310023084deeffffffffffff00000000001efff90000000000000000
nord_face_young_2   = 0x00000003b10023084deeffffffffffff00000000001efff90000000000000000
nord_face_middle_2  = 0x00000008310023084deeffffffffffff00000000001efff90000000000000000
nord_face_old_2     = 0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
nord_face_older_2   = 0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000

rhodok_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
rhodok_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
rhodok_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
rhodok_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
rhodok_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

rhodok_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

khergit_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
khergit_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2

bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2

undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

#NAMES:
#

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield

#MOD BEGIN
tf_guarantee_armors = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet

tf_guarantee_range = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged

#MOD END


troops = [
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
   [],
   str_4|agi_4|int_4|cha_4,wp(15),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_leather_jerkin, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_tribal_warrior_outfit, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows,itm_short_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],

####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
  ["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tutorial_maceman","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_club,itm_leather_jerkin,itm_hide_boots],
   str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],
  ["tutorial_archer","Archer","Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_tutorial_short_bow,itm_tutorial_arrows,itm_linen_tunic,itm_hide_boots],
   str_6|agi_6|level(5),wp(100),knows_common|knows_power_draw_4,mercenary_face_1,mercenary_face_2],
  ["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_sword,itm_leather_vest,itm_hide_boots],
   str_6|agi_6|level(5),wp(80),knows_common,mercenary_face_1,mercenary_face_2],

  ["novice_fighter","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["regular_fighter","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common|knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_riding_1|knows_shield_2,mercenary_face_1, mercenary_face_2],
  ["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,0,fac_commoners,
   [itm_hide_boots],
   str_10|agi_10|level(17),wp(110),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_11|level(22),wp(140),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_riding_3|knows_shield_4,mercenary_face_1, mercenary_face_2],

  ["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_7|agi_6|level(7),wp(70),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_7|level(9),wp(80),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_9|agi_8|level(13),wp(100),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_10|agi_9|level(15),wp(110),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_10|agi_10|level(17),wp(120),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_11|agi_10|level(19),wp(130),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_11|level(21),wp(140),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_12|level(23),wp(150),knows_common,mercenary_face_1, mercenary_face_2],

  ["cattle","Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],


#soldiers:
#This troop is the troop marked as soldiers_begin
  ["farmer","Farmer","Farmers",tf_guarantee_armor,0,0,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,
    itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
  ["townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_club,itm_staff,itm_dagger,itm_stones,itm_leather_cap,itm_linen_tunic,itm_coarse_tunic,itm_leather_apron,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["watchman","Watchman","Watchmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_bolts,itm_spiked_club,itm_fighting_pick,itm_sword_medieval_a,itm_boar_spear,itm_hunting_crossbow,itm_light_crossbow,itm_tab_shield_round_a,itm_tab_shield_round_b,
    itm_padded_cloth,itm_leather_jerkin,itm_leather_cap,itm_padded_coif,itm_footman_helmet,itm_nomad_boots,itm_wrapping_boots],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(70)|wp_throwing(60),knows_common|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1,mercenary_face_1, mercenary_face_2],
  ["caravan_guard","Caravan Guard","Caravan Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,no_scene,0,fac_commoners,
   [itm_spear,itm_fighting_pick,itm_sword_medieval_a,itm_voulge,itm_tab_shield_round_b,itm_tab_shield_round_c,
    itm_leather_jerkin,itm_leather_vest,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet,itm_saddle_horse],
   str_12 | agi_9 | int_4 | cha_4|level(17),wp_one_handed(120)|wp_two_handed(120)|wp_polearm(120)|wp_archery(10)|wp_crossbow(10)|wp_throwing(80),knows_common|knows_power_strike_3|knows_ironflesh_3|knows_shield_2|knows_athletics_3|knows_riding_3|knows_power_throw_2,mercenary_face_1, mercenary_face_2],
  ["mercenary_swordsman","Mercenary Swordsman","Mercenary Swordsmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_bastard_sword_a,itm_sword_medieval_b,itm_sword_medieval_b_small,itm_tab_shield_heater_c,
    itm_mail_hauberk,itm_haubergeon,itm_leather_boots,itm_mail_chausses,itm_kettle_hat,itm_mail_coif,itm_flat_topped_helmet, itm_helmet_with_neckguard],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5|knows_power_throw_3,mercenary_face_1, mercenary_face_2],
  ["hired_blade","Hired Blade","Hired Blades",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_bastard_sword_b,itm_sword_medieval_c,itm_tab_shield_heater_cav_a,
    itm_haubergeon,itm_mail_chausses,itm_iron_greaves,itm_plate_boots,itm_guard_helmet,itm_great_helmet,itm_bascinet, itm_leather_gloves],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7|knows_power_throw_4,mercenary_face_1, mercenary_face_2],
  ["mercenary_crossbowman","Mercenary Crossbowman","Mercenary Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_bolts,itm_spiked_club,itm_fighting_pick,itm_sword_medieval_a,itm_boar_spear,itm_crossbow,itm_tab_shield_pavise_a,itm_tab_shield_round_b,
    itm_padded_cloth,itm_leather_jerkin,itm_leather_cap,itm_padded_coif,itm_footman_helmet,itm_nomad_boots,itm_wrapping_boots],
   str_11 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5,mercenary_face_1, mercenary_face_2],
  ["mercenary_horseman","Mercenary Horseman","Mercenary Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_lance,itm_bastard_sword_a,itm_sword_medieval_b,itm_tab_shield_heater_c,
    itm_mail_shirt,itm_haubergeon,itm_leather_boots,itm_norman_helmet,itm_mail_coif,itm_helmet_with_neckguard,itm_saddle_horse,itm_courser],
   str_15 | agi_12 | int_4 | cha_4|level(21),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_5|knows_ironflesh_4|knows_shield_4|knows_athletics_5|knows_riding_5|knows_power_throw_3,mercenary_face_1, mercenary_face_2],
  ["mercenary_cavalry","Mercenary Cavalry","Mercenary Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_heavy_lance,itm_bastard_sword_a,itm_sword_medieval_b,itm_tab_shield_heater_c,
   itm_cuir_bouilli,itm_banded_armor,itm_hide_boots,itm_kettle_hat,itm_mail_coif,itm_flat_topped_helmet,itm_helmet_with_neckguard,itm_warhorse,itm_hunter],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_strike_7|knows_ironflesh_6|knows_shield_5|knows_athletics_6|knows_riding_7|knows_power_throw_4,mercenary_face_1, mercenary_face_2],
  ["mercenary_horse_crossbowman","Mercenary Horse Crossbowman","Mercenary Horse Crossbowmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_hunting_crossbow,itm_bolts,itm_sword_medieval_a,itm_sword_medieval_b,itm_fighting_pick,
    itm_hide_boots,itm_nomad_boots,itm_ragged_outfit,itm_padded_cloth,itm_footman_helmet,itm_nasal_helmet,itm_norman_helmet,itm_leather_gloves,itm_saddle_horse,itm_saddle_horse_b],
   str_11 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5|knows_horse_archery_3|knows_riding_3,khergit_face_young_1, khergit_face_older_2],
  ["mercenary_veteran_horse_crossbowman","Mercenary Veteran Horse Crossbowman","Mercenary Veteran Horse Crossbowmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_hunting_crossbow,itm_bolts,itm_light_crossbow,itm_steel_bolts,itm_sword_medieval_c,itm_sword_medieval_b,itm_military_pick,itm_military_cleaver_b,
    itm_hose_kneecops_red,itm_brigandine_purple,itm_brigandine_green,itm_brigandine_brown,itm_chapel_de_fer_e,itm_chapel_de_fer_f,itm_chapel_de_fer_d,itm_leather_gloves,itm_hunter,itm_saddle_horse,itm_courser,itm_saddle_horse_b],
   str_13 | agi_12 | int_4 | cha_4|level(19),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6|knows_horse_archery_4|knows_riding_5,khergit_face_young_1, khergit_face_older_2],
  ["mercenary_elite_horse_crossbowman","Mercenary Elite Horse Crossbowman","Mercenary Elite Horse Crossbowmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_commoners,
   [itm_light_crossbow,itm_steel_bolts,itm_sword_medieval_c_long,itm_sword_medieval_d_long,itm_sword_medieval_c,itm_military_hammer,itm_military_cleaver_c,
    itm_hose_kneecops_green,itm_hose_kneecops_red,itm_brigandine_brown_a,itm_brigandine_purple_a,itm_brigandine_green_b,itm_chapel_de_fer_c,itm_chapel_de_fer_b,itm_chapel_de_fer_a,itm_mail_gauntlets,itm_mail_gauntlets,itm_hunter,itm_courser],
   str_15 | agi_15 | int_4 | cha_4|level(24),wp_one_handed(95)|wp_two_handed(50)|wp_polearm(80)|wp_archery(180)|wp_crossbow(180)|wp_throwing(180),knows_common|knows_power_strike_3|knows_ironflesh_5|knows_athletics_7|knows_horse_archery_7|knows_riding_5,khergit_face_young_1, khergit_face_older_2],
  ["mercenary_horse_thrower","Mercenary Horse Thrower","Mercenary Horse Throwers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_javelin,itm_winged_mace,itm_sword_khergit_1,itm_sword_khergit_3,
    itm_hide_boots,itm_nomad_boots,itm_deli_robe,itm_nomad_robe,itm_tribal_warrior_outfit,itm_steppe_cap,itm_leather_steppe_cap_a,itm_sarranid_horseman_helmet,itm_leather_gloves,itm_steppe_horse,itm_saddle_horse],
   str_11 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5|knows_horse_archery_2|knows_riding_3|knows_power_throw_3,khergit_face_young_1, khergit_face_older_2],
  ["mercenary_veteran_horse_thrower","Mercenary Veteran Horse Thrower","Mercenary Veteran Horse Throwers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_javelin,itm_jarid,itm_scimitar,itm_winged_mace,itm_sword_khergit_2,itm_sword_khergit_3,itm_spiked_mace,
    itm_leather_boots,itm_khergit_leather_boots,itm_lamellar_vest,itm_lamellar_vest_khergit,itm_saracen_mail_b,itm_sarranid_horseman_helmet,itm_khergit_war_helmet,itm_sipahi_helmet_a,itm_leather_gloves,itm_courser,itm_steppe_horse],
   str_13 | agi_12 | int_4 | cha_4|level(19),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6|knows_horse_archery_3|knows_riding_4|knows_power_throw_5,khergit_face_young_1, khergit_face_older_2],
  ["mercenary_elite_horse_thrower","Mercenary Elite Horse Thrower","Mercenary Elite Horse Throwers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_commoners,
   [itm_jarid,itm_scimitar_b,itm_spiked_mace,itm_sword_khergit_4,itm_sword_khergit_2,
    itm_splinted_greaves,itm_splinted_leather_greaves,itm_arabian_armor_b,itm_mongol_armor,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_scale_gauntlets,itm_scale_gloves_b,itm_hunter,itm_courser],
   str_15 | agi_15 | int_4 | cha_4|level(24),wp_one_handed(95)|wp_two_handed(50)|wp_polearm(80)|wp_archery(180)|wp_crossbow(180)|wp_throwing(180),knows_common|knows_power_strike_2|knows_ironflesh_5|knows_athletics_7|knows_horse_archery_4|knows_riding_5|knows_power_throw_7,khergit_face_young_1, khergit_face_older_2],

   
#### Swadian mercenaries begin
  ["swadian_militia_merc","Swadian Militia","Swadian Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_commoners,
   [itm_bolts,itm_spiked_club,itm_fighting_pick,itm_boar_spear,itm_hunting_crossbow,itm_tab_shield_heater_a,
    itm_padded_cloth,itm_red_gambeson,itm_arming_cap,itm_arming_cap,itm_ankle_boots,itm_wrapping_boots],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(60)|wp_throwing(60),knows_common|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1|knows_power_throw_1, swadian_face_young_1, swadian_face_old_2],
  ["swadian_footman_merc","Swadian Footman","Swadian Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_commoners,
   [itm_spear,itm_fighting_pick,itm_sword_medieval_b_small,itm_sword_medieval_a,itm_tab_shield_heater_b,
    itm_mail_with_tunic_red,itm_ankle_boots,itm_mail_coif,itm_norman_helmet],
   str_12 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(110)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(80),knows_common|knows_power_strike_4|knows_ironflesh_2|knows_shield_2|knows_athletics_3|knows_power_throw_2,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_merc","Swadian Infantry","Swadian Infantry",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_pike,itm_fighting_pick,itm_bastard_sword_a,itm_sword_medieval_a,itm_sword_medieval_b_small,itm_tab_shield_heater_c,
    itm_mail_with_surcoat,itm_haubergeon,itm_mail_chausses,itm_leather_boots,itm_segmented_helmet,itm_flat_topped_helmet,itm_helmet_with_neckguard],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5|knows_power_throw_3,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_sergeant_merc","Swadian Sergeant","Swadian Sergeants",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_awlpike,itm_bastard_sword_b,itm_morningstar,itm_sword_medieval_c,itm_tab_shield_heater_d,
    itm_coat_of_plates,itm_brigandine_red,itm_mail_boots,itm_iron_greaves,itm_flat_topped_helmet,itm_guard_helmet,itm_mail_mittens,itm_gauntlets],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7|knows_power_throw_5,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_skirmisher_merc","Swadian Skirmisher","Swadian Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_club,itm_voulge,itm_tab_shield_heater_a,
    itm_red_gambeson,itm_padded_cloth,itm_ankle_boots,itm_arming_cap,itm_arming_cap],
   str_11 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5|knows_power_draw_3,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_crossbowman_merc","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_crossbow,itm_light_crossbow,itm_fighting_pick,itm_sword_medieval_a,itm_voulge,itm_tab_shield_heater_b,
    itm_leather_jerkin,itm_red_gambeson,itm_leather_boots,itm_ankle_boots,itm_norman_helmet,itm_segmented_helmet],
   str_13 | agi_12 | int_4 | cha_4|level(19),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6|knows_power_draw_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_sharpshooter_merc","Swadian Sharpshooter","Swadian Sharpshooters",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_bolts,itm_arrows,itm_crossbow,itm_crossbow,itm_heavy_crossbow,itm_sword_medieval_b_small,itm_sword_medieval_a,itm_voulge,itm_tab_shield_heater_c,
    itm_haubergeon,itm_arena_armor_red,itm_leather_boots,itm_mail_chausses,itm_kettle_hat,itm_helmet_with_neckguard,itm_leather_gloves],
   str_14 | agi_10 | int_4 | cha_4|level(24),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (120) | wp_throwing (100),knows_common|knows_power_draw_3|knows_ironflesh_1|knows_power_strike_1|knows_athletics_2,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_man_at_arms_merc","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_commoners,
   [itm_lance,itm_fighting_pick,itm_bastard_sword_b,itm_sword_medieval_b,itm_sword_medieval_c_small,itm_tab_shield_heater_cav_a,
    itm_haubergeon,itm_mail_with_surcoat,itm_mail_chausses,itm_norman_helmet,itm_mail_coif,itm_flat_topped_helmet,itm_helmet_with_neckguard,itm_warhorse,itm_warhorse,itm_hunter],
   str_12 | agi_9 | int_4 | cha_4|level(17),wp_one_handed(120)|wp_two_handed(120)|wp_polearm(120)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_3|knows_ironflesh_3|knows_shield_2|knows_athletics_3|knows_riding_3|knows_power_throw_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_cavalryman_merc","Swadian Cavalryman","Swadian Cavalrymen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_commoners,
   [itm_heavy_lance,itm_sword_two_handed_b,itm_sword_medieval_d_long,itm_morningstar,itm_morningstar,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,
    itm_coat_of_plates_red,itm_cuir_bouilli,itm_plate_boots,itm_guard_helmet,itm_great_helmet,itm_bascinet,itm_charger,itm_warhorse,itm_gauntlets,itm_mail_mittens],
   str_15 | agi_12 | int_4 | cha_4|level(21),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_strike_5|knows_ironflesh_4|knows_shield_4|knows_athletics_5|knows_riding_5|knows_power_throw_5,swadian_face_middle_1, swadian_face_older_2],



### Swadian mercenaries end


### Vaegir mercenaries begin

  ["vaegir_footman_merc","Vaegir Footman","Vaegir Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_commoners,
   [itm_spiked_club,itm_hand_axe,itm_sword_viking_1,itm_two_handed_axe,itm_tab_shield_kite_a,itm_tab_shield_kite_b,itm_spear,
    itm_nomad_cap,itm_vaegir_fur_cap,itm_rawhide_coat,itm_nomad_armor,itm_nomad_boots],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(10)|wp_throwing(60),knows_common|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1|knows_power_throw_1, vaegir_face_young_1, vaegir_face_middle_2],
  ["vaegir_skirmisher_merc","Vaegir Skirmisher","Vaegir Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_sword_khergit_1,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,
    itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   str_11 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5|knows_power_draw_3,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_archer_merc","Vaegir Archer","Vaegir Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_arrows,itm_axe,itm_sword_khergit_1,itm_nomad_bow,itm_nomad_bow,itm_short_bow,
    itm_leather_jerkin,itm_leather_vest,itm_nomad_boots,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_nomad_cap],
   str_13 | agi_12 | int_4 | cha_4|level(19),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6|knows_power_draw_4,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_marksman_merc","Vaegir Marksman","Vaegir Marksmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_barbed_arrows,itm_axe,itm_voulge,itm_sword_khergit_2,itm_strong_bow,itm_war_bow,itm_strong_bow,
    itm_leather_vest,itm_studded_leather_coat,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet],
   str_15 | agi_15 | int_4 | cha_4|level(24),wp_one_handed(95)|wp_two_handed(50)|wp_polearm(80)|wp_archery(180)|wp_crossbow(180)|wp_throwing(180),knows_common|knows_power_strike_2|knows_ironflesh_5|knows_athletics_7|knows_power_draw_6,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_veteran_merc","Vaegir Veteran","Vaegir Veterans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_commoners,
   [itm_spiked_mace,itm_two_handed_axe,itm_sword_viking_1,itm_tab_shield_kite_b,itm_tab_shield_kite_c,itm_spear,
    itm_steppe_cap,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_leather_jerkin,itm_studded_leather_coat,itm_nomad_boots,itm_saddle_horse],
   str_12 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(110)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(80),knows_common|knows_power_strike_4|knows_ironflesh_2|knows_shield_2|knows_athletics_3|knows_power_throw_2,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_infantry_merc","Vaegir Infantry","Vaegir Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_pike,itm_battle_axe,itm_sword_viking_2,itm_sword_khergit_2,itm_tab_shield_kite_c,itm_spear,
    itm_mail_hauberk,itm_lamellar_vest,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5|knows_power_throw_3,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_guard_merc","Vaegir Guard","Vaegir Guards",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_ashwood_pike,itm_bardiche,itm_battle_axe,itm_one_handed_battle_axe_a,itm_tab_shield_kite_d,
    itm_banded_armor,itm_lamellar_vest,itm_lamellar_armor,itm_mail_chausses,itm_iron_greaves,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_lamellar_helmet,itm_leather_gloves],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7|knows_power_throw_5,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_horseman_merc","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_commoners,
   [itm_battle_axe,itm_sword_khergit_2,itm_lance,itm_tab_shield_kite_cav_a,itm_spear,
    itm_studded_leather_coat,itm_lamellar_vest,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_steppe_horse,itm_hunter],
   str_15 | agi_12 | int_4 | cha_4|level(21),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_5|knows_ironflesh_4|knows_shield_4|knows_athletics_5|knows_riding_5|knows_power_throw_3,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_cavalryman_merc","Vaegir Cavalryman","Vaegir Cavalrymen",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_commoners,
   [itm_bardiche,itm_war_axe,itm_one_handed_battle_axe_a,itm_lance,itm_lance,itm_tab_shield_kite_cav_b,
    itm_banded_armor,itm_lamellar_vest,itm_lamellar_armor,itm_mail_boots,itm_plate_boots,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_lamellar_helmet,itm_hunter, itm_warhorse_steppe,itm_leather_gloves],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_strike_7|knows_ironflesh_6|knows_shield_5|knows_athletics_6|knows_riding_7|knows_power_throw_5,vaegir_face_middle_1, vaegir_face_older_2],


### Vaegir mercenaries end


### Khergit mercenaries begin

  ["khergit_skirmisher_merc","Khergit Skirmisher","Khergit Skirmishers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_commoners,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear,itm_nomad_bow,itm_javelin,itm_tab_shield_small_round_a,
    itm_steppe_cap,itm_nomad_cap_b,itm_leather_steppe_cap_a,itm_khergit_armor,itm_steppe_armor,itm_leather_vest,itm_nomad_boots,itm_khergit_leather_boots,itm_steppe_horse,itm_saddle_horse],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(65)|wp_two_handed(20)|wp_polearm(50)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100),knows_common|knows_power_strike_1|knows_ironflesh_1|knows_athletics_3|knows_power_draw_1|knows_riding_1|knows_power_throw_1|knows_horse_archery_1,khergit_face_younger_1, khergit_face_old_2],
  ["khergit_horseman_merc","Khergit Horseman","Khergit Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_commoners,
  [itm_arrows,itm_light_lance,itm_nomad_bow,itm_sword_khergit_2,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_spear,
   itm_leather_steppe_cap_a, itm_leather_steppe_cap_b,itm_nomad_robe,itm_nomad_vest,itm_khergit_leather_boots,itm_hide_boots,itm_spiked_helmet,itm_nomad_cap,itm_steppe_horse,itm_hunter],
   str_12 | agi_9 | int_4 | cha_4|level(17),wp_one_handed(120)|wp_two_handed(120)|wp_polearm(120)|wp_archery(110)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_3|knows_ironflesh_3|knows_shield_2|knows_athletics_3|knows_power_draw_2|knows_horse_archery_2|knows_power_throw_2|knows_riding_3,khergit_face_young_1, khergit_face_older_2],
  ["khergit_horse_archer_merc","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_commoners,
   [itm_arrows,itm_sword_khergit_2,itm_winged_mace,itm_spear,itm_khergit_bow,itm_tab_shield_small_round_a,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_bodkin_arrows,itm_arrows,itm_javelin,
    itm_leather_steppe_cap_b,itm_nomad_cap_b,itm_tribal_warrior_outfit,itm_nomad_robe,itm_khergit_leather_boots,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_steppe_horse],
   str_11 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5|knows_power_draw_3|knows_horse_archery_2|knows_riding_3|knows_power_throw_3,khergit_face_young_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer_merc","Khergit Veteran Horse Archer","Khergit Veteran Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_commoners,
   [itm_sword_khergit_3,itm_winged_mace,itm_spear,itm_khergit_bow,itm_khergit_bow,itm_khergit_bow,itm_nomad_bow,itm_arrows,itm_khergit_arrows,itm_khergit_arrows,itm_khergit_arrows,itm_javelin,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,
    itm_khergit_cavalry_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap,itm_lamellar_vest_khergit,itm_tribal_warrior_outfit,itm_khergit_leather_boots,itm_leather_gloves,itm_steppe_horse,itm_courser],
   str_13 | agi_12 | int_4 | cha_4|level(19),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6|knows_power_draw_4|knows_horse_archery_3|knows_riding_4|knows_power_throw_4|knows_shield_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_merc","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_commoners,
   [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
    itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_scale_gauntlets,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_courser,itm_warhorse_steppe,itm_warhorse_steppe,itm_warhorse_steppe],
   str_15 | agi_12 | int_4 | cha_4|level(21),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_strike_5|knows_ironflesh_4|knows_shield_4|knows_athletics_5|knows_riding_5|knows_power_throw_5,khergit_face_middle_1, khergit_face_older_2],

### Khergit mercenaries end
### Nord mercenaries begin
  ["nord_footman_merc","Nord Footman","Nord Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_commoners,
   [itm_one_handed_battle_axe_a,itm_one_handed_war_axe_a,itm_spear,itm_tab_shield_round_a,itm_tab_shield_round_b,itm_javelin,itm_throwing_axes,
    itm_leather_cap,itm_skullcap,itm_nomad_vest,itm_leather_boots,itm_nomad_boots],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(10)|wp_throwing(60),knows_common|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1|knows_power_throw_1,nord_face_young_1, nord_face_old_2],
  ["nord_trained_footman_merc","Nord Trained Footman","Nord Trained Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_one_handed_war_axe_a,itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,itm_tab_shield_round_b,
    itm_skullcap,itm_nasal_helmet,itm_nordic_footman_helmet,itm_byrnie,itm_studded_leather_coat,itm_leather_boots],
   str_12 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(110)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(80),knows_common|knows_power_strike_4|knows_ironflesh_2|knows_shield_2|knows_athletics_3|knows_power_throw_2,nord_face_young_1, nord_face_old_2],
  ["nord_warrior_merc","Nord Warrior","Nord Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_sword_viking_1,itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,itm_tab_shield_round_c,itm_javelin,
    itm_nordic_footman_helmet,itm_nordic_fighter_helmet,itm_mail_shirt,itm_studded_leather_coat,itm_hunter_boots,itm_leather_boots],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5|knows_power_throw_3,nord_face_young_1, nord_face_older_2],
  ["nord_veteran_merc","Nord Veteran","Nord Veterans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_sword_viking_2,itm_sword_viking_2_small,itm_one_handed_battle_axe_b,itm_spiked_mace,itm_tab_shield_round_d,itm_javelin,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_fighter_helmet,itm_mail_hauberk,itm_mail_shirt,itm_splinted_leather_greaves,itm_leather_boots,itm_leather_gloves],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7|knows_power_throw_4,nord_face_young_1, nord_face_older_2],
  ["nord_champion_merc","Nord Huscarl","Nord Huscarls",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_sword_viking_3,itm_sword_viking_3_small,itm_great_axe,itm_one_handed_battle_axe_c,itm_tab_shield_round_e,itm_throwing_spears,itm_heavy_throwing_axes,itm_heavy_throwing_axes,
    itm_nordic_huscarl_helmet,itm_nordic_warlord_helmet,itm_banded_armor,itm_mail_boots,itm_mail_chausses,itm_mail_mittens],
   str_21 | agi_18 | int_4 | cha_4|level(29),wp_one_handed(210)|wp_two_handed(210)|wp_polearm(210)|wp_archery(10)|wp_crossbow(10)|wp_throwing(140),knows_common|knows_power_strike_9|knows_ironflesh_7|knows_shield_6|knows_athletics_7|knows_power_throw_6,nord_face_middle_1, nord_face_older_2],
  ["nord_huntsman_merc","Nord Huntsman","Nord Huntsmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_arrows,itm_rawhide_coat,itm_hatchet,itm_hunting_bow,itm_hide_boots],
   str_11 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5|knows_power_draw_3,nord_face_young_1, nord_face_old_2],
  ["nord_archer_merc","Nord Archer","Nord Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_arrows,itm_axe,itm_short_bow,itm_padded_leather,itm_leather_jerkin,itm_padded_leather,itm_leather_boots,itm_nasal_helmet,itm_nordic_archer_helmet,itm_leather_cap],
   str_13 | agi_12 | int_4 | cha_4|level(19),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6|knows_power_draw_4,nord_face_young_1, nord_face_old_2],
  ["nord_veteran_archer_merc","Nord Veteran Archer","Nord Veteran Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bodkin_arrows,itm_sword_viking_2,itm_one_handed_battle_axe_a,itm_two_handed_axe,itm_long_bow,itm_mail_shirt,itm_mail_shirt,itm_byrnie,itm_leather_boots,itm_nordic_archer_helmet,itm_nordic_veteran_archer_helmet],
   str_15 | agi_15 | int_4 | cha_4|level(24),wp_one_handed(95)|wp_two_handed(50)|wp_polearm(80)|wp_archery(180)|wp_crossbow(180)|wp_throwing(180),knows_common|knows_power_strike_2|knows_ironflesh_5|knows_athletics_7|knows_power_draw_6,nord_face_middle_1, nord_face_older_2],
   
### Nord mercenaries end
### Rhodok mercenaries begin
  ["rhodok_spearman_merc","Rhodok Spearman","Rhodok Spearmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_spear,itm_pike,itm_spear,itm_tab_shield_pavise_a,itm_falchion,
    itm_felt_hat_b,itm_common_hood,itm_leather_armor,itm_arena_tunic_green,itm_wrapping_boots,itm_nomad_boots],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(10)|wp_throwing(60),knows_common|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1|knows_power_throw_1,rhodok_face_young_1, rhodok_face_old_2],
  ["rhodok_trained_spearman_merc","Rhodok Trained Spearman","Rhodok Trained Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_commoners,
   [itm_pike,itm_war_spear,itm_tab_shield_pavise_b,
    itm_footman_helmet,itm_padded_coif,itm_aketon_green,itm_aketon_green,itm_ragged_outfit,itm_nomad_boots,itm_leather_boots],
   str_12 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(110)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(80),knows_common|knows_power_strike_4|knows_ironflesh_2|knows_shield_2|knows_athletics_3|knows_power_throw_2,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman_merc","Rhodok Veteran Spearman","Rhodok Veteran Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_commoners,
   [itm_ashwood_pike,itm_glaive,itm_tab_shield_pavise_c,
    itm_kettle_hat,itm_mail_coif,itm_mail_with_tunic_green,itm_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5|knows_power_throw_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_sergeant_merc","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_commoners,
   [itm_glaive,itm_military_hammer,itm_military_cleaver_c,itm_tab_shield_pavise_d,
    itm_full_helm, itm_bascinet_3,itm_bascinet_2,itm_surcoat_over_mail,itm_surcoat_over_mail,itm_heraldic_mail_with_surcoat,itm_mail_chausses,itm_leather_gloves,itm_mail_mittens],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7|knows_power_throw_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_crossbowman_merc","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_commoners,
   [itm_sword_medieval_a,itm_falchion,itm_club_with_spike_head,itm_tab_shield_pavise_a,itm_crossbow,itm_bolts,
    itm_arena_tunic_green,itm_felt_hat_b,itm_common_hood,itm_nomad_boots,itm_wrapping_boots],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(65)|wp_two_handed(20)|wp_polearm(50)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100),knows_common|knows_power_strike_1|knows_ironflesh_1|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_trained_crossbowman_merc","Rhodok Trained Crossbowman","Rhodok Trained Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners,
   [itm_sword_medieval_a,itm_sword_medieval_b_small,itm_club_with_spike_head,itm_tab_shield_pavise_a,itm_crossbow,itm_bolts,
    itm_common_hood,itm_leather_armor,itm_arena_tunic_green,itm_nomad_boots],
   str_11 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_veteran_crossbowman_merc","Rhodok Veteran Crossbowman","Rhodok Veteran Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners,
   [itm_sword_medieval_a,itm_sword_medieval_b_small,itm_fighting_pick,itm_club_with_spike_head,itm_tab_shield_pavise_b,itm_tab_shield_pavise_c,itm_heavy_crossbow,itm_bolts,
    itm_leather_cap,itm_felt_hat_b,itm_aketon_green,itm_leather_boots],
   str_13 | agi_12 | int_4 | cha_4|level(19),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sharpshooter_merc","Rhodok Sharpshooter","Rhodok Sharpshooters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners,
   [itm_sword_medieval_b,itm_military_pick,itm_military_hammer,itm_tab_shield_pavise_c,itm_sniper_crossbow,itm_steel_bolts,
    itm_kettle_hat,itm_mail_coif,itm_mail_with_tunic_green,itm_leather_boots,itm_splinted_leather_greaves],
   str_15 | agi_15 | int_4 | cha_4|level(24),wp_one_handed(95)|wp_two_handed(50)|wp_polearm(80)|wp_archery(180)|wp_crossbow(180)|wp_throwing(180),knows_common|knows_power_strike_2|knows_ironflesh_5|knows_athletics_7,rhodok_face_middle_1, rhodok_face_older_2],

### Rhodok mercenaries end

### Sarranid mercenaries begin
 ["sarranid_footman_merc","Sarranid Footman","Sarranid Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_commoners,
   [itm_bamboo_spear,itm_arabian_sword_a,itm_tab_shield_kite_a,itm_desert_turban,
    itm_skirmisher_armor,itm_turban,itm_sarranid_boots_a,itm_sarranid_boots_b],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(10)|wp_throwing(60),knows_common|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1|knows_power_throw_1,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_veteran_footman_merc","Sarranid Veteran Footman","Sarranid Veteran Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_bamboo_spear,itm_arabian_sword_a,itm_arabian_sword_b,itm_tab_shield_kite_b,
    itm_sarranid_boots_b,itm_sarranid_warrior_cap,itm_sarranid_leather_armor,itm_jarid,itm_arabian_sword_a,itm_mace_3],
   str_12 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(110)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(80),knows_common|knows_power_strike_4|knows_ironflesh_2|knows_shield_2|knows_athletics_3|knows_power_throw_2,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_infantry_merc","Sarranid Infantry","Sarranid Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_sarranid_mail_shirt,itm_sarranid_mail_coif,itm_jarid,itm_sarranid_boots_c,itm_sarranid_boots_b,itm_sarranid_axe_a,itm_arabian_sword_b,itm_mace_3,itm_spear,itm_tab_shield_kite_c],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5|knows_power_throw_3,swadian_face_middle_1, swadian_face_old_2],
 ["sarranid_guard_merc","Sarranid Guard","Sarranid Guards",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_military_pick,itm_sarranid_two_handed_axe_a,itm_jarid,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_sarranid_boots_d, itm_sarranid_boots_c,itm_arabian_armor_b,itm_sarranid_mail_coif,itm_sarranid_veiled_helmet,itm_mail_mittens,itm_leather_gloves,itm_tab_shield_kite_d],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7|knows_power_throw_5,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_skirmisher_merc","Sarranid Skirmisher","Sarranid Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_turban,itm_desert_turban,itm_skirmisher_armor,itm_jarid,itm_jarid,itm_arabian_sword_a,itm_spiked_club,itm_tab_shield_small_round_a,itm_sarranid_warrior_cap,itm_sarranid_boots_a],
   str_11 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5|knows_power_draw_3,swadian_face_young_1, swadian_face_middle_2],
 ["sarranid_archer_merc","Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_arrows,itm_arrows,itm_nomad_bow,itm_arabian_sword_a,itm_archers_vest,itm_sarranid_boots_b,itm_sarranid_helmet1,itm_sarranid_warrior_cap,itm_turban,itm_desert_turban],
  str_13 | agi_12 | int_4 | cha_4|level(19),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6|knows_power_draw_4,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_master_archer_merc","Sarranid Master Archer","Sarranid Master Archers",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_barbed_arrows,itm_barbed_arrows,itm_arabian_sword_b,itm_mace_3,itm_strong_bow,itm_nomad_bow,
    itm_arabian_armor_b,itm_sarranid_boots_c,itm_sarranid_boots_b,itm_sarranid_mail_coif],
  str_15 | agi_15 | int_4 | cha_4|level(24),wp_one_handed(95)|wp_two_handed(50)|wp_polearm(80)|wp_archery(180)|wp_crossbow(180)|wp_throwing(180),knows_common|knows_power_strike_2|knows_ironflesh_5|knows_athletics_7|knows_power_draw_6,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_horseman_merc","Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_commoners,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_sarranid_boots_c,itm_sarranid_boots_b, itm_sarranid_horseman_helmet,itm_leather_gloves,itm_arabian_horse_a,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100)|wp_throwing(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3|knows_power_throw_3,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_mamluke_merc","Sarranid Mamluke","Sarranid Mamlukes",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_commoners,
   [itm_heavy_lance,itm_scimitar_b,itm_sarranid_two_handed_mace_1,itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c,
    itm_mamluke_mail,itm_sarranid_boots_d,itm_sarranid_boots_c,itm_sarranid_veiled_helmet,itm_arabian_horse_b,itm_warhorse_sarranid,itm_scale_gauntlets,itm_mail_mittens],
   def_attrib|level(27),wp_one_handed (150) | wp_two_handed (130) | wp_polearm (130) | wp_archery (75) | wp_crossbow (75) | wp_throwing (120),knows_common|knows_riding_6|knows_shield_5|knows_ironflesh_5|knows_power_strike_5|knows_power_throw_5,swadian_face_middle_1, swadian_face_older_2],
	
### Sarranid mercenaries end	
 ["mercenaries_end","mercenaries_end","mercenaries_end",0,no_scene,reserved,fac_commoners,
   [],
  def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],

#Swadia  12
  ["swadian_recruit","Polan's Recruit","Polan's Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_scythe,itm_hatchet,itm_club,itm_stones,itm_tab_shield_pavise_a,itm_pitch_fork,
	itm_leather_cap,itm_fur_hat,itm_red_shirt,itm_short_tunic,itm_wrapping_boots,itm_hide_boots],
   str_7 | agi_5 | int_4 | cha_4|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 
  ["swadian_militia","Polan's Militia","Polan's Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_sword_medieval_b,itm_spear,itm_tab_shield_pavise_a,itm_tab_shield_pavise_b,itm_leather_gloves,itm_javelin,
    itm_tabard,itm_red_kaftan,itm_white_kaftan,itm_mail_coif,itm_nasal_helmet,itm_serbian_ankle_boots,itm_nomad_boots,itm_wrapping_boots],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(10)|wp_throwing(60),knows_common|knows_power_throw_1|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  
  ["swadian_footman","Polan's Footman","Polan's Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_sword_medieval_c,itm_fighting_pick,itm_sword_medieval_c_small,itm_tab_shield_pavise_b,itm_tab_shield_pavise_c,itm_spear,itm_mail_mittens,itm_mail_gloves,itm_javelin,
    itm_kaftan_over_mail_c,itm_brigandine_white,itm_brigandine_red_c,itm_kaftan_over_mail_d,itm_surcoat_over_mail_heraldic,itm_lithuanian_helmet,itm_helmet_with_neckguard,itm_mail_coif,itm_hose_kneecops_red,itm_mail_chausses,itm_rus_cav_boots],
   str_12 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(110)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(70),knows_common|knows_power_strike_4|knows_ironflesh_2|knows_shield_3|knows_athletics_3|knows_power_throw_2,swadian_face_young_1, swadian_face_old_2],
  
  ["swadian_infantry","Polan's Infantry","Polan's Infantry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_pike_b,itm_greatsword_a,itm_poleaxe_b,itm_military_hammer,itm_nobleman_sword_b,itm_nobleman_sword_a,itm_tab_shield_pavise_d,itm_javelin,
    itm_surcoa_over_mail_and_plate_heraldic,itm_brigandine_white_a,itm_brigandine_red_b,itm_lithuanian_ducal_armor,itm_mail_chausses,itm_surcoa_over_mail_and_plate_red,itm_surcoa_over_mail_and_plate_white,itm_rus_cav_boots,itm_hose_kneecops_red,itm_lithuanian_helmet,itm_guard_helmet,itm_novogrod_helmet,itm_hourglass_gloves,itm_hourglass_gauntlets_a],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5|knows_power_throw_3,swadian_face_middle_1, swadian_face_old_2],
 
  ["swadian_pikeman","Polan's Pikeman","Polan's Pikemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_pike_b,itm_nobleman_sword_b,itm_nobleman_sword_a,
    itm_transitional_heraldic,itm_polish_transitional_armor,itm_mail_boots,itm_iron_greaves,itm_sugarloaf_a,itm_klappvisier,itm_hourglass_gauntlets_a,itm_heavy_plate_gloves],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_6|knows_ironflesh_3|knows_athletics_5|knows_power_throw_3,swadian_face_middle_1, swadian_face_old_2],

  ["swadian_sergeant","Polan's Sergeant","Polan's Sergeants",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_danish_greatsword,itm_heavy_great_sword,itm_morningstar,itm_warhammer_b,itm_nobleman_sword_b,itm_nobleman_sword_a,itm_tab_shield_pavise_d,itm_poleaxe_d,itm_one_handed_warhammer,
    itm_transitional_heraldic,itm_polish_transitional_armor,itm_mail_boots,itm_iron_greaves,itm_novogrod_helmet,itm_sugarloaf_a,itm_klappvisier,itm_hourglass_gauntlets_a,itm_heavy_plate_gloves],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7|knows_power_throw_4,swadian_face_middle_1, swadian_face_older_2],
  
  ["swadian_skirmisher","Polan's Skirmisher","Polan's Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_club,itm_sword_medieval_a,itm_mace_2,
    itm_white_kaftan,itm_red_kaftan,itm_lithuanian_shirt,itm_hide_boots,itm_fur_hat,itm_leather_gloves],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(65)|wp_two_handed(20)|wp_polearm(50)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100),knows_common|knows_power_strike_1|knows_ironflesh_1|knows_athletics_3,swadian_face_young_1, swadian_face_middle_2],
  
  ["swadian_crossbowman","Polan's Crossbowman","Polan's Crossbowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_light_crossbow,itm_sword_medieval_b,itm_sword_medieval_a,itm_mace_2,itm_one_handed_war_axe_a,
    itm_red_gambeson,itm_white_gambeson_a,itm_nasal_helmet,itm_mail_coif,itm_leather_boots,itm_ankle_boots,itm_serbian_ankle_boots,itm_leather_gloves,itm_mail_gloves],
   str_12 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5,swadian_face_young_1, swadian_face_old_2],
  
  ["swadian_sharpshooter","Polan's Sharpshooter","Polan's Sharpshooters",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_steel_bolts,itm_crossbow,itm_heavy_crossbow,itm_sword_medieval_b_small,itm_sword_medieval_a,itm_one_handed_warhammer,itm_sarranid_axe_b,
    itm_surcoat_over_mail_heraldic,itm_surcoa_over_mail_and_plate_heraldic,itm_surcoa_over_mail_and_plate_red,itm_surcoa_over_mail_and_plate_white,itm_mail_chausses,itm_kettle_hat_d,itm_mail_gloves,itm_wisby_gloves_black],
   str_13 | agi_12 | int_4 | cha_4|level(19),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6,swadian_face_middle_1, swadian_face_older_2],
  
  ["swadian_man_at_arms","Polan's Man at Arms","Polan's Men at Arms",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_lance,itm_cav_sword,itm_sword_medieval_d_long,itm_lithuanian_shield,itm_military_hammer,itm_javelin,
    itm_lithuanian_ducal_armor,itm_surcoa_over_mail_and_plate_heraldic,itm_mail_and_plate_boots_b,itm_splinted_greaves_spurs,itm_lithuanian_helmet,itm_novogrod_helmet,itm_hourglass_gloves,itm_hourglass_gauntlets_a,itm_hunter,itm_courser],
   str_13 | agi_9 | int_4 | cha_4|level(20),wp_one_handed(120)|wp_two_handed(120)|wp_polearm(120)|wp_archery(10)|wp_crossbow(10)|wp_throwing(90),knows_common|knows_horse_archery_2|knows_power_throw_2|knows_power_strike_3|knows_ironflesh_3|knows_shield_2|knows_athletics_3|knows_riding_5,swadian_face_middle_1, swadian_face_old_2],
 
  ["swadian_knight","Polan's Knight","Polan's Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_heavy_lance,itm_morningstar,itm_sword_medieval_d_long,itm_cav_sword,itm_great_lance,itm_lithuanian_shield,itm_tab_shield_heater_cav_b,
    itm_corrazina_red,itm_churburg_b,itm_mail_and_plate_boots_b,itm_splinted_greaves_spurs,itm_great_helmet,itm_gotland_helmet_c,itm_sugarloaf_a,itm_great_helmet_e,itm_great_helmet_f,itm_plated_charger,itm_charger,itm_warhorse,itm_gilded_hourglass_gloves,itm_hourglass_gauntlets_b],
   str_16 | agi_12 | int_4 | cha_4|level(25),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_throw_3|knows_horse_archery_3|knows_power_strike_5|knows_ironflesh_5|knows_shield_4|knows_athletics_5|knows_riding_7,swadian_face_middle_1, swadian_face_older_2],

  ["swadian_heavy_knight","Polan's Heavy Knight","Polan's Heavy Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_heavy_lance,itm_morningstar,itm_sword_medieval_d_long,itm_cav_sword,itm_great_lance,itm_lithuanian_shield,itm_triangle_shield,itm_tab_shield_heater_cav_b,
    itm_transitional_heraldic,itm_polish_transitional_armor,itm_mail_and_plate_boots_b,itm_splinted_greaves_spurs,itm_sugarloaf_a,itm_gotland_helmet_b,itm_great_helmet_g,itm_gotland_helmet_b,itm_plated_charger,itm_charger,itm_warhorse,itm_gilded_hourglass_gloves,itm_hourglass_gauntlets_b],
   str_19 | agi_15 | int_4 | cha_4|level(29),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(140),knows_common|knows_power_throw_4|knows_horse_archery_4|knows_power_strike_7|knows_ironflesh_7|knows_shield_5|knows_athletics_6|knows_riding_9,swadian_face_young_1, swadian_face_old_2],
 

  ["swadian_heavy_knight_b","Polan's Heavy Knight","Polan's Heavy Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_great_lance,itm_great_lance,itm_great_lance,itm_great_lance,itm_great_lance,itm_tab_shield_heater_cav_b,
    itm_transitional_heraldic,itm_polish_transitional_armor,itm_mail_and_plate_boots_b,itm_splinted_greaves_spurs,itm_sugarloaf_a,itm_gotland_helmet_b,itm_great_helmet_g,itm_gotland_helmet_b,itm_plated_charger,itm_charger,itm_warhorse,itm_gilded_hourglass_gloves,itm_hourglass_gauntlets_b],
   str_19 | agi_15 | int_4 | cha_4|level(29),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_7|knows_ironflesh_7|knows_shield_5|knows_athletics_6|knows_riding_9,swadian_face_young_1, swadian_face_old_2],

  ["polanie_kingsguard","Polan's King's Guard","Polan's King's Guards",tf_guarantee_all_wo_ranged|tf_mounted,0,0,fac_kingdom_1,
   [itm_morningstar,itm_triangle_shield,
    itm_transitional_heraldic,itm_shynbaulds,itm_great_helmet_k,itm_plate_mittens,itm_barded_warhorse],
   str_24 | agi_21 | int_21 | cha_9|level(35),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_archery(150)|wp_crossbow(150)|wp_throwing(150),knows_common|knows_power_throw_5|knows_power_strike_9|knows_ironflesh_10|knows_shield_8|knows_athletics_8|knows_riding_10,swadian_face_young_1, swadian_face_old_2],

   
  ["swadian_messenger","Swadian Messenger","Swadian Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,swadian_face_young_1, swadian_face_old_2],
  ["swadian_deserter","Swadian Deserter","Swadian Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_dagger,itm_club,itm_voulge,itm_wooden_shield,itm_leather_jerkin,itm_padded_cloth,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet],
   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_prison_guard","Prison Guard","Prison Guards",tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_heavy_great_sword,itm_one_handed_warhammer,itm_polish_transitional_armor,itm_iron_greaves,itm_sugarloaf_a,itm_heavy_plate_gloves],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_castle_guard","Castle Guard","Castle Guards",tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_poleaxe_d,itm_cav_sword,itm_polish_transitional_armor,itm_splinted_greaves_spurs,itm_gotland_helmet_b,itm_hourglass_gauntlets_b],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

# Vaegir watchman?	12
  ["vaegir_recruit","Grey Recruit","Grey Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_scythe,itm_hatchet,itm_cudgel,itm_axe,itm_stones,itm_arena_shield_red,itm_arena_shield_blue,itm_arena_shield_green,itm_arena_shield_yellow,
    itm_tunic_with_green_cape, itm_linen_tunic,itm_wrapping_boots,itm_felt_hat,itm_woolen_cap],
   str_7 | agi_5 | int_4 | cha_4|level(4),wp(60),knows_common, vaegir_face_younger_1, vaegir_face_middle_2],
 
  ["vaegir_footman","Grey Footman","Grey Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_spear,itm_mace_2,itm_one_handed_war_axe_a,itm_axe,itm_javelin,
    itm_skullcap,itm_nasal_helmet,itm_ragged_outfit,itm_nomad_armor,itm_wrapping_boots,itm_hide_boots],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(10)|wp_throwing(60),knows_common|knows_power_throw_1|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1, vaegir_face_young_1, vaegir_face_middle_2],

  ["vaegir_veteran","Grey Veteran","Grey Veterans",tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_one_handed_war_axe_a,itm_scimitar,itm_spear,itm_tab_shield_kite_cav_a,itm_iberian_mace,itm_javelin,
    itm_nasal_helmet,itm_nasal_helmet,itm_mail_shirt_with_fur,itm_byrnie,itm_nasal_helmet,itm_mail_coif_d,itm_rus_cav_boots,itm_leather_boots,itm_leather_gloves],
   str_12 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(110)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(80),knows_common|knows_power_strike_5|knows_ironflesh_2|knows_shield_2|knows_athletics_3|knows_power_throw_2,vaegir_face_young_1, vaegir_face_old_2],
 
  ["vaegir_infantry","Grey Infantry","Grey Infantries",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_sword_medieval_d_long,itm_scimitar_b,itm_pike_b,itm_one_handed_bar_mace,itm_morningstar,itm_celtic_axe,itm_longsword,itm_bec_de_corbin_a,itm_steel_pick,itm_tab_shield_kite_cav_b,itm_long_bardiche,itm_javelin,
    itm_kuyak_a,itm_kuyak_b,itm_norman_helmet_b,itm_norman_helmet_c,itm_norman_helmet_d,itm_pronoia_helmet,itm_rus_cav_boots,itm_mail_gloves,itm_gilded_hourglass_gloves],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_7|knows_ironflesh_3|knows_shield_4|knows_athletics_5|knows_power_throw_3,vaegir_face_young_1, vaegir_face_older_2],
  
  ["vaegir_pikeman","Grey Pikeman","Grey Pikemen",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_pike_b,itm_pike_b,itm_pike_b,itm_scimitar_b,
    itm_norman_helmet_b,itm_norman_helmet_c,itm_norman_helmet_d,itm_kuyak_a,itm_kuyak_b,itm_rus_cav_boots,itm_mail_gloves,itm_gilded_hourglass_gloves],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_polearm(190)|wp_one_handed(140)|wp_two_handed(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_strike_9|knows_ironflesh_5|knows_athletics_7|knows_power_throw_4,vaegir_face_young_1, vaegir_face_older_2],
  
  ["vaegir_guard","Grey Guard","Grey Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_scimitar_b,itm_steel_pick,itm_danish_greatsword,itm_warhammer,itm_morningstar,itm_long_maul,itm_poleaxe_d,itm_pike_b,itm_tab_shield_kite_cav_b,itm_great_long_bardiche,itm_one_handed_warhammer,itm_bec_de_corbin_a,
    itm_transitional_heraldic,itm_milanese_armour,itm_milanese_sallet,itm_sugarloaf_a,itm_iron_greaves,itm_hourglass_gauntlets_b],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(140),knows_common|knows_power_strike_9|knows_ironflesh_5|knows_shield_5|knows_athletics_7|knows_power_throw_5,vaegir_face_middle_1, vaegir_face_older_2],
  
  ["vaegir_skirmisher","Grey Skirmisher","Grey Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_arrows,itm_hunting_bow,itm_short_bow,itm_mace_2,itm_one_handed_war_axe_a,
    itm_tunic_with_green_cape,itm_linen_tunic,itm_wrapping_boots,itm_felt_hat,itm_woolen_cap],
   str_9 | agi_7 | int_4 | cha_4|level(14),wp_one_handed(65)|wp_two_handed(20)|wp_polearm(50)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100),knows_common|knows_power_strike_1|knows_ironflesh_1|knows_athletics_3|knows_power_draw_1,vaegir_face_young_1, vaegir_face_old_2],
  
  ["vaegir_crossbowman","Grey Crossbowman","Grey Crossbowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_heavy_crossbow,itm_light_crossbow,itm_steel_bolts,itm_one_handed_war_axe_a,itm_mace_2,
    itm_tribal_warrior_outfit,itm_wrapping_boots,itm_rus_cav_boots,itm_nasal_helmet,itm_norman_helmet_d],
   str_13 | agi_9 | int_4 | cha_4|level(19),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5, vaegir_face_old_2],
  
  ["vaegir_archer","Grey Archer","Grey Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_war_bow,itm_bodkin_arrows,itm_one_handed_war_axe_a,itm_mace_2,
    itm_skullcap,itm_nasal_helmet,itm_coarse_tunic,itm_nomad_armor,itm_wrapping_boots,itm_hide_boots],
   str_11 | agi_9 | int_4 | cha_4|level(19),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5|knows_power_draw_3, vaegir_face_older_2],
  
  ["vaegir_marksman","Grey Marksman","Grey Marksmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_long_bow,itm_war_bow,itm_bodkin_arrows,itm_scimitar,itm_mace_2,itm_one_handed_war_axe_a,
    itm_tribal_warrior_outfit,itm_wrapping_boots,itm_rus_cav_boots,itm_nasal_helmet,itm_norman_helmet_d],
   str_13 | agi_12 | int_4 | cha_4|level(24),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6|knows_power_draw_4,vaegir_face_young_1, vaegir_face_older_2],
  
  ["vaegir_horseman","Grey Horseman","Grey Horsemen",tf_mounted|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_lance,itm_scimitar_b,itm_sword_medieval_d_long,itm_tab_shield_kite_cav_b,itm_javelin,
    itm_kuyak_a,itm_kuyak_b,itm_norman_helmet_b,itm_norman_helmet_c,itm_norman_helmet_d,itm_pronoia_helmet,itm_rus_cav_boots,itm_mail_gloves,itm_gilded_hourglass_gloves,itm_saddle_horse,itm_courser],
   str_12 | agi_9 | int_4 | cha_4|level(24),wp_one_handed(120)|wp_two_handed(120)|wp_polearm(120)|wp_archery(10)|wp_crossbow(10)|wp_throwing(80),knows_common|knows_horse_archery_2|knows_power_throw_2|knows_power_strike_3|knows_ironflesh_3|knows_shield_2|knows_athletics_3|knows_riding_4,vaegir_face_young_1, vaegir_face_older_2],
  
  ["vaegir_knight","Grey Knight","Grey Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_heavy_lance,itm_lance,itm_scimitar_b,itm_sword_medieval_d_long,itm_tab_shield_kite_cav_b,
    itm_transitional_heraldic,itm_milanese_armour,itm_milanese_sallet,itm_sugarloaf_a,itm_iron_greaves,itm_hourglass_gauntlets_b,itm_warhorse_b,itm_hunter],
   str_15 | agi_12 | int_4 | cha_4|level(29),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_archery(10)|wp_crossbow(10)|wp_throwing(110),knows_common|knows_power_throw_4|knows_horse_archery_3|knows_power_strike_5|knows_ironflesh_4|knows_shield_4|knows_athletics_5|knows_riding_6,vaegir_face_middle_1, vaegir_face_older_2],

  ["vaegir_messenger","Grey Messenger","Grey Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_2,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_deserter","Grey Deserter","Grey Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_scimitar_b,itm_sword_medieval_d_long,itm_tab_shield_kite_cav_b,
    itm_milanese_armour,itm_milanese_sallet,itm_iron_greaves,itm_hourglass_gauntlets_b  ],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_scimitar_b,itm_sword_medieval_d_long,itm_tab_shield_kite_cav_b,
    itm_milanese_armour,itm_milanese_sallet,itm_iron_greaves,itm_hourglass_gauntlets_b],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],

  ["dynior","Danior the Grey","Daniory the Grey",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_sword_viking_a_long,itm_tab_shield_small_round_c,
    itm_kuyak_a,itm_rus_cav_boots,itm_pronoia_helmet,itm_mail_gauntlets],
   def_attrib|level(40),wp_melee(530),knows_riding_2|knows_athletics_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_10,vaegir_face_middle_1, vaegir_face_older_2],
  
  ["grey_kingsguard","Grey King's Guard","Grey King's Guards", tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_steel_pick,itm_tab_shield_heater_cav_b,
    itm_milanese_armour,itm_milanese_sallet,itm_iron_greaves,itm_hourglass_gauntlets_b],
   str_24 | agi_21 | int_21 | cha_9|level(35),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_archery(150)|wp_crossbow(150)|wp_throwing(150),knows_common|knows_power_throw_5|knows_power_strike_9|knows_ironflesh_10|knows_shield_8|knows_athletics_8|knows_riding_10,swadian_face_young_1, swadian_face_old_2],
 

 
##################  Khergits			12		
##### Golden Horde Helmet		Crested Boerk with Plume		Crested Boerk		Boerk
#	Crested Solak Helmet with Plume		Crested Solak Helmet		Solak Helmet
# 		https://www.google.com.tr/search?q=topkap%C4%B1+silah+koleksiyonu&biw=1366&bih=643&source=lnms&tbm=isch&sa=X&ved=0CAYQ_AUoAWoVChMI4_P6y6TryAIV4_ByCh2uJAvf
   
#  coursers rounceys and war horse for lord only

	################ WARRIORS OF TENGRI 12

  ["khergit_tribesman","Tribesman of Tengri","Tribesmen of Tengri",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_3,
   [itm_cudgel,itm_spiked_club,itm_tab_shield_kite_a,
    itm_deli_cap,itm_sarranid_cloth_robe,itm_saracen_shirt_a,itm_deli_robe_b,itm_turkish_shoes,itm_nomad_boots],
   str_7 | agi_5 | int_4 | cha_4|level(4),wp(60),knows_common,khergit_face_younger_1, khergit_face_old_2],
 
  ["khergit_footman","Footman of Tengri","Footmen of Tengri",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_arabian_sword_a,itm_spiked_mace,itm_sarranid_mace_1,itm_tab_shield_kite_b,itm_two_handed_axe,itm_javelin,
    itm_kazakh_hat,itm_solak_helmet_a,itm_kazakh_outfit,itm_skirmisher_armor,itm_kazakh_boots,itm_leather_gloves],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(10)|wp_throwing(60),knows_common|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1|knows_power_throw_1,khergit_face_younger_1, khergit_face_old_2],
  
  ["khergit_warrior","Warrior of Tengri","Warriors of Tengri",tf_guarantee_armors|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_arabian_sword_b,itm_scimitar,itm_sarranid_two_handed_axe_b,itm_sarranid_mace_1,itm_sarranid_axe_a,itm_hafted_blade_b,itm_tab_shield_kite_c,itm_tab_shield_kite_d,itm_two_handed_battle_axe_2,itm_ashwood_pike,itm_jarid,itm_javelin,
    itm_sarranid_horseman_helmet,itm_saracen_helmet_a,itm_saracen_helmet_b,itm_deli_robe,itm_sarranid_leather_armor,itm_sarranid_boots_b,itm_nomad_boots,itm_leather_gloves],
   str_12 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(110)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_4|knows_ironflesh_2|knows_shield_2|knows_athletics_3|knows_power_throw_3,khergit_face_younger_1, khergit_face_old_2],
 
  ["khergit_veteran_warrior","Veteran Warrior of Tengri","Warriors of Tengri",tf_guarantee_armors|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_arabian_sword_d,itm_scimitar_b,itm_sarranid_two_handed_axe_a,itm_sarranid_two_handed_mace_1,itm_sarranid_axe_b,itm_hafted_blade_a,itm_plate_covered_round_shield,itm_tab_shield_kite_d,itm_ashwood_pike,itm_jarid,
    itm_ghulam_helmet_a,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_saracen_mail_c,itm_saracen_mail_b,itm_saracen_mail_a,itm_sarranid_boots_d,itm_sarranid_boots_c,itm_lamellar_gauntlets,itm_scale_gloves_a],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5|knows_power_throw_5,khergit_face_young_1, khergit_face_older_2],

  ["khergit_veteran_horse_archer","Elite Warrior of Tengri","Elite Warrior of Tengri",tf_guarantee_armors|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_scimitar_b,itm_sarranid_two_handed_axe_a,itm_tab_shield_small_round_c,itm_arabian_sword_d,
    itm_ottoman_chichak,itm_ottoman_elite_cavalry_chichak,itm_sarranid_elite_armor,itm_heavy_yawshan,itm_sarranid_boots_c,itm_scale_gauntlets,itm_scale_gloves_a],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7,khergit_face_middle_1, khergit_face_older_2],

  ["khergit_skirmisher","Skirmisher of Tengri","Skirmishers of Tengri",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_arabian_sword_a,itm_hunting_bow,itm_arrows,
    itm_sarranid_felt_hat,itm_turban,itm_turban_b,itm_saracen_shirt_c,itm_saracen_shirt_b,itm_skirmisher_armor,itm_sarranid_boots_a,itm_turkish_shoes,itm_nomad_boots],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(65)|wp_two_handed(20)|wp_polearm(50)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100),knows_common|knows_power_strike_1|knows_ironflesh_1|knows_athletics_3|knows_power_draw_1,khergit_face_younger_1, khergit_face_old_2],
  
  ["khergit_archer","Archer of Tengri","Archers of Tengri",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_short_bow,itm_nomad_bow,itm_arrows,itm_bodkin_arrows,itm_scimitar,itm_sarranid_mace_1,itm_spiked_mace,
    itm_janissary_boerk_a,itm_janissary_boerk_b,itm_janissary_boerk_c,itm_archers_vest,itm_skirmisher_armor,itm_turkish_shoes,itm_sarranid_boots_a,itm_leather_gloves],
   str_11 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5|knows_power_draw_3, khergit_face_young_1, khergit_face_older_2],
 
  ["khergit_veteran_archer","Veteran Archer of Tengri","Veteran Archers of Tengri",tf_guarantee_range,0,0,fac_kingdom_3,
   [itm_khergit_bow,itm_bodkin_arrows,itm_arrows,itm_strong_bow,itm_scimitar_b,itm_arabian_sword_b,itm_sarranid_mace_1,
    itm_janissary_boerk_b,itm_janissary_boerk_a,itm_janissary_boerk_c,itm_sarranid_leather_armor,itm_deli_robe,itm_khergit_leather_boots,itm_leather_gloves],
   str_13 | agi_12 | int_4 | cha_4|level(19),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6|knows_power_draw_4,khergit_face_middle_1, khergit_face_older_2],
  
  ["khergit_horse_archer","Elite Archer of Tengri","Elite Archers of Tengri",tf_guarantee_range,0,0,fac_kingdom_3,
   [itm_khergit_bow,itm_bodkin_arrows,itm_arrows,itm_strong_bow,itm_scimitar_b,itm_arabian_sword_b,itm_sarranid_mace_1,
    itm_janissary_boerk_c,itm_janissary_boerk_b,itm_janissary_boerk_a,itm_saracen_mail_c,itm_saracen_mail_b,itm_saracen_mail_a,itm_sarranid_boots_d,itm_sarranid_boots_c,itm_lamellar_gauntlets,itm_scale_gloves_a],
   str_15 | agi_15 | int_4 | cha_4|level(24),wp_one_handed(95)|wp_two_handed(50)|wp_polearm(80)|wp_archery(180)|wp_crossbow(180)|wp_throwing(180),knows_common|knows_power_strike_2|knows_ironflesh_5|knows_athletics_7|knows_power_draw_6, khergit_face_young_1, khergit_face_older_2],

  ["khergit_horseman","Horseman of Tengri","Horsemen of Tengri",tf_mounted|tf_guarantee_armors|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_lance,itm_arabian_sword_b,itm_scimitar,itm_two_handed_axe,itm_two_handed_battle_axe_2,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_javelin,
    itm_saracen_helmet_c, itm_ghulam_helmet_a,itm_saracen_lamellar_a,itm_sarranid_cavalry_robe,itm_arabian_armor_a2,itm_sarranid_boots_c,itm_sarranid_boots_d,itm_scale_gloves_a,itm_saddle_horse,itm_courser],
   str_12 | agi_9 | int_4 | cha_4|level(15),wp_one_handed(120)|wp_two_handed(120)|wp_polearm(120)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_3|knows_ironflesh_3|knows_shield_2|knows_athletics_3|knows_riding_3|knows_power_throw_2|knows_horse_archery_2,khergit_face_young_1, khergit_face_older_2],
  
  ["khergit_lancer","Lancer of Tengri","Lancers of Tengri",tf_mounted|tf_guarantee_armors|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_heavy_lance,itm_arabian_sword_d,itm_scimitar_b,itm_sarranid_two_handed_axe_b,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_jarid,
    itm_saracen_helmet_b,itm_saracen_helmet_d,itm_mamluke_mail,itm_sipahi_jawshan,itm_sarranid_boots_c,itm_sarranid_boots_d,itm_scale_gauntlets,itm_scale_gloves_a,itm_warhorse_b,itm_courser],
   str_15 | agi_12 | int_4 | cha_4|level(21),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_throw_3|knows_horse_archery_3|knows_power_strike_5|knows_ironflesh_4|knows_shield_4|knows_athletics_5|knows_riding_5|knows_power_throw_3,khergit_face_middle_1, khergit_face_older_2],
 
  ["khergit_heavy_lancer","Heavy Lancer of Tengri","Heavy Lancers of Tengri",tf_mounted|tf_guarantee_armors|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_heavy_lance,itm_sarranid_cavalry_sword,itm_scimitar_b,itm_sarranid_two_handed_axe_a,itm_tab_shield_small_round_c,
    itm_ottoman_chichak,itm_ottoman_elite_cavalry_chichak,itm_sarranid_elite_armor,itm_heavy_yawshan,itm_sarranid_boots_c,itm_scale_gauntlets,itm_scale_gloves_a,itm_warhorse_b,itm_courser],
   str_18 | agi_15 | int_4 | cha_4|level(27),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(140),knows_common|knows_power_throw_5|knows_horse_archery_4|knows_power_strike_7|knows_ironflesh_6|knows_shield_5|knows_athletics_6|knows_riding_7,khergit_face_middle_1, khergit_face_older_2],

  ["khergit_messenger","Messenger of Tengri","Messengers of Tengri",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_2,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(125),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,khergit_face_young_1, khergit_face_older_2],
  ["khergit_deserter","Deserter of Tengri","Deserters of Tengri",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_sword_khergit_1,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap_b,itm_khergit_armor,itm_steppe_armor,itm_tribal_warrior_outfit,itm_nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,khergit_face_young_1, khergit_face_older_2],
  ["khergit_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_scimitar_b,itm_shield_heater_d,
    itm_ottoman_chichak,itm_ottoman_elite_cavalry_chichak,itm_sarranid_elite_armor,itm_heavy_yawshan,itm_sarranid_boots_c,itm_scale_gauntlets,itm_scale_gloves_a,itm_warhorse_sarranid,itm_arabian_horse_b],
   def_attrib|level(24),wp(130),knows_athletics_5|knows_shield_2|knows_ironflesh_5,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_scimitar_b,itm_shield_heater_d,
    itm_ottoman_chichak,itm_ottoman_elite_cavalry_chichak,itm_sarranid_elite_armor,itm_heavy_yawshan,itm_sarranid_boots_c,itm_scale_gauntlets,itm_scale_gloves_a],
   def_attrib|level(24),wp(130),knows_athletics_5|knows_shield_2|knows_ironflesh_5,khergit_face_middle_1, khergit_face_older_2],

  ["tengri_kingsguard","Tengri King's Guard","Tengri King's Guards",tf_guarantee_all_wo_ranged|tf_mounted,0,0,fac_kingdom_3,
   [itm_heavy_lance,itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c,
    itm_ottoman_elite_cavalry_chichak,itm_heavy_yawshan,itm_sarranid_boots_c,itm_scale_gauntlets,itm_courser],
   str_24 | agi_21 | int_21 | cha_9|level(35),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_archery(150)|wp_crossbow(150)|wp_throwing(150),knows_common|knows_power_throw_5|knows_power_strike_9|knows_ironflesh_10|knows_shield_8|knows_athletics_8|knows_riding_10,swadian_face_young_1, swadian_face_old_2],

 #nords					12
   
  ["nord_recruit","Kalmarunionen Recruit","Kalmarunionen Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_axe,itm_hatchet,itm_spear,itm_wooden_shield,itm_club,
    itm_red_tunic,itm_coarse_tunic,itm_hide_boots,itm_nomad_boots],
   str_8 | agi_5 | int_4 | cha_4|level(4),wp(60),knows_common,nord_face_younger_1, nord_face_old_2],
  
  ["nord_footman","Kalmarunionen Footman","Kalmarunionen Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_4,
   [itm_falchion,itm_sword_viking_1,itm_sword_viking_2_small,itm_long_axe,itm_two_handed_axe,itm_voulge_new,itm_nordic_shield,itm_wooden_shield,itm_javelin,
    itm_leather_cap,itm_skullcap,itm_leather_scale_armor,itm_peltastos_armor,itm_leather_boots,itm_nomad_boots,itm_leather_gloves],
   str_12 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(10)|wp_throwing(60),knows_common|knows_power_throw_1|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1,nord_face_young_1, nord_face_old_2],
  
  ["nord_trained_footman","Kalmarunionen Trained Footman","Kalmarunionen Trained Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_long_axe_b,itm_military_cleaver_b,itm_two_handed_battle_axe_2,itm_sledgehammer,itm_ashwood_pike,itm_plate_covered_round_shield,itm_round_shield,itm_javelin,
    itm_kettle_hat_f,itm_kettle_hat_e,itm_brigandine_red_c,itm_brigandine_yellow_a,itm_brigandine_blue_a,itm_chapel_de_fer_d,itm_brigandine_blue,itm_brigandine_yellow,itm_brigandine_red_b,itm_hose_kneecops_red,itm_hose_kneecops_green,itm_wisby_gloves_red,itm_wisby_gauntlets_red],
   str_16 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(110)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_throw_2|knows_power_strike_4|knows_ironflesh_2|knows_shield_2|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  
  ["nord_warrior","Kalmarunionen Warrior","Kalmarunionen Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_danish_greatsword,itm_military_cleaver_c,itm_sword_viking_3,itm_military_hammer,itm_great_axe,itm_warhammer,itm_flambard_a,itm_long_axe_c,itm_long_axe_b,itm_bec_de_corbin_a,itm_plate_covered_round_shield,itm_throwing_spears,
    itm_morion_a,itm_morion_b,itm_black_armor_b,itm_black_armor_c,itm_splinted_greaves_spurs,itm_plate_boots,itm_wisby_gloves,itm_bnw_gauntlets],
   str_18 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_throw_3|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_power_throw_4|knows_athletics_5,nord_face_young_1, nord_face_older_2],
  
  ["nord_veteran","Kalmarunionen Pikeman","Kalmarunionen Pikemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_pike,itm_awlpike,itm_military_hammer,itm_glaive2,
    itm_morion_a,itm_morion_b,itm_black_armor_b,itm_black_armor_c,itm_splinted_greaves_spurs,itm_plate_boots,itm_wisby_gloves,itm_bnw_gauntlets],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_throw_3|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5,nord_face_young_1, nord_face_older_2],
  
  ["nord_champion","Kalmarunionen Veteran Pikeman","Kalmarunionen Veteran Pikemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_pike,itm_awlpike,itm_pike_b,itm_military_hammer,itm_glaive2,
    itm_great_bascinet_a,itm_plate_armor_c,itm_morion_a,itm_corrazina_grey,itm_plate_boots,itm_hourglass_gauntlets_a],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(140),knows_common|knows_power_throw_4|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7,nord_face_middle_1, nord_face_older_2],
 
  ["nord_huntsman","Kalmarunionen Huntsman","Kalmarunionen Huntsmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_arrows,itm_short_bow,itm_hunting_bow,itm_falchion,
    itm_rawhide_coat,itm_hide_boots],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(65)|wp_two_handed(20)|wp_polearm(50)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100),knows_common|knows_power_strike_1|knows_ironflesh_1|knows_athletics_3|knows_power_draw_1,nord_face_young_1, nord_face_old_2],
 
  ["nord_crossboman","Kalmarunionen Crossbowman","Kalmarunionen Crossbowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_heavy_crossbow,itm_light_crossbow,itm_steel_bolts,itm_bolts,itm_mace_4,itm_sword_viking_1,itm_sword_viking_2_small,
    itm_nordic_veteran_archer_helmet,itm_nordic_archer_helmet,itm_peltastos_armor,itm_leather_scale_armor,itm_hide_boots,itm_leather_gloves],
   str_13 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5,nord_face_young_1, nord_face_old_2],
  
  ["nord_archer","Kalmarunionen Archer","Kalmarunionen Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_khergit_arrows,itm_short_bow,itm_long_bow,itm_bodkin_arrows,itm_mace_4,itm_sword_viking_1,itm_sword_viking_2_small,
    itm_nordic_veteran_archer_helmet,itm_nordic_archer_helmet,itm_peltastos_armor,itm_leather_scale_armor,itm_hide_boots,itm_leather_gloves],
   str_11 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5|knows_power_draw_3,nord_face_young_1, nord_face_old_2],
  
  ["nord_veteran_archer","Kalmarunionen Veteran Archer","Kalmarunionen Veteran Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_bodkin_arrows,itm_khergit_arrows,itm_military_hammer,itm_military_cleaver_b,itm_long_bow,itm_sword_viking_1,itm_sword_viking_2_small,
    itm_chapel_de_fer_a,itm_byrnja,itm_byrnie,itm_leather_boots,itm_leather_gloves],
   str_13 | agi_12 | int_4 | cha_4|level(21),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6|knows_power_draw_4,nord_face_middle_1, nord_face_older_2],
  
  ["nord_horseman","Kalmarunionen Horseman","Kalmarunionen Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_lance,itm_sword_viking_c_long,itm_sword_viking_a_long,itm_plate_covered_round_shield,itm_tab_shield_heater_cav_a,itm_throwing_spears,
    itm_great_helmet_i,itm_great_helmet_h,itm_great_helmet_d,itm_topfhelm_f,itm_surcoa_over_mail_and_plate_blue,itm_wisby_gloves,itm_surcoat_over_mail_blue,itm_splinted_greaves_spurs,itm_hourglass_gauntlets_a,itm_saddle_horse,itm_courser,],
   str_12 | agi_9 | int_4 | cha_4|level(17),wp_one_handed(120)|wp_two_handed(120)|wp_polearm(120)|wp_archery(10)|wp_crossbow(10)|wp_throwing(90),knows_common|knows_power_strike_3|knows_power_throw_3|knows_horse_archery_2|knows_horse_archery_2|knows_ironflesh_3|knows_shield_2|knows_athletics_3|knows_riding_3,nord_face_young_1, nord_face_older_2],
  
  ["nord_knight","Kalmarunionen Knight","Kalmarunionen Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_lance,itm_heavy_lance,itm_nordic_nobleman_sword,itm_sword_viking_a_long,itm_plate_covered_round_shield,itm_tab_shield_heater_cav_b,
    itm_pigface_klappvisier,itm_corrazina_grey,itm_great_bascinet_a,itm_plate_armor_c,itm_plate_boots,itm_splinted_greaves_spurs,itm_hourglass_gauntlets_a,itm_warhorse_b,itm_hunter],
   str_15 | agi_12 | int_4 | cha_4|level(24),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_archery(10)|wp_crossbow(10)|wp_throwing(110),knows_common|knows_power_throw_4|knows_horse_archery_3|knows_power_strike_5|knows_ironflesh_4|knows_shield_4|knows_athletics_5|knows_riding_5,nord_face_middle_1, nord_face_older_2],

   
   
  ["nord_messenger","Kalmarunionen Messenger","Kalmarunionen Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,nord_face_young_1, nord_face_older_2],
  
  ["nord_deserter","Kalmarunionen Deserter","Kalmarunionen Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,nord_face_young_1, nord_face_older_2],
  
  ["nord_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_nordic_nobleman_sword,itm_plate_covered_round_shield,
    itm_great_bascinet_a,itm_morion_a,itm_corrazina_grey,itm_plate_armor_c,itm_plate_boots,itm_hourglass_gauntlets_a],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1, nord_face_older_2],
  
  ["nord_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_nordic_nobleman_sword,itm_plate_covered_round_shield,
    itm_great_bascinet_a,itm_morion_a,itm_corrazina_grey,itm_plate_armor_c,itm_plate_boots,itm_hourglass_gauntlets_a],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1, nord_face_older_2],
 
  ["kalmarunionen_kingsguard","Kalmarunionen King's Guard","Kalmarunionen King's Guards",tf_guarantee_all_wo_ranged|tf_mounted,0,0,fac_kingdom_2,
   [itm_heavy_lance,itm_sword_viking_c_long,itm_plate_covered_round_shield,
    itm_great_bascinet_a,itm_plate_armor_c,itm_plate_boots,itm_hourglass_gauntlets_a,itm_hunter],
   str_24 | agi_21 | int_21 | cha_9|level(35),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_archery(150)|wp_crossbow(150)|wp_throwing(150),knows_common|knows_power_throw_5|knows_power_strike_9|knows_ironflesh_10|knows_shield_8|knows_athletics_8|knows_riding_10,swadian_face_young_1, swadian_face_old_2],

 

  #Rhodoks 				12
   
  ["rhodok_tribesman","Druzhina Tribesman","Druzhina Tribesmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_scythe,itm_club,itm_tab_shield_kite_a,
    itm_short_tunic,itm_fur_coat,itm_rus_shoes,itm_wrapping_boots,itm_fur_hat,itm_nomad_cap],
   str_7 | agi_5 | int_4 | cha_4|level(4),wp(60),knows_common,vaegir_face_younger_1, vaegir_face_old_2],

  ["rhodok_spearman","Druzhina Footman","Druzhina Footmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_spiked_club,itm_spear,itm_tab_shield_kite_a,itm_javelin,
    itm_steppe_cap,itm_vaegir_fur_cap,itm_nomad_vest,itm_drz_kaftan,itm_rus_shoes,itm_nomad_boots],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(10)|wp_throwing(60),knows_common|knows_power_throw_1|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1,vaegir_face_young_1, vaegir_face_old_2],
  
  ["rhodok_trained_spearman","Druzhina Trained Footman","Druzhina Trained Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_scimitar,itm_bardiche,itm_war_spear,itm_tab_shield_kite_b,itm_mace_4,itm_one_handed_war_axe_a,itm_javelin,
    itm_rus_helmet_b,itm_tagancha_helmet_a,itm_drz_mail_shirt,itm_kuyak_a,itm_rus_cav_boots,itm_mail_gloves,itm_mail_gauntlets],
   str_12 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(110)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_4|knows_ironflesh_2|knows_shield_2|knows_athletics_3|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2],
  
  ["rhodok_veteran_spearman","Druzhina Veteran Footman","Druzhina Veteran Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_scimitar_b,itm_military_hammer,itm_bardiche,itm_maul,itm_long_bardiche,itm_pike,itm_tab_shield_kite_c,itm_javelin,
    itm_nikolskoe_helmet,itm_tagancha_helmet_b,itm_drz_lamellar_armor,itm_gnezdovo_helmet,itm_drz_lamellar_armor_a,itm_drz_lamellar_armor_a,itm_rus_cav_boots,itm_hourglass_gloves,itm_gilded_hourglass_gloves],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5|knows_power_throw_3,vaegir_face_young_1, vaegir_face_older_2],
  
  ["rhodok_sergeant","Druzhina Sergeant","Druzhina Sergeants",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_scimitar_b,itm_one_handed_warhammer,itm_steel_pick,itm_warhammer,itm_danish_greatsword,itm_longsword,itm_great_bardiche,itm_awlpike,itm_bec_de_corbin_a,itm_great_long_bardiche,itm_pike_b,itm_tab_shield_kite_d,
    itm_nikolskoe_helmet,itm_litchina_helmet,itm_drz_elite_lamellar_armor,itm_rus_scale,itm_rus_scale_b,itm_rus_scale_c,itm_rus_scale_d,itm_rus_splint_greaves,itm_rus_cav_boots,itm_hourglass_gauntlets_a,itm_hourglass_gauntlets_b],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(140),knows_common|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7|knows_power_throw_4,vaegir_face_middle_1, vaegir_face_older_2],
  
  ["rhodok_crossbowman","Druzhina Archer","Druzhina Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_5,
   [itm_one_handed_war_axe_a,itm_hunting_bow,itm_arrows,
    itm_short_tunic,itm_fur_coat,itm_rus_shoes,itm_wrapping_boots,itm_fur_hat,itm_nomad_cap],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(65)|wp_two_handed(20)|wp_polearm(50)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100),knows_common|knows_power_strike_1|knows_ironflesh_1|knows_athletics_3|knows_power_draw_1,vaegir_face_young_1, vaegir_face_older_2],
  
  ["rhodok_trained_crossbowman","Druzhina Trained Archer","Druzhina Trained Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_arrows,itm_short_bow,itm_hunting_bow,itm_one_handed_war_axe_a,itm_arrows,itm_bodkin_arrows,
    itm_steppe_cap,itm_vaegir_fur_cap,itm_nomad_vest,itm_drz_kaftan,itm_rus_shoes,itm_nomad_boots],
   str_11 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5|knows_power_draw_3,vaegir_face_young_1, vaegir_face_older_2],
  
  ["rhodok_veteran_crossbowman","Druzhina Veteran Archer","Druzhina Veteran Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_nomad_bow,itm_war_bow,itm_scimitar,itm_mace_4,itm_one_handed_war_axe_a,itm_arrows,itm_bodkin_arrows,
    itm_rus_helmet_b,itm_vaegir_lamellar_helmet,itm_tribal_warrior_outfit,itm_rus_cav_boots,itm_mail_gloves,itm_mail_gauntlets],
   str_13 | agi_12 | int_4 | cha_4|level(19),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6|knows_power_draw_4,vaegir_face_middle_1, vaegir_face_older_2],
  
  ["rhodok_sharpshooter","Druzhina Elite Archer","Druzhina Elite Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_war_bow,itm_scimitar_b,itm_military_hammer,itm_arrows,itm_bodkin_arrows,
    itm_rus_helmet_b,itm_tagancha_helmet_a,itm_drz_mail_shirt,itm_rus_cav_boots,itm_mail_gloves,itm_mail_gauntlets],
   str_15 | agi_15 | int_4 | cha_4|level(24),wp_one_handed(95)|wp_two_handed(50)|wp_polearm(80)|wp_archery(180)|wp_crossbow(180)|wp_throwing(180),knows_common|knows_power_strike_2|knows_ironflesh_5|knows_athletics_7|knows_power_draw_6,vaegir_face_middle_1, vaegir_face_older_2],
  
  ["rhodok_horseman","Druzhina Horseman","Druzhina Horsemen",tf_mounted|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_scimitar,itm_spear,itm_tab_shield_kite_cav_a,itm_javelin,
    itm_rus_helmet_b,itm_tagancha_helmet_a,itm_drz_mail_shirt,itm_rus_cav_boots,itm_mail_gloves,itm_mail_gauntlets,itm_saddle_horse,itm_rus_horse],
   str_12 | agi_9 | int_4 | cha_4|level(19),wp_one_handed(120)|wp_two_handed(120)|wp_polearm(120)|wp_archery(10)|wp_crossbow(10)|wp_throwing(80),knows_common|knows_horse_archery_2|knows_power_throw_2|knows_power_strike_3|knows_ironflesh_3|knows_shield_2|knows_athletics_3|knows_riding_3,vaegir_face_young_1, vaegir_face_older_2],

  ["rhodok_veteran_horseman","Druzhina Veteran Horseman","Druzhina Veteran Horsemen",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_lance,itm_scimitar,itm_bardiche,itm_tab_shield_kite_cav_a,itm_javelin,
    itm_rus_helmet_b,itm_tagancha_helmet_a,itm_kuyak_a,itm_rus_cav_boots,itm_mail_gloves,itm_mail_gauntlets,itm_saddle_horse,itm_rus_horse],
   str_15 | agi_12 | int_4 | cha_4|level(24),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_archery(10)|wp_crossbow(10)|wp_throwing(110),knows_common|knows_horse_archery_3|knows_power_throw_4|knows_power_strike_5|knows_ironflesh_4|knows_shield_4|knows_athletics_5|knows_riding_5,vaegir_face_middle_1, vaegir_face_older_2],
   
  ["rhodok_knight","Druzhina Knight","Druzhina Knights",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_heavy_lance,itm_scimitar_b,itm_longsword,itm_bardiche,itm_tab_shield_kite_cav_b,
    itm_tagancha_helmet_b,itm_litchina_helmet,itm_rus_scale,itm_rus_scale_b,itm_rus_scale_c,itm_rus_scale_d,itm_rus_splint_greaves,itm_rus_cav_boots,itm_hourglass_gauntlets_a,itm_hourglass_gauntlets_b,itm_warhorse_b,itm_hunter,itm_courser,],
   str_18 | agi_15 | int_4 | cha_4|level(29),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(130),knows_common|knows_power_throw_5|knows_horse_archery_4|knows_power_strike_7|knows_ironflesh_6|knows_shield_5|knows_athletics_6|knows_riding_7,vaegir_face_middle_1, vaegir_face_older_2],

  ["rhodok_messenger","Druzhina Messenger","Druzhina Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_5,
   [itm_scimitar,itm_bardiche,itm_maul,itm_war_spear,itm_tab_shield_kite_b,itm_mace_4,itm_one_handed_war_axe_a,
    itm_rus_helmet_b,itm_vaegir_lamellar_helmet,itm_drz_mail_shirt,itm_kuyak_a,itm_rus_cav_boots,itm_mail_gloves,itm_mail_gauntlets],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,vaegir_face_middle_1, vaegir_face_older_2],
  
  ["rhodok_deserter","Druzhina Deserter","Druzhina Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_nomad_bow,itm_war_bow,itm_scimitar,itm_mace_4,itm_one_handed_war_axe_a,itm_arrows,itm_bodkin_arrows,
    itm_rus_helmet_b,itm_tribal_warrior_outfit,itm_rus_cav_boots,itm_mail_gloves,itm_mail_gauntlets],
   def_attrib|str_10|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,vaegir_face_middle_1, vaegir_face_older_2],
 
  ["rhodok_prison_guard","Prison Guard","Prison Guards",  tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_great_bardiche,
    itm_heavy_gothic_armor_a,itm_heavy_gothic_helmet_a,itm_mail_and_plate_boots_a,itm_hourglass_gauntlets_a],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],
  
  ["rhodok_castle_guard","Castle Guard","Castle Guards", tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_great_bardiche,
    itm_heavy_gothic_armor_a,itm_heavy_gothic_helmet_a,itm_mail_and_plate_boots_a,itm_hourglass_gauntlets_a],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],
  
  ["druzhina_kingsguard","Druzhina King's Guard","Druzhina King's Guards",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_war_bow,itm_scimitar_b,itm_bodkin_arrows,
    itm_rus_helmet_b,itm_heraldic_mail_with_tabard,itm_rus_cav_boots,itm_mail_gauntlets],
   str_24 | agi_21 | int_21 | cha_9|level(35),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_archery(300)|wp_crossbow(150)|wp_throwing(150),knows_common|knows_power_throw_5|knows_power_strike_4|knows_ironflesh_10|knows_shield_1|knows_athletics_8|knows_riding_10|knows_power_draw_8,swadian_face_young_1, swadian_face_old_2],

   
   

   
   #peasant - retainer - footman - man-at-arms -  knight

   
  #Sarranidzi 12

   
  ["sarranid_recruit","Templar Recruit","Templar Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_club,itm_cudgel,itm_pitch_fork,itm_staff,itm_tab_shield_kite_a,
    itm_linen_tunic,itm_arming_cap,itm_wrapping_boots,itm_robe],
   str_7 | agi_5 | int_4 | cha_4|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],

  ["sarranid_footman","Templar Footman","Templar Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_sword_medieval_a,itm_spear,itm_sword_medieval_b_small,itm_fighting_pick,itm_mace_2,itm_tab_shield_kite_b,itm_darts,
    itm_mail_coif,itm_arming_cap,itm_padded_cloth,itm_gambeson,itm_woolen_hose,itm_wrapping_boots],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(10)|wp_throwing(70),knows_common|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1|knows_power_throw_2,swadian_face_young_1, swadian_face_old_2],
   
  ["sarranid_veteran_footman","Templar Veteran Footman","Templar Veteran Footmen",tf_guarantee_armors|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_sword_medieval_c,itm_sword_medieval_c_small,itm_one_handed_battle_axe_a,itm_longsword_c,itm_war_spear,itm_tab_shield_kite_c,itm_tab_shield_kite_d,itm_war_darts,
    itm_helmet_a,itm_nasal_helmet_c,itm_segmented_helmet_b,itm_skullcap_c,itm_skullcap_d,itm_surcoat_over_mail_heraldic,itm_padded_cloth_c,itm_surcoa_over_mail_and_plate_white,itm_mail_chausses,itm_nomad_boots,itm_leather_gloves],
   str_12 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(110)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_4|knows_ironflesh_2|knows_shield_2|knows_athletics_3|knows_power_throw_3,swadian_face_young_1, swadian_face_old_2],

  ["sarranid_infantry","Templar Infantry","Templar Infantries",tf_guarantee_shield|tf_guarantee_armors,0,0,fac_kingdom_6,
   [itm_sword_medieval_c_long,itm_sword_medieval_d_long,itm_military_hammer,itm_one_handed_battle_axe_a,itm_heavy_great_sword,itm_longsword_c,itm_pike_b,itm_tab_shield_kite_d,itm_war_darts,
    itm_helmet_a,itm_crusader_face_plate_a,itm_crusader_face_plate_b,itm_crusader_face_plate_c,itm_surcoa_over_mail_and_plate_white,itm_surcoa_over_mail_and_plate_heraldic,itm_iron_greaves,itm_mail_gauntlets,itm_mail_gloves],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5|knows_power_throw_4,swadian_face_middle_1, swadian_face_old_2],

  ["sarranid_guard","Templar Guard","Templar Guards",tf_guarantee_shield|tf_guarantee_armors,0,0,fac_kingdom_6,
   [itm_crusader_sword,itm_one_handed_battle_axe_c,itm_one_handed_warhammer,itm_morningstar,itm_longsword_c,itm_flamberge,itm_pike_b,itm_large_shield,
    itm_great_helmet_c,itm_crusader_helmet_a,itm_crusader_helmet_b,itm_transitional_white,itm_transitional_heraldic,itm_steel_greaves_a,itm_shynbaulds,itm_hourglass_gloves,itm_hourglass_gauntlets_a],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(140),knows_common|knows_power_throw_4|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7,swadian_face_middle_1, swadian_face_older_2],
 
  ["sarranid_skirmisher","Templar Skirmisher","Templar Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_bolts,itm_light_crossbow,itm_mace_2,itm_sword_medieval_a,itm_sword_medieval_b_small,
    itm_nasal_helmet,itm_arming_cap,itm_padded_cloth,itm_gambeson,itm_woolen_hose,itm_wrapping_boots],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(65)|wp_two_handed(20)|wp_polearm(50)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100),knows_common|knows_power_strike_1|knows_ironflesh_1|knows_athletics_3,swadian_face_young_1, swadian_face_middle_2],
 
  ["sarranid_archer","Templar Crossbowman","Templar Crossbowmen",tf_guarantee_range,0,0,fac_kingdom_6,
   [itm_steel_bolts,itm_heavy_crossbow,itm_fighting_pick,itm_one_handed_battle_axe_a,itm_sword_medieval_c,
    itm_kettle_hat_g,itm_chapel_de_fer_e,itm_padded_cloth_c,itm_padded_cloth,itm_woolen_hose,itm_leather_gloves],
   str_13 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5,swadian_face_young_1, swadian_face_old_2],
 
  ["sarranid_master_archer","Templar Veteran Crossbowman","Templar Veteran Crossbowmen",tf_guarantee_range,0,0,fac_kingdom_6,
   [itm_steel_bolts,itm_sniper_crossbow,itm_military_pick,itm_military_hammer,itm_sword_medieval_c,
    itm_chapel_de_fer_b,itm_kettle_hat_b,itm_kettle_hat_c,itm_surcoa_over_mail_and_plate_white,itm_surcoa_over_mail_and_plate_heraldic,itm_mail_chausses,itm_mail_gauntlets,itm_mail_gloves],
   str_15 | agi_12 | int_4 | cha_4|level(21),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6,swadian_face_middle_1, swadian_face_older_2],
 
  ["sarranid_horseman","Templar Horseman","Templar Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_lance,itm_sword_medieval_b,itm_sword_medieval_a,itm_tab_shield_kite_cav_a,
    itm_skullcap_c,itm_skullcap_e,itm_segmented_helmet_b,itm_neckguard_helm_new_b,itm_padded_cloth_c,itm_hose_kneecops_red,itm_rus_cav_boots,itm_saddle_horse],
   str_12 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(120)|wp_two_handed(120)|wp_polearm(120)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_3|knows_ironflesh_3|knows_shield_2|knows_athletics_3|knows_riding_3,swadian_face_young_1, swadian_face_old_2],
 
  ["sarranid_mamluke","Templar Man at Arms","Templar Men at Arms",tf_mounted|tf_guarantee_armors|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_lance,itm_sword_medieval_c,itm_sword_medieval_c_long,itm_tab_shield_kite_cav_a,itm_tab_shield_kite_cav_b,
    itm_helmet_a,itm_nasal_helmet_c,itm_surcoat_over_mail_heraldic,itm_surcoa_over_mail_and_plate_white,itm_mail_chausses,itm_nomad_boots,itm_leather_gloves,itm_hunter,itm_saddle_horse,itm_courser],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_archery(10)|wp_crossbow(10)|wp_throwing(90),knows_common|knows_power_throw_2|knows_power_strike_5|knows_ironflesh_4|knows_shield_4|knows_athletics_5|knows_riding_5,swadian_face_middle_1, swadian_face_older_2],

  ["sarranid_man_at_arms","Templar Knight","Templar Knights",tf_mounted|tf_guarantee_armors|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_heavy_lance,itm_crusader_sword,itm_longsword_c,itm_morningstar,itm_tab_shield_kite_cav_b,
    itm_helmet_a,itm_crusader_face_plate_a,itm_crusader_face_plate_b,itm_crusader_face_plate_c,itm_surcoa_over_mail_and_plate_white,itm_surcoa_over_mail_and_plate_heraldic,itm_iron_greaves,itm_mail_gauntlets,itm_mail_gloves,itm_hunter,itm_barded_warhorse],
   str_18 | agi_15 | int_4 | cha_4|level(24),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(110),knows_common|knows_power_throw_3|knows_power_strike_7|knows_ironflesh_6|knows_shield_5|knows_athletics_6|knows_riding_7,swadian_face_young_1, swadian_face_old_2],
 
  ["sarranid_knight","Templar Heavy Knight","Templar Heavy Knights",tf_mounted|tf_guarantee_armors|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_heavy_lance,itm_great_lance,itm_crusader_sword,itm_longsword_c,itm_tab_shield_kite_cav_b,
    itm_great_helmet_c,itm_crusader_helmet_a,itm_crusader_helmet_b,itm_transitional_white,itm_transitional_heraldic,itm_steel_greaves_a,itm_shynbaulds,itm_hourglass_gloves,itm_hourglass_gauntlets_a,itm_barded_warhorse],
   str_21 | agi_18 | int_4 | cha_4|level(29),wp_one_handed(200)|wp_two_handed(200)|wp_polearm(200)|wp_archery(10)|wp_crossbow(10)|wp_throwing(130),knows_common|knows_power_throw_4|knows_power_strike_8|knows_ironflesh_7|knows_shield_6|knows_athletics_7|knows_riding_8,swadian_face_middle_1, swadian_face_older_2],
 
  ["sarranid_messenger","Templar Messenger","Templar Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_mail_chausses,itm_sarranid_helmet1,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
 
  ["sarranid_deserter","Templar Deserter","Templar Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_mail_chausses,itm_desert_turban,itm_arabian_horse_a],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
 
  ["sarranid_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_armors,0,0,fac_kingdom_6,
   [itm_crusader_sword,itm_large_shield,
    itm_great_helmet_c,itm_crusader_helmet_a,itm_crusader_helmet_b,itm_transitional_white,itm_transitional_heraldic,itm_steel_greaves_a,itm_shynbaulds,itm_hourglass_gloves,itm_hourglass_gauntlets_a],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_middle_1, swadian_face_older_2],

  ["sarranid_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_armors,0,0,fac_kingdom_6,
   [itm_crusader_sword,itm_large_shield,
    itm_great_helmet_c,itm_crusader_helmet_a,itm_crusader_helmet_b,itm_transitional_white,itm_transitional_heraldic,itm_steel_greaves_a,itm_shynbaulds,itm_hourglass_gloves,itm_hourglass_gauntlets_a],
   def_attrib|level(25),wp_melee(135),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_middle_1, swadian_face_older_2],

  ["templar_kingsguard","Templar King's Guard","Templar King's Guard",tf_guarantee_all_wo_ranged|tf_mounted,0,0,fac_kingdom_6,
   [itm_crusader_sword,itm_large_shield,itm_heavy_lance,
    itm_crusader_face_plate_c,itm_transitional_heraldic,itm_steel_greaves_a,itm_shynbaulds,itm_hourglass_gauntlets_a,itm_warhorse_b],
   str_24 | agi_21 | int_21 | cha_9|level(35),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_archery(150)|wp_crossbow(150)|wp_throwing(150),knows_common|knows_power_throw_5|knows_power_strike_9|knows_ironflesh_10|knows_shield_8|knows_athletics_8|knows_riding_10,swadian_face_young_1, swadian_face_old_2],

   
  ############## EQUES		12
  ["eques_tribesman","Eques Recruit","Eques Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_7,
   [itm_scythe,itm_club,itm_tab_shield_pavise_a,itm_stones,
    itm_shirt,itm_coarse_tunic,itm_hide_boots,itm_wrapping_boots,itm_felt_hat,itm_padded_coif],
   str_7 | agi_5 | int_4 | cha_4|level(4),wp(60),knows_common,vaegir_face_younger_1, vaegir_face_old_2],

  ["eques_spearman","Eques Footman","Eques Footmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_7,
   [itm_sword_medieval_a,itm_winged_mace,itm_sword_medieval_b,itm_axe,itm_spear,itm_tab_shield_pavise_a,itm_darts,itm_war_darts,
    itm_mail_coif,itm_ranger_hood,itm_leather_jerkin,itm_aketon_green,itm_hide_boots,itm_leather_boots,itm_black_leather_gloves],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(10)|wp_throwing(70),knows_common|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1|knows_power_throw_2,vaegir_face_young_1, vaegir_face_old_2],
  
  ["eques_trained_spearman","Eques Trained Footman","Eques Trained Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_7,
   [itm_sword_medieval_c,itm_sword_medieval_c_small,itm_war_spear,itm_german_bastard_sword,itm_mace_2,itm_tab_shield_pavise_b,itm_war_darts,itm_throwing_spears,
    itm_helmet_with_neckguard,itm_kettle_hat,itm_heraldic_mail_with_surcoat,itm_haubergeon,itm_leather_boots,itm_mail_chausses,itm_mail_gloves,itm_mail_gauntlets],
   str_12 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(110)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_4|knows_ironflesh_2|knows_shield_2|knows_athletics_3|knows_power_throw_3,vaegir_face_young_1, vaegir_face_older_2],
  
  ["eques_veteran_spearman","Eques Infantry","Eques Infantry",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_kingdom_7,
   [itm_grosse_messer_a,itm_grosse_messer_b,itm_bastard_sword_b,itm_great_axe,itm_sword_two_handed_a,itm_long_axe_c,itm_pike,itm_tab_shield_pavise_c,itm_tab_shield_pavise_d,itm_throwing_spears,
    itm_guard_helmet,itm_gotland_helmet,itm_banded_armor_b,itm_heavy_gotland_armor,itm_norman_shoes,itm_wisby_gauntlets_black,itm_wisby_gloves_black],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5|knows_power_throw_4,vaegir_face_young_1, vaegir_face_older_2],
  
  ["eques_sergeant","Eques Sergeant","Eques Sergeants",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_7,
   [itm_lombardic_sword,itm_grosse_messer_a,itm_grosse_messer_b,itm_executioner_sword_a,itm_poleaxe_c,itm_morningstar_a,itm_german_greatsword,itm_morningstar,itm_kreigsmesser,itm_pike,itm_bearded_axe,itm_tab_shield_pavise_d,
    itm_great_helmet_j,itm_topfhelm,itm_gotland_helmet,itm_coat_of_plates,itm_transitional_black,itm_norman_shoes,itm_iron_greaves,itm_wisby_gloves,itm_wisby_gauntlets_black],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(140),knows_common|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7|knows_power_throw_5,vaegir_face_middle_1, vaegir_face_older_2],
  
  ["eques_crossbowman","Eques Crossbowman","Eques Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_7,
   [itm_winged_mace,itm_sword_medieval_a,itm_sword_medieval_b,itm_hunting_crossbow,itm_light_crossbow,itm_bolts,
    itm_tabard,itm_coarse_tunic,itm_hide_boots,itm_wrapping_boots,itm_black_hood,itm_ranger_hood,itm_leather_gloves,itm_black_leather_gloves],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(65)|wp_two_handed(20)|wp_polearm(50)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100),knows_common|knows_power_strike_1|knows_ironflesh_1|knows_athletics_3|knows_power_draw_1,vaegir_face_young_1, vaegir_face_older_2],
  
  ["eques_trained_crossbowman","Eques Trained Crossboman","Eques Trained Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_7,
   [itm_fighting_pick,itm_winged_mace,itm_sword_medieval_b_small,itm_sword_medieval_b,itm_crossbow,itm_heavy_crossbow,itm_steel_bolts,itm_bolts,
    itm_kettle_hat_i,itm_black_hood,itm_padded_cloth_b,itm_ragged_outfit,itm_khergit_leather_boots,itm_black_leather_gloves],
   str_11 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5|knows_power_draw_3,vaegir_face_young_1, vaegir_face_older_2],
  
  ["eques_veteran_crossbowman","Eques Veteran Crossboman","Eques Veteran Crossbomen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_7,
   [itm_sniper_crossbow,itm_steel_bolts,itm_grosse_messer_a,itm_grosse_messer_b,itm_winged_mace,
    itm_chapel_de_fer_b,itm_kettle_hat,itm_heraldic_mail_with_tunic,itm_brigandine_black_a,itm_hose_kneecops_red,itm_wisby_gauntlets_black,itm_wisby_gloves_black],
   str_13 | agi_12 | int_4 | cha_4|level(21),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(160)|wp_crossbow(160)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6|knows_power_draw_4,vaegir_face_middle_1, vaegir_face_older_2],
  
  ["eques_sharpshooter","Eques Bowman","Eques Bowmans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_7,
   [itm_long_bow,itm_arrows,itm_bodkin_arrows,itm_grosse_messer_a,itm_grosse_messer_b,
    itm_chapel_de_fer_b,itm_kettle_hat,itm_heraldic_mail_with_tunic,itm_ritterbruder_armor,itm_hose_kneecops_red,itm_wisby_gauntlets_black,itm_wisby_gloves_black],
   str_13 | agi_12 | int_4 | cha_4|level(19),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6|knows_power_draw_4,vaegir_face_middle_1, vaegir_face_older_2],
 
  ["eques_horseman","Eques Horseman","Eques Horsemen",tf_mounted|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_7,
   [itm_lance,itm_sword_medieval_c_long,itm_grosse_messer_b,itm_tab_shield_heater_cav_a,itm_throwing_spears,
    itm_guard_helmet,itm_gotland_helmet,itm_ritterbruder_armor,itm_ritterbruder_armor,itm_ritterbruder_armor,itm_ritterbruder_armor,itm_heavy_gotland_armor,itm_norman_shoes,itm_wisby_gauntlets_black,itm_wisby_gloves_black,itm_saddle_horse,itm_courser],
   str_12 | agi_9 | int_4 | cha_4|level(19),wp_one_handed(120)|wp_two_handed(120)|wp_polearm(120)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_throw_3|knows_power_strike_3|knows_ironflesh_3|knows_shield_2|knows_athletics_3|knows_riding_3,vaegir_face_young_1, vaegir_face_older_2],

  ["eques_veteran_horseman","Eques Veteran Horseman","Eques Veteran Horsemen",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_7,
   [itm_lance,itm_sword_medieval_d_long,itm_great_axe,itm_executioner_sword_a,itm_tab_shield_heater_cav_b,itm_throwing_spears,
    itm_great_helmet_j,itm_topfhelm,itm_gotland_helmet,itm_plated_light_brigandine,itm_transitional_black,itm_norman_shoes,itm_iron_greaves,itm_wisby_gloves,itm_wisby_gauntlets_black,itm_hunter,itm_saddle_horse,itm_courser],
   str_15 | agi_12 | int_4 | cha_4|level(24),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_throw_4|knows_power_strike_5|knows_ironflesh_4|knows_shield_4|knows_athletics_5|knows_riding_5,vaegir_face_middle_1, vaegir_face_older_2],
   
  ["eques_knight","Eques Knight","Eques Knights",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_7,
   [itm_heavy_lance,itm_cav_sword,itm_morningstar,itm_german_bastard_sword,itm_great_lance,itm_bastard_sword_b,itm_tab_shield_heater_cav_b,itm_hand_pavise_b,
    itm_heavy_gothic_helmet_b,itm_visored_sallet_with_coif_b,itm_gothic_knightly_plate_b,itm_heavy_gothic_armor_b,itm_great_helmet_b,itm_black_greaves,itm_wisby_gloves,itm_warhorse_b,itm_hunter,itm_courser,],
   str_18 | agi_15 | int_4 | cha_4|level(29),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(140),knows_common|knows_power_throw_5|knows_power_strike_7|knows_ironflesh_6|knows_shield_5|knows_athletics_6|knows_riding_7,vaegir_face_middle_1, vaegir_face_older_2],

  ["eques_messenger","Eques Messenger","Eques Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_7,
   [itm_scimitar,itm_bardiche,itm_maul,itm_war_spear,itm_tab_shield_kite_b,itm_mace_4,itm_one_handed_war_axe_a,
    itm_rus_helmet_b,itm_vaegir_lamellar_helmet,itm_drz_mail_shirt,itm_kuyak_a,itm_rus_cav_boots,itm_mail_gloves,itm_mail_gauntlets],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,vaegir_face_middle_1, vaegir_face_older_2],
  
  ["eques_deserter","Eques Deserter","Eques Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_nomad_bow,itm_war_bow,itm_scimitar,itm_mace_4,itm_one_handed_war_axe_a,itm_arrows,itm_bodkin_arrows,
    itm_rus_helmet_b,itm_tribal_warrior_outfit,itm_rus_cav_boots,itm_mail_gloves,itm_mail_gauntlets],
   def_attrib|str_10|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,vaegir_face_middle_1, vaegir_face_older_2],
 
  ["eques_prison_guard","Prison Guard","Prison Guards",  tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_poleaxe_c,
    itm_visored_sallet_with_coif_b,itm_heavy_gothic_armor_b,itm_black_greaves,itm_wisby_gloves],
   def_attrib|level(24),wp(190),knows_athletics_3|knows_shield_2|knows_ironflesh_6|knows_power_strike_8,vaegir_face_middle_1, vaegir_face_older_2],
  
  ["eques_castle_guard","Castle Guard","Castle Guards", tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_poleaxe_c,
     itm_heavy_gothic_helmet_b,itm_gothic_knightly_plate_b,itm_black_greaves,itm_wisby_gloves],
    def_attrib|level(24),wp(190),knows_athletics_3|knows_shield_2|knows_ironflesh_6|knows_power_strike_8,vaegir_face_middle_1, vaegir_face_older_2],

  ["eques_kingsguard","Eques King's Guard","Eques King's Guards", tf_guarantee_all_wo_ranged,0,0,fac_kingdom_7,
   [itm_sword_two_handed_a,
     itm_heavy_gothic_helmet_b,itm_gothic_knightly_plate_b,itm_black_greaves,itm_wisby_gloves],
   str_24 | agi_21 | int_21 | cha_9|level(35),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_archery(150)|wp_crossbow(150)|wp_throwing(150),knows_common|knows_power_throw_5|knows_power_strike_9|knows_ironflesh_10|knows_shield_8|knows_athletics_8|knows_riding_10,swadian_face_young_1, swadian_face_old_2],

   
   
   ###########################################################
   ####################		Norse			12
   ############################################################
  ["norse_recruit","Norse Recruit","Norse Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
   [itm_axe,itm_hatchet,itm_wooden_shield,itm_tab_shield_round_a,itm_club,
    itm_linen_tunic,itm_linen_shirt_a,itm_hide_boots,itm_wrapping_boots],
   str_7 | agi_5 | int_4 | cha_4|level(4),wp(60),knows_common,nord_face_younger_1, nord_face_old_2],
  
  ["norse_footman","Norse Footman","Norse Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_8,
   [itm_one_handed_war_axe_a,itm_axe,itm_spear,itm_sword_viking_1,itm_sword_viking_2,itm_tab_shield_round_b,itm_light_throwing_axes,
    itm_leather_cap,itm_nordic_archer_helmet,itm_nordic_veteran_archer_helmet,itm_coarse_tunic,itm_leather_jerkin,itm_leather_boots,itm_nomad_boots,itm_leather_gloves],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(10)|wp_throwing(60),knows_common|knows_power_throw_1|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1,nord_face_young_1, nord_face_old_2],
  
  ["norse_trained_footman","Norse Trained Footman","Norse Trained Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_8,
   [itm_one_handed_battle_axe_a,itm_sword_viking_2_small,itm_sword_viking_2,itm_boar_spear,itm_two_handed_axe,itm_tab_shield_round_c,itm_light_throwing_axes,itm_throwing_axes,
    itm_nordic_footman_helmet,itm_nordic_fighter_helmet,itm_byrnie,itm_mail_hauberk,itm_dark_hauberk,itm_mail_shirt,itm_leather_boots,itm_mail_chausses,itm_mail_mittens,itm_mail_gauntlets,itm_mail_gloves],
   str_12 | agi_9 | int_4 | cha_4|level(15),wp_one_handed(110)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_strike_3|knows_ironflesh_2|knows_shield_2|knows_athletics_3|knows_power_throw_3,nord_face_young_1, nord_face_old_2],
  
  ["norse_warrior","Norse Warrior","Norse Warriors",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [itm_sword_viking_3,itm_war_spear,itm_thegn_sword,itm_tab_shield_round_d,itm_throwing_axes,itm_heavy_throwing_axes,
    itm_nordic_huscarl_helmet,itm_nordic_helmet,itm_heraldic_mail_with_tabard,itm_studded_leather_coat,itm_mail_chausses,itm_norman_shoes,itm_lamellar_gauntlets,itm_scale_gloves_a],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_throw_4|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5,nord_face_young_1, nord_face_older_2],
  
  ["norse_veteran_warrior","Norse Veteran Warrior","Norse Veteran Warriors",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [itm_sword_viking_a_long,itm_sword_viking_c_long,itm_nordic_nobleman_sword,itm_war_spear,itm_tab_shield_round_e,itm_heavy_throwing_axes,itm_throwing_axes,
    itm_nordic_warlord_helmet,itm_gjermundbu_helmet,itm_cuir_bouilli,itm_banded_armor,itm_splinted_greaves,itm_norman_shoes,itm_gauntlets],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(140),knows_common|knows_power_throw_5|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7,nord_face_young_1, nord_face_older_2],
  
  ["norse_axeman","Norse Axeman","Norse Axeman",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [itm_one_handed_battle_axe_b,itm_one_handed_battle_axe_a,itm_two_handed_battle_axe_2,itm_long_axe,itm_tab_shield_round_d,itm_throwing_axes,
    itm_nordic_huscarl_helmet,itm_nordic_helmet,itm_black_studded_leather_mail,itm_byrnja_d,itm_norman_shoes,itm_mail_chausses,itm_lamellar_gauntlets,itm_scale_gloves_a],
   str_15 | agi_12 | int_4 | cha_4|level(22),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(130),knows_common|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5|knows_power_throw_5,nord_face_young_1, nord_face_older_2],
 
  ["norse_vetera_axeman","Norse Vetera Axeman","Norse Veteran Axemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [itm_one_handed_battle_axe_c,itm_one_handed_battle_axe_b,itm_celtic_axe,itm_long_axe_b,itm_heavy_throwing_axes,itm_tab_shield_round_e,itm_heavy_throwing_axes,
    itm_nordic_warlord_helmet,itm_nordic_warlord_helmet,itm_nordic_warlord_helmet,itm_nordic_warlord_helmet,itm_gjermundbu_helmet,itm_coat_of_plates,itm_banded_armor_b,itm_norman_shoes,itm_mail_chausses,itm_hourglass_gloves,itm_hourglass_gauntlets_a],
   str_18 | agi_15 | int_4 | cha_4|level(27),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(160),knows_common|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7|knows_power_throw_6,nord_face_young_1, nord_face_old_2],

  ["norse_huntsman","Norse Huntsman","Norse Huntsmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
   [itm_hunting_bow,itm_arrows,itm_one_handed_war_axe_a,itm_sword_viking_1,
    itm_leather_cap,itm_coarse_tunic,itm_hide_boots],
   str_9 | agi_7 | int_4 | cha_4|level(8),wp_one_handed(65)|wp_two_handed(20)|wp_polearm(50)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100),knows_common|knows_power_strike_1|knows_ironflesh_1|knows_athletics_3|knows_power_draw_1,nord_face_young_1, nord_face_old_2],
 
  ["norse_archer","Norse Archer","Norse Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
   [itm_short_bow,itm_arrows,itm_bodkin_arrows,itm_long_bow,itm_one_handed_war_axe_a,itm_sword_viking_1,
    itm_nordic_veteran_archer_helmet,itm_nordic_footman_helmet,itm_leather_jerkin,itm_nomad_boots,itm_leather_boots,itm_leather_gloves],
   str_11 | agi_9 | int_4 | cha_4|level(13),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5|knows_power_draw_3,nord_face_young_1, nord_face_old_2],
  
  ["norse_veteran_archer","Norse Veteran Archer","Norse Veteran Archers",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
   [itm_long_bow,itm_bodkin_arrows,itm_one_handed_battle_axe_a,itm_sword_viking_2,itm_sword_viking_2_small,
    itm_nordic_fighter_helmet,itm_nordic_helmet,itm_byrnja,itm_byrnja_b,itm_leather_boots,itm_nomad_boots,itm_leather_gloves],
   str_13 | agi_12 | int_4 | cha_4|level(18),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6|knows_power_draw_4,nord_face_middle_1, nord_face_older_2],
  
  ["norse_horseman","Norse Horseman","Norse Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [itm_sword_viking_3,itm_sword_viking_a_long,itm_tab_shield_round_d,itm_light_throwing_axes,
    itm_nordic_huscarl_helmet,itm_nordic_helmet,itm_mail_hauberk,itm_dark_hauberk,itm_mail_chausses,itm_norman_shoes,itm_mail_mittens,itm_mail_gauntlets,itm_saddle_horse,itm_sumpter_horse],
   str_12 | agi_9 | int_4 | cha_4|level(19),wp_one_handed(120)|wp_two_handed(120)|wp_polearm(120)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_throw_2|knows_power_strike_3|knows_ironflesh_3|knows_shield_2|knows_athletics_3|knows_riding_3,nord_face_young_1, nord_face_older_2],
  
  ["norse_cavalryman","Norse Cavalryman","Norse Cavalrymen",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [itm_sword_viking_c_long,itm_nordic_nobleman_sword,itm_tab_shield_round_d,itm_throwing_axes,
    itm_nordic_warlord_helmet,itm_gjermundbu_helmet,itm_cuir_bouilli,itm_banded_armor,itm_splinted_greaves,itm_norman_shoes,itm_lamellar_gauntlets,itm_scale_gloves_a,itm_hunter,itm_courser],
   str_15 | agi_12 | int_4 | cha_4|level(25),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_throw_4|knows_power_strike_5|knows_ironflesh_4|knows_shield_4|knows_athletics_5|knows_riding_5,nord_face_middle_1, nord_face_older_2],
				
  ["norse_messenger","Norse Messenger","Norse Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_8,
   [itm_sword_viking_2,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,nord_face_young_1, nord_face_older_2],
  
  ["norse_deserter","Norse Deserter","Norse Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,nord_face_young_1, nord_face_older_2],
  
  ["norse_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_8,
   [itm_celtic_axe,
    itm_nordic_warlord_helmet,itm_banded_armor_b,itm_norman_shoes,itm_hourglass_gauntlets_a],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7,nord_face_middle_1, nord_face_older_2],
  
  ["norse_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_8,
   [itm_celtic_axe,
    itm_nordic_warlord_helmet,itm_coat_of_plates,itm_norman_shoes,itm_hourglass_gauntlets_a],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7,nord_face_middle_1, nord_face_older_2],

  ["norse_kingsguard","Norse King's Guard","Norse King's Guards", tf_guarantee_all_wo_ranged,0,0,fac_kingdom_8,
   [itm_nordic_nobleman_sword,itm_tab_shield_round_e,itm_one_handed_battle_axe_c,
    itm_winged_great_helmet,itm_coat_of_plates_green,itm_norman_shoes,itm_plate_mittens],
   str_24 | agi_21 | int_21 | cha_9|level(35),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_archery(150)|wp_crossbow(150)|wp_throwing(190),knows_common|knows_power_throw_7|knows_power_strike_9|knows_ironflesh_10|knows_shield_8|knows_athletics_8|knows_riding_10,swadian_face_young_1, swadian_face_old_2],
   
   ############
   ############## ODE			12
   ###########
  ["order_recruit","ODE Recruit","ODE Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_9,
   [itm_pitch_fork,itm_club,itm_cleaver,itm_tab_shield_heater_a,itm_stones,
	itm_arming_cap,itm_felt_hat,itm_shirt,itm_blue_tunic,itm_wrapping_boots,itm_hide_boots],
   str_7 | agi_5 | int_4 | cha_4|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 
  ["order_footman","ODE Footman","ODE Footman",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_9,
   [itm_falchion,itm_falchion_c,itm_shortened_voulge,itm_military_fork,itm_tab_shield_heater_b,itm_tab_shield_heater_a,itm_darts,
    itm_hood_d,itm_leather_cap,itm_tabard,itm_blue_gambeson_a,itm_ankle_boots,itm_woolen_hose,itm_leather_gloves],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(10)|wp_throwing(60),knows_common|knows_power_throw_1|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  
  ["order_trained_footman","ODE Trained Footman","ODE Trained Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_9,
   [itm_falchion,itm_fauchard_fork,itm_sledgehammer,itm_fighting_pick,itm_military_fork,itm_tab_shield_heater_c,itm_tab_shield_heater_b,itm_war_darts,
    itm_helmet_with_neckguard,itm_pepperpot_helmet_f,itm_scale_armor,itm_palace_guard,itm_mail_chausses,itm_rus_shoes,itm_mail_gauntlets,itm_mail_gloves],
   str_12 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(110)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(90),knows_common|knows_power_throw_1|knows_power_strike_4|knows_ironflesh_2|knows_shield_2|knows_athletics_3,swadian_face_young_1, swadian_face_old_2],
  
  ["order_veteran_footman","ODE Veteran Footman","ODE Veteran Footmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_9,
   [itm_falchion_b,itm_military_hammer,itm_morningstar,itm_bastard_sword_a,itm_french_longsword,itm_battle_fork,itm_tab_shield_heater_d,itm_tab_shield_heater_c,
    itm_full_helm,itm_chapel_de_fer_g,itm_surcoa_over_mail_and_plate_blue,itm_brigandine_blue_a,itm_hose_kneecops_red,itm_hose_kneecops_green,itm_hourglass_gauntlets_a,itm_hourglass_gloves],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(110),knows_common|knows_power_throw_2|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5,swadian_face_middle_1, swadian_face_old_2],
 
  ["order_spearman","ODE Spearman","ODE Spearman",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_9,
   [itm_long_voulge,itm_bec_de_corbin_a,itm_spetum_b,itm_guisarme_a,
    itm_chapel_de_fer_g,itm_open_sallet,itm_brigandine_blue_a,itm_mail_and_plate,itm_hose_kneecops_green,itm_hose_kneecops_red,itm_hourglass_gauntlets_a,itm_hourglass_gloves],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(110),knows_common|knows_power_throw_2|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5,swadian_face_middle_1, swadian_face_old_2],

  ["order_elite_footman","ODE Elite Footman","ODE Elite Footmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_9,
   [itm_french_greatsword,itm_warhammer,itm_falchion_b,itm_espada_eslavona_b,itm_military_pick,itm_tab_shield_heater_d,
	itm_pepperpot_helmet_e,itm_french_pepperpot_helmet,itm_french_pepperpot_helmet_b,itm_french_plate,itm_churburg_a,itm_iron_greaves,itm_shynbaulds,itm_hourglass_gauntlets_a,itm_hourglass_gloves],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(130),knows_common|knows_power_throw_3|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7,swadian_face_middle_1, swadian_face_older_2],
  
  ["order_crossbowman","ODE Crossbowman","ODE Crossbowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_9,
   [itm_light_crossbow,itm_hunting_crossbow,itm_bolts,itm_falchion,itm_spiked_club,itm_fighting_pick,
    itm_footman_helmet,itm_hood_d,itm_padded_leather,itm_blue_gambeson_a,itm_blue_hose,itm_woolen_hose,itm_leather_gloves],
   str_11 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5|knows_power_draw_3,swadian_face_young_1, swadian_face_middle_2],
  
  ["order_veteran_crossbowman","ODE Trained Crossbowman","ODE Trained Crossbowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_9,
   [itm_crossbow,itm_heavy_crossbow,itm_bolts,itm_steel_bolts,itm_military_hammer,itm_fighting_pick,itm_falchion_c,itm_falchion,
    itm_kettle_hat,itm_helmet_with_neckguard,itm_heraldic_mail_with_tunic,itm_haubergeon,itm_mail_chausses,itm_leather_boots,itm_mail_mittens,itm_mail_gloves],
   str_13 | agi_12 | int_4 | cha_4|level(19),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6|knows_power_draw_4,swadian_face_young_1, swadian_face_old_2],
  
  ["order_elite_crossbowman","ODE Elite Crossbowman","ODE Elite Crossbowmen",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_9,
   [itm_sniper_crossbow,itm_heavy_crossbow,itm_steel_bolts,itm_falchion_b,itm_military_hammer,itm_military_pick,itm_espada_eslavona_a,
    itm_chapel_de_fer_a,itm_helmet_a,itm_heraldic_mail_with_tunic_b,itm_palace_guard,itm_splinted_leather_greaves,itm_nomad_boots,itm_mail_mittens,itm_mail_gloves,itm_mail_gauntlets],
   str_15 | agi_15 | int_4 | cha_4|level(24),wp_one_handed(95)|wp_two_handed(50)|wp_polearm(80)|wp_archery(180)|wp_crossbow(180)|wp_throwing(180),knows_common|knows_power_strike_2|knows_ironflesh_5|knows_athletics_7|knows_power_draw_6,swadian_face_middle_1, swadian_face_older_2],
  
  ["order_nobleman","ODE Nobleman","ODE Noblemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_9,
   [itm_light_lance,itm_lance,itm_military_pick,itm_espada_eslavona_a,itm_tab_shield_heater_cav_a,
	itm_footman_helmet,itm_norman_helmet,itm_blue_gambeson_a,itm_padded_leather,itm_blue_hose,itm_leather_boots,itm_leather_gloves,itm_courser,itm_saddle_horse],
   str_9 | agi_7 | int_4 | cha_4|level(12),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(10)|wp_throwing(80),knows_common|knows_power_throw_2|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1|knows_riding_3,swadian_face_middle_1, swadian_face_old_2],
 
  ["order_knight","ODE Knight","ODE Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_9,
   [itm_lance,itm_heavy_lance,itm_bastard_sword_a,itm_espada_eslavona_a,itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_a,
    itm_open_sallet,itm_open_sallet_coif,itm_surcoa_over_mail_and_plate_blue,itm_surcoat_over_mail_blue,itm_hose_kneecops_green,itm_hose_kneecops_red,itm_hourglass_gauntlets_a,itm_hourglass_gloves,itm_hunter,itm_courser],
   str_12 | agi_9 | int_4 | cha_4|level(19),wp_one_handed(110)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(100),knows_common|knows_power_throw_3|knows_power_strike_4|knows_ironflesh_2|knows_shield_2|knows_athletics_3|knows_riding_5,swadian_face_middle_1, swadian_face_older_2],

  ["order_heavy_knight","ODE Heavy Knight","ODE Heavy Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_9,
   [itm_heavy_lance,itm_great_lance,itm_french_longsword,itm_espada_eslavona_b,itm_bastard_sword_b,itm_tab_shield_heater_cav_b,
    itm_visored_sallet,itm_visored_sallet_coif,itm_churburg_a,itm_transitional_blue,itm_shynbaulds,itm_splinted_greaves_spurs,itm_gilded_hourglass_gloves,itm_hourglass_gauntlets_b,itm_warhorse,itm_hunter],
   str_16 | agi_12 | int_4 | cha_4|level(29),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_throw_4|knows_power_strike_5|knows_ironflesh_4|knows_shield_4|knows_athletics_5|knows_riding_7,swadian_face_young_1, swadian_face_old_2],
 
  ["order_messenger","ODE Messenger","ODE Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_9,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,swadian_face_young_1, swadian_face_old_2],
  ["order_deserter","ODE Deserter","ODE Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_dagger,itm_club,itm_voulge,itm_wooden_shield,itm_leather_jerkin,itm_padded_cloth,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet],
   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_old_2],
  ["order_prison_guard","Prison Guard","Prison Guards",tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_9,
   [itm_french_greatsword,
    itm_visored_sallet,itm_visored_sallet_coif,itm_french_plate,itm_shynbaulds,itm_iron_greaves,itm_hourglass_gauntlets_a],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["order_castle_guard","Castle Guard","Castle Guards",tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_9,
   [itm_french_greatsword,
	itm_visored_sallet_coif,itm_visored_sallet,itm_french_plate,itm_shynbaulds,itm_iron_greaves,itm_hourglass_gauntlets_a],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

  ["order_kingsguard","ODE King's Guard","ODE King's Guards",tf_guarantee_all_wo_ranged|tf_mounted|tf_no_capture_alive,0,0,fac_kingdom_9,
   [itm_falchion_b,itm_tab_shield_heater_cav_b,
	itm_full_helm,itm_french_plate,itm_iron_greaves,itm_hourglass_gauntlets_c,itm_saddle_horse],
   str_24 | agi_21 | int_21 | cha_9|level(35),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_archery(150)|wp_crossbow(150)|wp_throwing(150),knows_common|knows_power_throw_5|knows_power_strike_9|knows_ironflesh_10|knows_shield_8|knows_athletics_8|knows_riding_10,swadian_face_young_1, swadian_face_old_2],

   
  ################ PLAYER Troops
  ### 																				###### do zmiany w WSE na odnalezienie jednostki o tym id i zwrocenie jej ID w formie int
  ["player_recruit","Recruit","Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_player_supporters_faction,
   [itm_club,itm_spiked_club,itm_cleaver,itm_tab_shield_round_a,
	itm_felt_hat,itm_straw_hat,itm_shirt,itm_linen_shirt_a,itm_wrapping_boots,itm_hide_boots],
   str_7 | agi_5 | int_4 | cha_4|level(4),wp(60),knows_common|knows_inventory_management_10,swadian_face_younger_1, swadian_face_middle_2],
 
  ["player_footman","Footman","Footmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_player_supporters_faction,
   [itm_sword_medieval_a,itm_spiked_club,itm_one_handed_war_axe_a,itm_shortened_spear,itm_spear,itm_tab_shield_round_b,
    itm_nordic_archer_helmet,itm_leather_warrior_cap,itm_leather_jerkin,itm_red_gambeson,itm_nomad_boots,itm_leather_boots,itm_leather_gloves,itm_black_leather_gloves],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1|knows_power_throw_2,swadian_face_younger_1, swadian_face_middle_2],
  
  ["player_trained_footman","Trained Footman","Trained Footmen",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_player_supporters_faction,
   [itm_one_handed_war_axe_b,itm_sword_medieval_b,itm_sword_medieval_c,itm_fighting_pick,itm_war_spear,itm_spear,itm_long_hafted_knobbed_mace,itm_javelin,itm_tab_shield_round_c,itm_tab_shield_round_b,
	itm_helmet_with_neckguard,itm_segmented_helmet,itm_mail_shirt_with_fur,itm_byrnie,itm_nomad_boots,itm_leather_boots,itm_leather_gloves],
   str_12 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(110)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_4|knows_ironflesh_2|knows_shield_2|knows_athletics_3|knows_power_throw_2,swadian_face_younger_1, swadian_face_middle_2],
  
  ["player_infantry","Infantry","Infantries",tf_guarantee_shield|tf_guarantee_armors,0,0,fac_player_supporters_faction,
   [itm_one_handed_battle_axe_b,itm_steel_pick,itm_military_hammer,itm_bardiche,itm_war_spear,itm_long_bardiche,itm_longsword_b,itm_long_hafted_spiked_mace,itm_ashwood_pike,itm_tab_shield_round_c,itm_tab_shield_round_d,itm_javelin,itm_throwing_spears,
	itm_guard_helmet,itm_bascinet_3,itm_heraldic_mail_with_surcoat,itm_heraldic_mail_with_tabard,itm_mail_chausses,itm_mail_mittens,itm_hourglass_gloves,itm_gilded_hourglass_gloves],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5|knows_power_throw_3,swadian_face_younger_1, swadian_face_middle_2],
    
  ["player_elite_footman","Elite Footman","Elite Footmen",tf_guarantee_shield|tf_guarantee_armors,0,0,fac_player_supporters_faction,
   [itm_one_handed_battle_axe_b,itm_steel_pick,itm_military_hammer,itm_bardiche,itm_war_spear,itm_long_bardiche,itm_longsword_b,itm_long_hafted_spiked_mace,itm_ashwood_pike,itm_tab_shield_round_c,itm_tab_shield_round_d,itm_javelin,itm_throwing_spears,
	itm_guard_helmet,itm_bascinet_3,itm_heraldic_mail_with_surcoat,itm_heraldic_mail_with_tabard,itm_mail_chausses,itm_mail_mittens,itm_hourglass_gloves,itm_gilded_hourglass_gloves],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5|knows_power_throw_4,swadian_face_younger_1, swadian_face_middle_2],

  ["player_sergeant","Sergeant","Sergeants",tf_guarantee_shield|tf_guarantee_armors|tf_mounted,0,0,fac_player_supporters_faction,
   [itm_one_handed_warhammer,itm_one_handed_battle_axe_c,itm_steel_pick,itm_sword_two_handed_a,itm_great_bardiche,itm_warhammer,itm_great_long_bardiche,itm_ashwood_pike,itm_tab_shield_round_d,itm_tab_shield_round_e,itm_throwing_spears,
	itm_great_helmet_f,itm_great_helmet_g,itm_gotland_helmet_b,itm_great_helmet_h,itm_great_helmet_i,itm_transitional_blue,itm_churburg_a,itm_transitional_heraldic,itm_steel_greaves_a,itm_iron_greaves,itm_gilded_hourglass_gloves,itm_hourglass_gloves,itm_hourglass_gauntlets_a,itm_hourglass_gauntlets_b],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7|knows_power_throw_5,swadian_face_younger_1, swadian_face_middle_2],
  

  ["player_skirmisher","Skirmisher","Skirmishers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_player_supporters_faction,
   [itm_fighting_pick,itm_one_handed_war_axe_a,itm_hunting_bow,itm_arrows,itm_short_bow,itm_barbed_arrows,
   	itm_nordic_archer_helmet,itm_leather_warrior_cap,itm_leather_jerkin,itm_red_gambeson,itm_nomad_boots,itm_leather_boots,itm_leather_gloves,itm_black_leather_gloves],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(65)|wp_two_handed(20)|wp_polearm(50)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100),knows_common|knows_power_strike_1|knows_ironflesh_1|knows_athletics_3|knows_power_draw_1,swadian_face_younger_1, swadian_face_middle_2],

  ["player_archer","Archer","Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_player_supporters_faction,
   [itm_one_handed_war_axe_b,itm_sword_medieval_a,itm_long_bow,itm_barbed_arrows,itm_short_bow,itm_bodkin_arrows,
    itm_nordic_archer_helmet,itm_leather_warrior_cap,itm_leather_jerkin,itm_red_gambeson,itm_nomad_boots,itm_leather_boots,itm_leather_gloves,itm_black_leather_gloves],
   str_11 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5|knows_power_draw_3,swadian_face_younger_1, swadian_face_middle_2],

  ["player_master_archer","Master Archer","Master Archers",tf_guarantee_range|tf_mounted,0,0,fac_player_supporters_faction,
   [itm_one_handed_war_axe_b,itm_military_hammer,itm_long_bow,itm_barbed_arrows,itm_bodkin_arrows,
	itm_helmet_with_neckguard,itm_segmented_helmet,itm_mail_shirt_with_fur,itm_byrnie,itm_nomad_boots,itm_leather_boots,itm_leather_gloves],
   str_13 | agi_12 | int_4 | cha_4|level(19),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6|knows_power_draw_4,swadian_face_younger_1, swadian_face_middle_2],

   
  ["player_horseman","Horseman","Horsemen",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_horse|tf_mounted,0,0,fac_player_supporters_faction,
   [itm_sword_medieval_a,itm_sword_medieval_b,itm_light_lance,itm_lance,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_javelin,
	itm_helmet_with_neckguard,itm_segmented_helmet,itm_mail_shirt_with_fur,itm_byrnie,itm_nomad_boots,itm_leather_boots,itm_leather_gloves,itm_saddle_horse,itm_courser],
   str_12 | agi_9 | int_4 | cha_4|level(17),wp_one_handed(120)|wp_two_handed(120)|wp_polearm(120)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_3|knows_ironflesh_3|knows_shield_2|knows_athletics_3|knows_riding_3,swadian_face_younger_1, swadian_face_middle_2],

  ["player_nobleman","Nobleman","Noblemen",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves|tf_mounted|tf_guarantee_horse,0,0,fac_player_supporters_faction,
   [itm_one_handed_battle_axe_b,itm_steel_pick,itm_military_hammer,itm_bardiche,itm_longsword_b,itm_lance,itm_heavy_lance,itm_tab_shield_round_c,itm_tab_shield_small_round_b,
	itm_guard_helmet,itm_bascinet_3,itm_heraldic_mail_with_surcoat,itm_heraldic_mail_with_tabard,itm_mail_chausses,itm_mail_mittens,itm_hourglass_gloves,itm_gilded_hourglass_gloves,itm_courser,itm_hunter],
   str_15 | agi_12 | int_4 | cha_4|level(21),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_5|knows_ironflesh_4|knows_shield_4|knows_athletics_5|knows_riding_5,swadian_face_younger_1, swadian_face_middle_2],

  ["player_knight","Knight","Knights",tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves|tf_mounted|tf_guarantee_horse,0,0,fac_player_supporters_faction,
   [itm_one_handed_warhammer,itm_one_handed_battle_axe_c,itm_steel_pick,itm_sword_two_handed_a,itm_heavy_lance,itm_great_lance,itm_tab_shield_small_round_c,
	itm_great_helmet_f,itm_great_helmet_g,itm_gotland_helmet_b,itm_great_helmet_h,itm_great_helmet_i,itm_transitional_blue,itm_churburg_a,itm_transitional_heraldic,itm_steel_greaves_a,itm_iron_greaves,itm_gilded_hourglass_gloves,itm_hourglass_gloves,itm_hourglass_gauntlets_a,itm_hourglass_gauntlets_b,itm_warhorse,itm_warhorse_b],
    str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_7|knows_ironflesh_6|knows_shield_5|knows_athletics_6|knows_riding_7,swadian_face_younger_1, swadian_face_middle_2],

  ["player_kingsguard","King's Guard","King's Guards",tf_guarantee_all_wo_ranged|tf_mounted|tf_no_capture_alive,0,0,fac_kingdom_9,
   [itm_one_handed_battle_axe_b,itm_tab_shield_small_round_c,
	itm_great_helmet_f,itm_great_helmet_g,itm_gotland_helmet_b,itm_great_helmet_h,itm_great_helmet_i,itm_transitional_blue,itm_churburg_a,itm_transitional_heraldic,itm_steel_greaves_a,itm_iron_greaves,itm_gilded_hourglass_gloves,itm_hourglass_gloves,itm_hourglass_gauntlets_a,itm_hourglass_gauntlets_b,itm_warhorse,itm_warhorse_b],
   str_24 | agi_21 | int_21 | cha_9|level(35),wp_one_handed(300)|wp_two_handed(300)|wp_polearm(300)|wp_archery(150)|wp_crossbow(150)|wp_throwing(150),knows_common|knows_power_strike_9|knows_ironflesh_10|knows_shield_8|knows_athletics_8|knows_riding_10,swadian_face_young_1, swadian_face_old_2],
 
 ["player_prison_guard","Prison Guard","Prison Guards",tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_9,
   [itm_great_long_bardiche,
	itm_great_helmet_f,itm_great_helmet_g,itm_gotland_helmet_b,itm_great_helmet_h,itm_great_helmet_i,itm_transitional_blue,itm_churburg_a,itm_transitional_heraldic,itm_steel_greaves_a,itm_iron_greaves,itm_gilded_hourglass_gloves,itm_hourglass_gloves,itm_hourglass_gauntlets_a,itm_hourglass_gauntlets_b,itm_warhorse,itm_warhorse_b],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["player_castle_guard","Castle Guard","Castle Guards",tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_9,
   [itm_great_long_bardiche,
	itm_great_helmet_f,itm_great_helmet_g,itm_gotland_helmet_b,itm_great_helmet_h,itm_great_helmet_i,itm_transitional_blue,itm_churburg_a,itm_transitional_heraldic,itm_steel_greaves_a,itm_iron_greaves,itm_gilded_hourglass_gloves,itm_hourglass_gloves,itm_hourglass_gauntlets_a,itm_hourglass_gauntlets_b,itm_warhorse,itm_warhorse_b],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],


  ["looter","Looter","Looters",0,0,0,fac_outlaws,
   [itm_hatchet,itm_club,itm_butchering_knife,itm_falchion,itm_rawhide_coat,itm_stones,itm_nomad_armor,itm_nomad_armor,itm_woolen_cap,itm_woolen_cap,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(20),knows_common,bandit_face1, bandit_face2],
  ["bandit","Bandit","Bandits",tf_guarantee_armor,0,0,fac_outlaws,
   [itm_arrows,itm_spiked_mace,itm_sword_viking_1,itm_short_bow,itm_falchion,itm_nordic_shield,itm_rawhide_coat,itm_leather_cap,itm_leather_jerkin,itm_nomad_armor,itm_nomad_boots,itm_wrapping_boots,itm_saddle_horse],
   def_attrib|level(10),wp(60),knows_common|knows_power_draw_1,bandit_face1, bandit_face2],
  ["brigand","Brigand","Brigands",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_outlaws,
   [itm_arrows,itm_spiked_mace,itm_sword_viking_1,itm_falchion,itm_wooden_shield,itm_hide_covered_round_shield,itm_long_bow,itm_leather_cap,itm_leather_jerkin,itm_nomad_boots,itm_saddle_horse],
   def_attrib|level(16),wp(90),knows_common|knows_power_draw_3,bandit_face1, bandit_face2],


###### 		Mountain Bandits	########## 
  ["mountain_bandit","Mountain Bandit","Mountain Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_spear,itm_spiked_club,itm_falchion,itm_short_bow,itm_javelin,itm_fur_covered_shield,itm_hide_covered_round_shield,
    itm_felt_hat,itm_head_wrappings,itm_rawhide_coat,itm_leather_armor,itm_hide_boots,itm_nomad_boots],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_2|knows_shield_2|knows_athletics_2,rhodok_face_young_1, rhodok_face_old_2],
 
  ["mountain_archer","Mountain Archer","Mountain Archers",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_winged_mace,itm_falchion,itm_short_bow,
    itm_felt_hat,itm_head_wrappings,itm_skullcap,itm_ragged_outfit,itm_rawhide_coat,itm_leather_armor,itm_hide_boots,itm_nomad_boots,itm_wooden_shield,itm_nordic_shield],
   def_attrib|str_12|agi_10|level(15),wp(120)|wp_archery(150),knows_common|knows_power_draw_4|knows_power_strike_1|knows_athletics_4,rhodok_face_young_1, rhodok_face_old_2],

  ["mountain_warrior","Mountain Warrior","Mountain Warriors",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_sword_viking_1,itm_spear,itm_long_spiked_club,itm_winged_mace,itm_maul,itm_falchion,itm_javelin,itm_fur_covered_shield,itm_hide_covered_round_shield,
   itm_skullcap,itm_ragged_outfit,itm_leather_armor,itm_nomad_boots,itm_wooden_shield,itm_nordic_shield],
   def_attrib|str_15|agi_12|level(15),wp(140),knows_common|knows_power_draw_2|knows_power_strike_4|knows_shield_4|knows_athletics_4,rhodok_face_young_1, rhodok_face_old_2],

  ["mountain_leader","Mountain Leader","Mountain Leaders",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_sword_viking_1,itm_nailed_warclub,itm_maul,itm_battle_axe,itm_javelin,itm_fur_covered_shield,itm_hide_covered_round_shield,
    itm_helmet_a,itm_kuyak_a,itm_leather_boots,itm_leather_gloves],
   def_attrib|str_18|agi_15|level(18),wp(180),knows_common|knows_power_draw_2|knows_power_strike_6|knows_shield_4|knows_athletics_4,rhodok_face_young_1, rhodok_face_old_2],

###### 		Forest Bandits	##########
  ["forest_bandit","Forest Bandit","Forest Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_axe,itm_hatchet,itm_staff,itm_short_bow,itm_hunting_bow,
    itm_common_hood,itm_black_hood,itm_shirt,itm_padded_leather,itm_leather_jerkin,itm_ragged_outfit,itm_hide_boots,itm_leather_boots],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_2,swadian_face_young_1, swadian_face_old_2],

  ["forest_archer","Forest Archer","Forest Archers",tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_axe,itm_hatchet,itm_staff,itm_long_bow,itm_barbed_arrows,
    itm_nasal_helmet,itm_black_hood,itm_padded_leather,itm_ranger_leather_armor,itm_hide_boots,itm_leather_boots,itm_leather_gloves],
   def_attrib|str_12|agi_12|level(15),wp(120)|wp_archery(150),knows_common|knows_power_draw_5|knows_athletics_3,swadian_face_young_1, swadian_face_old_2],

  ["forest_fighters","Forest Fighter","Forest Fighters",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_mace_2,itm_long_hafted_knobbed_mace,itm_spear,itm_falchion,itm_spear,itm_axe,
    itm_nasal_helmet,itm_helmet_with_neckguard,itm_red_gambeson,itm_ragged_outfit,itm_hide_boots,itm_leather_boots,itm_leather_gloves],
   def_attrib|str_12|agi_10|level(15),wp(150),knows_common|knows_power_draw_3|knows_athletics_4|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

  ["forest_bandit_leader","Forest Bandits Leader","Forest Bandits Leaders",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_mace_2,itm_long_hafted_knobbed_mace,itm_sword_medieval_a,
    itm_nasal_helmet_c,itm_helmet_with_neckguard,itm_mail_shirt_with_fur,itm_leather_boots,itm_leather_gloves],
   def_attrib|str_15|agi_12|level(18),wp(180),knows_common|knows_power_draw_3|knows_athletics_4|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
   
######  	SEA RAIDERS   	##########
  ["sea_raider_light","Sea Raider","Sea Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_one_handed_war_axe_a,itm_spear,itm_nordic_shield,itm_nordic_shield,itm_round_shield,itm_wooden_shield,itm_long_bow,itm_javelin,itm_light_throwing_axes,
    itm_nasal_helmet,itm_nordic_fighter_helmet,itm_nomad_vest,itm_leather_jerkin,itm_leather_boots, itm_nomad_boots],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(110)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(10)|wp_throwing(90),knows_common|knows_power_strike_2|knows_power_throw_2|knows_ironflesh_1|knows_shield_3|knows_athletics_1,nord_face_young_1, nord_face_old_2],
 
  ["sea_raider","Sea Raider","Sea Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_one_handed_battle_axe_a,itm_one_handed_war_axe_a,itm_spear,itm_nordic_shield,itm_round_shield,itm_nordic_shield,itm_wooden_shield,itm_long_bow,itm_javelin,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_fighter_helmet,itm_byrnie,itm_mail_shirt,itm_leather_boots, itm_nomad_boots,itm_leather_gloves],
   str_12 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(140)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(120),knows_common|knows_power_strike_4|knows_power_throw_4|knows_ironflesh_2|knows_shield_5|knows_athletics_3,nord_face_young_1, nord_face_old_2],
 
  ["sea_raider_leader_a","Sea Raider Leader","Sea Raiders Leaders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_nordic_nobleman_sword,itm_sword_viking_a_long,itm_sword_viking_c_long,itm_two_handed_battle_axe_2,itm_long_axe,itm_tab_shield_round_d,itm_round_shield,itm_javelin,itm_heavy_throwing_axes,
    itm_nordic_huscarl_helmet,itm_dark_hauberk,itm_mail_hauberk,itm_leather_boots, itm_nomad_boots,itm_leather_gloves],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(170)|wp_two_handed(170)|wp_polearm(170)|wp_archery(10)|wp_crossbow(10)|wp_throwing(110),knows_common|knows_power_strike_6|knows_power_throw_5|knows_ironflesh_3|knows_shield_8|knows_athletics_5,nord_face_young_1, nord_face_old_2],

###### 		Steppe Bandits	##########
  ["steppe_bandit","Steppe Bandit","Steppe Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear, itm_light_lance,itm_nomad_bow,itm_nomad_bow,itm_short_bow,itm_jarid,
    itm_leather_steppe_cap_a,itm_leather_steppe_cap_b,itm_nomad_cap,itm_nomad_cap_b,itm_khergit_armor,itm_steppe_armor,itm_leather_vest,itm_hide_boots,itm_nomad_boots,itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_saddle_horse,itm_steppe_horse,itm_steppe_horse],
   def_attrib|level(12),wp(100),knows_riding_4|knows_shield_1|knows_horse_archery_3|knows_power_draw_3|knows_power_strike_2,khergit_face_young_1, khergit_face_old_2],
 
  ["steppe_bandit_archer","Steppe Horse Archer","Steppe Horse Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_mounted,0,0,fac_outlaws,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_khergit_bow,itm_strong_bow,itm_jarid,
    itm_leather_steppe_cap_a,itm_leather_steppe_cap_b,itm_nomad_cap,itm_nomad_cap_b,itm_tribal_warrior_outfit,itm_steppe_armor,itm_leather_vest,itm_hide_boots,itm_nomad_boots,itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_saddle_horse,itm_steppe_horse,itm_steppe_horse],
   def_attrib|str_10|agi_10|level(15),wp(140),knows_riding_6|knows_shield_2|knows_horse_archery_5|knows_power_draw_5|knows_power_strike_2,khergit_face_young_1, khergit_face_old_2],
 
  ["steppe_bandit_lancer","Steppe Lancer","Steppe Lancers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_sword_khergit_1,itm_winged_mace,itm_lance,itm_light_lance,itm_jarid,itm_tab_shield_small_round_a,
    itm_khergit_war_helmet,itm_khergit_helmet,itm_tribal_warrior_outfit,itm_nomad_boots,itm_leather_covered_round_shield,itm_saddle_horse,itm_steppe_horse,itm_steppe_horse],
   def_attrib|str_12|agi_12|level(15),wp(140),knows_riding_6|knows_shield_3|knows_horse_archery_3|knows_power_throw_3|knows_power_strike_4,khergit_face_young_1, khergit_face_old_2],

  ["steppe_bandit_leader","Steppe Leader","Steppe Leaders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_sword_khergit_1,itm_winged_mace,itm_lance,itm_jarid,itm_tab_shield_small_round_a,
    itm_khergit_war_helmet,itm_khergit_helmet,itm_lamellar_vest_khergit,itm_khergit_leather_boots,itm_courser],
   def_attrib|str_15|agi_12|level(18),wp(170),knows_riding_8|knows_shield_4|knows_horse_archery_4|knows_power_throw_5|knows_power_strike_5,khergit_face_young_1, khergit_face_old_2],

###### 		Taiga Bandits	##########  
  ["taiga_bandit","Taiga Bandit","Taiga Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear, itm_light_lance,itm_nomad_bow,itm_nomad_bow,itm_short_bow,itm_jarid,itm_javelin,itm_vaegir_fur_cap,itm_leather_steppe_cap_c,itm_nomad_armor,itm_leather_jerkin,itm_hide_boots,itm_nomad_boots,itm_leather_covered_round_shield,itm_leather_covered_round_shield],
   def_attrib|level(15),wp(110),knows_common|knows_power_draw_4|knows_power_throw_3,vaegir_face_young_1, vaegir_face_old_2],
###### 		Desert Bandits	########## 
  ["desert_bandit","Desert Bandit","Desert Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_arrows,itm_spiked_mace,itm_spear, itm_light_lance,itm_jarid,itm_nomad_bow,itm_short_bow,itm_jarid,
    itm_sarranid_cloth_robe, itm_skirmisher_armor, itm_desert_turban, itm_turban,itm_leather_covered_round_shield,itm_saddle_horse,itm_arabian_horse_a],
   def_attrib|level(12),wp(100),knows_riding_3|knows_horse_archery_3|knows_power_draw_3|knows_shield_2|knows_power_throw_2,khergit_face_young_1, khergit_face_old_2],
  
  ["desert_horse_archer","Desert Horse Archer","Desert Horse Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_arrows,itm_arabian_sword_a,itm_spiked_mace,itm_nomad_bow,itm_strong_bow,
    itm_archers_vest,itm_skirmisher_armor, itm_desert_turban, itm_turban,itm_leather_covered_round_shield,itm_saddle_horse,itm_arabian_horse_a],
   def_attrib|str_12|agi_10|level(15),wp(120),knows_riding_4|knows_power_throw_3|knows_horse_archery_5|knows_power_draw_5|knows_power_strike_1|knows_shield_3,khergit_face_young_1, khergit_face_old_2],

  ["desert_horse_warrior","Desert Warrior","Desert Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_lance,itm_arabian_sword_a,itm_winged_mace,itm_sarranid_mace_1, itm_lance,itm_jarid,itm_scimitar,
    itm_archers_vest,itm_skirmisher_armor,itm_sarranid_warrior_cap,itm_leather_gloves,itm_sarranid_boots_a,itm_sarranid_boots_b, itm_desert_turban, itm_turban,itm_leather_covered_round_shield,itm_saddle_horse,itm_arabian_horse_a],
   def_attrib|str_15|agi_12|level(15),wp(140),knows_riding_5|knows_power_throw_4|knows_horse_archery_3|knows_power_draw_3|knows_power_strike_3|knows_shield_4,khergit_face_young_1, khergit_face_old_2],

  ["desert_bandits_leader","Desert Bandits Leader","Desert Bandits Leaders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_arabian_sword_a,itm_lance,itm_scimitar,itm_sarranid_two_handed_axe_a,itm_sarranid_two_handed_axe_b,itm_sarranid_two_handed_mace_1,
    itm_sarranid_helmet1,itm_sarranid_mail_coif,itm_saracen_helmet_c,itm_saracen_lamellar_a,itm_sarranid_cavalry_robe,itm_sarranid_boots_b,itm_leather_gloves,itm_leather_covered_round_shield,itm_arabian_horse_b],
   def_attrib|str_18|agi_12|level(18),wp(180),knows_riding_7|knows_horse_archery_3|knows_power_throw_5|knows_power_draw_3|knows_power_strike_5|knows_shield_4,khergit_face_young_1, khergit_face_old_2],
 
 ################ SWAMP BANDITS
 
  ["swamp_bandit","Swamp Bandit","Swamp Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_hunting_bow,itm_bolts,itm_hunting_crossbow,itm_axe,itm_falchion,itm_boar_spear,itm_one_handed_war_axe_a,itm_spiked_club,itm_long_spiked_club,itm_falchion_c,itm_fur_covered_shield,itm_hide_covered_round_shield,itm_darts,
    itm_leather_cap,itm_leather_cap,itm_leather_cap,itm_skullcap,itm_coarse_tunic,itm_rawhide_coat,itm_hide_boots,itm_wrapping_boots],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_2|knows_shield_2|knows_athletics_2,rhodok_face_young_1, rhodok_face_old_2],
 
  ["swamp_archer","Swamp Bandit Archer","Swamp Bandit Archers",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_short_bow,itm_strong_bow,itm_mace_2,itm_falchion,itm_one_handed_war_axe_a,itm_fighting_pick,
    itm_leather_cap,itm_skullcap,itm_ragged_outfit,itm_leather_scale_armor,itm_leather_jerkin,itm_hide_boots,itm_nomad_boots],
   def_attrib|str_12|agi_10|level(15),wp(120)|wp_archery(150),knows_common|knows_power_draw_4|knows_power_strike_1|knows_athletics_4,rhodok_face_young_1, rhodok_face_old_2],

  ["swamp_warrior","Swamp Bandit Warrior","Swamp Bandit Warriors",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_falchion,itm_fighting_pick,itm_spear,itm_one_handed_battle_axe_a,itm_winged_mace,itm_mace_2,itm_battle_axe,itm_war_darts,itm_javelin,itm_leather_covered_round_shield,itm_hide_covered_round_shield,
    itm_helmet_with_neckguard,itm_nasal_helmet,itm_padded_cloth_c,itm_leather_scale_armor,itm_nomad_boots,itm_leather_boots],
   def_attrib|str_15|agi_12|level(15),wp(140),knows_common|knows_power_draw_2|knows_power_strike_4|knows_shield_4|knows_athletics_4,rhodok_face_young_1, rhodok_face_old_2],

  ["swamp_leader","Swamp Bandit Leader","Swamp Bandit Leaders",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_grosse_messer_a,itm_grosse_messer_b,itm_war_axe,itm_javelin,itm_boar_spear,itm_fur_covered_shield,itm_hide_covered_round_shield,
    itm_chapel_de_fer_b,itm_banded_armor_b,itm_kettle_hat_g,itm_brigandine_black_a,itm_hose_kneecops_red,itm_mail_gloves],
   def_attrib|str_18|agi_15|level(18),wp(180),knows_common|knows_power_draw_2|knows_power_strike_6|knows_shield_4|knows_athletics_4,rhodok_face_young_1, rhodok_face_old_2],

  ["troop_1","Troop","Troop",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws, [],
   def_attrib|str_18|agi_15|level(18),wp(180),knows_common|knows_power_draw_2|knows_power_strike_6|knows_shield_4|knows_athletics_4,rhodok_face_young_1, rhodok_face_old_2],
  
  ["black_khergit_horseman","Black Khergit Horseman","Black Khergit Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
   [itm_arrows,itm_sword_khergit_2,itm_scimitar,itm_scimitar,itm_winged_mace,itm_spear,itm_lance,itm_khergit_bow,itm_khergit_bow,itm_nomad_bow,itm_nomad_bow,itm_steppe_cap,itm_nomad_cap,itm_khergit_war_helmet,itm_khergit_war_helmet,itm_mail_hauberk,itm_lamellar_armor,itm_hide_boots,itm_plate_covered_round_shield,itm_plate_covered_round_shield,itm_saddle_horse,itm_steppe_horse],
   def_attrib|level(21),wp(100),knows_riding_3|knows_ironflesh_3|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],

  ["manhunter","Manhunter","Manhunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_mace_3,itm_winged_mace,itm_nasal_helmet,itm_padded_cloth,itm_aketon_green,itm_aketon_green,itm_wooden_shield,itm_nomad_boots,itm_wrapping_boots,itm_sumpter_horse],
   def_attrib|level(10),wp(50),knows_common,bandit_face1, bandit_face2],
##  ["deserter","Deserter","Deserters",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_swadian_deserters,
##   [itm_arrows,itm_spear,itm_fighting_pick,itm_short_bow,itm_sword,itm_voulge,itm_nordic_shield,itm_round_shield,itm_kettle_hat,itm_leather_cap,itm_padded_cloth,itm_leather_armor,itm_scale_armor,itm_saddle_horse],
##   def_attrib|level(12),wp(60),knows_common,bandit_face1, bandit_face2],

#fac_slavers
##  ["slave_keeper","Slave Keeper","Slave Keepers",tf_guarantee_armor ,0,0,fac_slavers,
##   [itm_cudgel,itm_club,itm_woolen_cap,itm_rawhide_coat,itm_coarse_tunic,itm_nomad_armor,itm_nordic_shield,itm_nomad_boots,itm_wrapping_boots,itm_sumpter_horse],
##   def_attrib|level(10),wp(60),knows_common,bandit_face1, bandit_face2],
  ["slave_driver","Slave Driver","Slave Drivers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse ,0,0,fac_slavers,
   [itm_club_with_spike_head,itm_segmented_helmet,itm_tribal_warrior_outfit,itm_nordic_shield,itm_leather_boots,itm_leather_gloves,itm_khergit_leather_boots,itm_steppe_horse],
   def_attrib|level(14),wp(80),knows_common,bandit_face1, bandit_face2],
  ["slave_hunter","Slave Hunter","Slave Hunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac_slavers,
   [itm_winged_mace,itm_maul,itm_kettle_hat,itm_mail_shirt,itm_tab_shield_round_c,itm_leather_boots,itm_leather_gloves,itm_courser],
   def_attrib|level(18),wp(90),knows_common,bandit_face1, bandit_face2],
  ["slave_crusher","Slave Crusher","Slave Crushers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac_slavers,
   [itm_sledgehammer,itm_spiked_mace,itm_mail_hauberk,itm_bascinet_2,itm_bascinet_3,itm_mail_mittens,itm_tab_shield_round_d,itm_mail_chausses,itm_splinted_leather_greaves,itm_hunter],
   def_attrib|level(22),wp(110),knows_common|knows_riding_4|knows_power_strike_3,bandit_face1, bandit_face2],
  ["slaver_chief","Slaver Chief","Slaver Chiefs",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_slavers,
   [itm_military_hammer,itm_warhammer,itm_brigandine_red,itm_steel_shield,itm_scale_gauntlets,itm_mail_mittens,itm_guard_helmet,itm_plate_boots,itm_mail_boots,itm_warhorse],
   def_attrib|level(26),wp(130),knows_common|knows_riding_4|knows_power_strike_5,bandit_face1, bandit_face2],

#Rhodok tribal, Hunter, warrior, veteran, warchief






#  ["undead_walker","undead_walker","undead_walkers",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["undead_horseman","undead_horseman","undead_horsemen",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_undeads,
#   [], 
#   def_attrib|level(19),wp(100),knows_common,undead_face1, undead_face2],
#  ["undead_nomad","undead_nomad","undead_nomads",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
#   [], 
#   def_attrib|level(21),wp(100),knows_common|knows_riding_4,khergit_face1, khergit_face2],
#  ["undead","undead","undead",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["hell_knight","hell_knight","hell_knights",tf_undead|tf_allways_fall_dead|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_undeads,
#   [], 
#   def_attrib|level(23),wp(100),knows_common|knows_riding_3,undead_face1, undead_face2],



  ["follower_woman","Camp Follower","Camp Follower",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_nordic_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,itm_dress,itm_woolen_dress, itm_skullcap, itm_wrapping_boots],
   def_attrib|level(5),wp(70),knows_common,refugee_face1,refugee_face2],
  ["hunter_woman","Huntress","Huntresses",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_arrows,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_nordic_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,itm_dress,itm_leather_jerkin, itm_skullcap, itm_wrapping_boots],
   def_attrib|level(10),wp(85),knows_common|knows_power_strike_1,refugee_face1,refugee_face2],
  ["fighter_woman","Camp Defender","Camp Defenders",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_arrows,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_fur_covered_shield,itm_hide_covered_round_shield,itm_hatchet,itm_voulge,itm_mail_shirt,itm_byrnie, itm_skullcap, itm_wrapping_boots],
   def_attrib|level(16),wp(100),knows_common|knows_riding_3|knows_power_strike_2|knows_athletics_2|knows_ironflesh_1,refugee_face1,refugee_face2],
  ["sword_sister","Sword Sister","Sword Sisters",tf_female|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_commoners,
   [itm_bolts,itm_sword_medieval_b,itm_sword_khergit_3,itm_plate_covered_round_shield,itm_tab_shield_small_round_c, itm_crossbow,itm_plate_armor,itm_coat_of_plates,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_courser,itm_leather_gloves],
   def_attrib|level(22),wp(140),knows_common|knows_power_strike_3|knows_riding_5|knows_athletics_3|knows_ironflesh_2|knows_shield_2,refugee_face1,refugee_face2],

  ["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(45),knows_common,refugee_face1,refugee_face2],
  ["peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(40),knows_common,refugee_face1,refugee_face2],

 
  ["caravan_master","Caravan Master","Caravan Masters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,
   [itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,
    itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,
    itm_leather_jacket, itm_leather_cap],
   def_attrib|level(9),wp(100),knows_common|knows_riding_4|knows_ironflesh_3,mercenary_face_1, mercenary_face_2],

  ["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
   [itm_dress,itm_leather_boots],
   def_attrib|level(2),wp(50),knows_common|knows_riding_2,woman_face_1, woman_face_2],


#This troop is the troop marked as soldiers_end and town_walkers_begin
 ["town_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic,itm_fur_coat, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_arena_tunic_white, itm_leather_apron, itm_shirt, itm_arena_tunic_green, itm_arena_tunic_blue, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2],
 ["town_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["khergit_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_sarranid_felt_hat,itm_turban,itm_wrapping_boots,itm_khergit_leather_boots,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 ["khergit_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["sarranid_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_sarranid_felt_hat,itm_turban,itm_wrapping_boots,itm_sarranid_boots_a,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 ["sarranid_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_sarranid_common_dress, itm_sarranid_common_dress_b,itm_woolen_hose,itm_sarranid_boots_a, itm_sarranid_felt_head_cloth, itm_sarranid_felt_head_cloth_b],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
  
#This troop is the troop marked as town_walkers_end and village_walkers_begin
 ["village_walker_1","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_leather_vest, itm_leather_apron, itm_shirt, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_younger_1, man_face_older_2],
 ["village_walker_2","Villager","Villagers",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

#This troop is the troop marked as village_walkers_end and spy_walkers_begin
 ["spy_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_robe, itm_leather_apron, itm_shirt, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
 ["spy_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
# Ryan END

#This troop is the troop marked as spy_walkers_end
# Zendar
  ["tournament_master","Tournament Master","Tournament Master",tf_hero, scn_zendar_center|entry(1),reserved,  fac_commoners,[itm_nomad_armor,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["trainer","Trainer","Trainer",tf_hero, scn_zendar_center|entry(2),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x00000000000430c701ea98836781647f],
  ["Constable_Hareck","Constable Hareck","Constable Hareck",tf_hero, scn_zendar_center|entry(5),reserved,  fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x00000000000c41c001fb15234eb6dd3f],

# Ryan BEGIN
  ["Ramun_the_slave_trader","Ramun, the slave trader","Ramun, the slave trader",tf_hero, no_scene,reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x0000000fd5105592385281c55b8e44eb00000000001d9b220000000000000000],

  ["guide","Quick Jimmy","Quick Jimmy",tf_hero, no_scene,0,  fac_commoners,[itm_coarse_tunic,itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c318301f24e38a36e38e3],
# Ryan END

  ["Xerina","Xerina","Xerina",tf_hero|tf_female, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|str_15|agi_15|level(39),wp(312),knows_power_strike_5|knows_ironflesh_5|knows_riding_6|knows_power_draw_4|knows_athletics_8|knows_shield_3,0x00000001ac0820074920561d0b51e6ed00000000001d40ed0000000000000000],
  ["Dranton","Dranton","Dranton",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|str_15|agi_14|level(42),wp(324),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000],
  ["Kradus","Kradus","Kradus",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_padded_leather,itm_hide_boots],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000],


#Tutorial
  ["tutorial_trainer","Training Ground Master","Training Ground Master",tf_hero, 0, 0, fac_commoners,[itm_robe,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["tutorial_student_1","{!}tutorial_student_1","{!}tutorial_student_1",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_2","{!}tutorial_student_2","{!}tutorial_student_2",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_3","{!}tutorial_student_3","{!}tutorial_student_3",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_4","{!}tutorial_student_4","{!}tutorial_student_4",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],

#Sargoth
  #halkard, hardawk. lord_taucard lord_caupard. lord_paugard

#Salt mine
  ["Galeas","Galeas","Galeas",tf_hero, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x000000000004718201c073191a9bb10c],

#Dhorak keep

  ["farmer_from_bandit_village","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_linen_tunic,itm_coarse_tunic,itm_shirt,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],

  ["trainer_1","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_1|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000d0d1030c74ae8d661b651c6840000000000000e220000000000000000],
  ["trainer_2","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_2|entry(6),reserved,  fac_commoners,[itm_nomad_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e5a04360428ec253846640b5d0000000000000ee80000000000000000],
  ["trainer_3","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_3|entry(6),reserved,  fac_commoners,[itm_padded_leather,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e4a0445822ca1a11ab1e9eaea0000000000000f510000000000000000],
  ["trainer_4","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_4|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e600452c32ef8e5bb92cf1c970000000000000fc20000000000000000],
  ["trainer_5","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_5|entry(6),reserved,  fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e77082000150049a34c42ec960000000000000e080000000000000000],

# Ransom brokers.
  ["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_red_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_3","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_5","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_bookseller_1","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots,
               itm_book_tactics, itm_book_persuasion, itm_book_wound_treatment_reference, itm_book_leadership, 
               itm_book_intelligence, itm_book_training_reference, itm_book_surgery_reference],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_bookseller_2","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots,
               itm_book_wound_treatment_reference, itm_book_leadership, itm_book_intelligence, itm_book_trade, 
               itm_book_engineering, itm_book_weapon_mastery],def_attrib|level(5),wp(20),knows_common,merchant_face_1, merchant_face_2],

# Tavern minstrel.
  ["tavern_minstrel_1","Wandering Minstrel","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_leather_jacket, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute
  ["tavern_minstrel_2","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_tunic_with_green_cape, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],  #early harp/lyre
  ["tavern_minstrel_3","Wandering Ashik","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_nomad_robe, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute/oud or rebab
  ["tavern_minstrel_4","Wandering Skald","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_fur_coat, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #No instrument or lyre
  ["tavern_minstrel_5","Wandering Troubadour","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_short_tunic, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #Lute or Byzantine/Occitan lyra
  
#NPC system changes begin
#Companions
  ["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],

  ["npc1","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_armor,itm_nomad_boots,itm_knife],
   str_8|agi_7|int_12|cha_7|level(3),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_linen_tunic,itm_hide_boots,itm_club],
   str_7|agi_7|int_11|cha_6|level(1),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_dress,itm_woolen_hose,itm_knife],
   str_6|agi_9|int_11|cha_6|level(1),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_jerkin,itm_nomad_boots, itm_sword_medieval_a],
   str_10|agi_9|int_13|cha_10|level(10),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_vest,itm_nomad_boots, itm_sword_khergit_1],
   str_9|agi_9|int_12|cha_7|level(5),wp(90),knows_warrior_npc|
   knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_nomad_boots, itm_sword_medieval_a],
   str_10|agi_12|int_10|cha_5|level(6),wp(105),knows_warrior_npc|
   knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_ragged_outfit,itm_wrapping_boots, itm_hunting_bow, itm_arrows, itm_staff],
   str_8|agi_9|int_10|cha_6|level(2),wp(80),knows_tracker_npc|
   knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tribal_warrior_outfit,itm_nomad_boots, itm_sword_viking_1],
   str_9|agi_10|int_9|cha_10|level(7),wp(90),knows_warrior_npc|
   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_nomad_boots, itm_sword_medieval_b_small],
   str_11|agi_8|int_7|cha_8|level(2),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_padded_leather,itm_nomad_boots, itm_crossbow, itm_bolts, itm_pickaxe],
   str_12|agi_8|int_9|cha_11|level(9),wp(105),knows_warrior_npc|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_apron, itm_falchion, itm_wrapping_boots],
   str_8|agi_11|int_10|cha_10|level(8),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_pilgrim_disguise,itm_nomad_boots, itm_staff],
   str_8|agi_7|int_13|cha_7|level(4),wp(30),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_robe,itm_nomad_boots, itm_scimitar, itm_courser],
   str_7|agi_7|int_12|cha_8|level(3),wp(80),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nobleman_outfit,itm_nomad_boots, itm_sword_medieval_b_small],
   str_9|agi_8|int_11|cha_8|level(5),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_rich_outfit,itm_nomad_boots, itm_sword_medieval_b_small],
   str_9|agi_9|int_12|cha_8|level(7),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_peasant_dress,itm_nomad_boots, itm_dagger, itm_throwing_knives],
   str_7|agi_11|int_8|cha_7|level(2),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],
#NPC system changes end


#governers olgrel rasevas                                                                        Horse          Bodywear                Footwear_in                     Footwear_out                    Armor                       Weapon                  Shield                  Headwaer
  ["kingdom_1_lord",  "King Dawo",  "Dawo",  tf_hero, 0,reserved,  fac_kingdom_1,[itm_warhorse,   itm_courtly_outfit,        itm_woolen_hose,                  itm_splinted_greaves_spurs,               itm_polish_transitional_armor, itm_gloves_a,    itm_longsword_b,      itm_triangle_shield,       itm_crowned_helmet],          knight_attrib_5,wp(360),knight_skills_5, 0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000,swadian_face_older_2],
  ["kingdom_2_lord",  "King Hetman",  "Hetman",  tf_hero, 0,reserved,  fac_kingdom_2,[itm_courtly_outfit,      itm_leather_boots,              itm_rus_cav_boots,              itm_kuyak_a, itm_wisby_gauntlets_black,      itm_steel_pick,      itm_tab_shield_kite_cav_b,      itm_norman_helmet_d],    knight_attrib_5,wp(360),knight_skills_5, 0x0000000ec50001400a2269f919dee11700000000001cc57d0000000000000000, vaegir_face_old_2],
  ["kingdom_3_lord",  "Sultan Azap",  "Azap",  tf_hero, 0,reserved,  fac_kingdom_3,[itm_courser,   itm_nomad_robe,  itm_leather_boots,            itm_splinted_greaves,           itm_khergit_guard_armor,  itm_lamellar_gauntlets,       itm_sword_khergit_3,              itm_tab_shield_small_round_c,       itm_guard_helmet],      knight_attrib_5,wp(360),knight_skills_5, 0x0000000cee0051cc44be2d14d370c65c00000000001ed6df0000000000000000,khergit_face_old_2],
  ["kingdom_4_lord",  "Queen Margaret",  "Margaret",  tf_hero|tf_female, 0,reserved,  fac_kingdom_4,[itm_hunter,    itm_nobleman_outfit,    itm_leather_boots,              itm_mail_boots,                 itm_cuir_bouilli,   itm_gauntlets,    itm_great_axe,           itm_tab_shield_round_e,    itm_nordic_helmet],            knight_attrib_5,wp(360),knight_skills_5, 0x0000000189080005549c575aea691962000000000011dd270000000000000000, nord_face_older_2],
  ["kingdom_5_lord",  "King Nebun",  "Nebun",  tf_hero, 0,reserved,  fac_kingdom_5,[  itm_tabard,             itm_rus_shoes,                 itm_tribal_warrior_outfit, itm_transitional_heraldic, itm_leather_gloves,         itm_war_bow, itm_bodkin_arrows,	itm_bodkin_arrows,     itm_scimitar_b,    itm_tab_shield_heater_cav_b,        itm_vaegir_mask],         knight_attrib_4,wp(300),knight_skills_4|knows_shield_1|knows_power_draw_10, 0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000, rhodok_face_old_2],
  ["kingdom_6_lord",  "King Casimir",  "Casimir",  tf_hero, 0,reserved,  fac_kingdom_6,[itm_warhorse_b, itm_nobleman_outfit,    itm_transitional_heraldic,	itm_iron_greaves,       itm_great_helmet_k,  itm_plate_mittens,      itm_longsword_c,    itm_tab_shield_small_round_c],         knight_attrib_4,wp(220),knight_skills_5|knows_shield_1, 0x0000000a4b103354189c71d6d36e8ac00000000001e24eb0000000000000000, rhodok_face_old_2],
  ["kingdom_7_lord",  "King Atze",  "Atze",  tf_hero, 0,reserved,  fac_kingdom_7,[  itm_tabard,             itm_leather_boots,              itm_iron_greaves,   itm_coat_of_plates, itm_hourglass_gauntlets_b,         itm_sword_two_handed_a,         itm_tab_shield_heater_cav_b,        itm_nordic_warlord_helmet],         knight_attrib_4,wp(300),knight_skills_4|knows_shield_1, 0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000, rhodok_face_old_2],
  ["kingdom_8_lord",  "King Norr",  "Norr",  tf_hero, 0,reserved,  fac_kingdom_8,[   itm_nord_nobleman_outfit,    itm_leather_boots,              itm_mail_chausses,                 itm_coat_of_plates_blue,   itm_lamellar_gauntlets,    itm_nordic_nobleman_sword,           itm_tab_shield_round_e,    itm_nordic_warlord_helmet],            knight_attrib_5,wp(360),knight_skills_5, 0x0000000189080005549c575aea691962000000000011dd270000000000000000, nord_face_older_2],
  ["kingdom_9_lord",  "King Thorvic",  "Thorvic",  tf_hero, 0,reserved,  fac_kingdom_9,[ itm_saddle_horse,  itm_nord_nobleman_outfit,    itm_leather_boots,              itm_iron_greaves,                 itm_french_plate,   itm_hourglass_gauntlets_b,    itm_french_longsword,   itm_heavy_lance,        itm_tab_shield_heater_cav_b,    itm_visored_sallet_coif],            knight_attrib_5,wp(360),knight_skills_5, 0x0000000189080005549c575aea691962000000000011dd270000000000000000, nord_face_older_2],

#    Imbrea   Belinda Ruby Qaelmas Rose    Willow 
#  Alin  Ganzo            Zelka Rabugti
#  Qlurzach Ruhbus Givea_alsev  Belanz        Bendina  
# Dunga        Agatha     Dibus Crahask
  
#                                                                               Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield
  #Swadian civilian clothes: itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit itm_short_tunic itm_tabard
  #Older knights with higher skills moved to top
  ["knight_1_1", "Count Radon", "Radon", tf_hero, 0, reserved,  fac_kingdom_1, [	      itm_courtly_outfit,      itm_kuyak_a,   itm_nomad_boots, itm_rus_cav_boots,       itm_novogrod_helmet,   itm_hourglass_gauntlets_b,        itm_warhammer_b         ,itm_tab_shield_heater_cav_b],   																					knight_attrib_4,wp(260),knight_skills_4, 0x0000000c3e08601414ab4dc6e39296b200000000001e231b0000000000000000, swadian_face_older_2],
  ["knight_1_2", "Count Cahir", "Cahir", tf_hero, 0, reserved,  fac_kingdom_1, [		itm_red_gambeson,      itm_brigandine_red, itm_nomad_boots,  itm_splinted_greaves,   itm_byzantion_helmet_g,  itm_wisby_gauntlets_red,        itm_khergit_sword_two_handed_b,itm_tab_shield_heater_cav_b],       																						knight_attrib_5,wp(300),knight_skills_5, 0x0000000c0f0c320627627238dcd6599400000000001c573d0000000000000000, swadian_face_young_2],
  ["knight_1_3", "Count Dariusz", "Dariusz", tf_hero, 0, reserved,  fac_kingdom_1, [itm_courser,          itm_nobleman_outfit,     itm_surcoa_over_mail_and_plate_black,                 itm_leather_boots,          itm_splinted_greaves_spurs,        itm_visored_sallet_with_coif_b, itm_wisby_gauntlets_black,itm_cav_sword,itm_great_lance,	   itm_norman_shield_3],  	knight_attrib_4,wp(260),knight_skills_4, 0x0000000cb700210214ce89db276aa2f400000000001d36730000000000000000, swadian_face_young_2],
  ["knight_1_4", "Count Juras", "Juras", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,      itm_short_tunic,       itm_polish_transitional_armor,           itm_leather_boots,          itm_iron_greaves,                   itm_zitta_bascinet, itm_heavy_plate_gloves,       itm_nobleman_sword_b,  itm_heavy_lance,  itm_tab_shield_heater_cav_b],    					knight_attrib_4,wp(260),knight_skills_4, 0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000, swadian_face_older_2],
  ["knight_1_5", "Count Cichoszek", "Cichoszek", tf_hero, 0, reserved,  fac_kingdom_1, [itm_plated_charger,            itm_rich_outfit,        itm_polish_transitional_armor,itm_woolen_hose, itm_iron_greaves, itm_norman_pot_helmet, itm_gauntlets,         itm_nobleman_sword_b,itm_heavy_lance,    itm_tab_shield_heater_cav_b],      										knight_attrib_4,wp(260),knight_skills_4, 0x0000000c0c1064864ba34e2ae291992b00000000001da8720000000000000000, swadian_face_older_2],
  ["knight_1_6", "Count Bananek", "Bananek", tf_hero, 0, reserved,  fac_kingdom_1, [		itm_tabard,      itm_polish_transitional_armor,               itm_leather_boots,          itm_iron_greaves,                      itm_gotland_helmet_b, itm_gauntlets,  itm_greatsword_a,itm_tab_shield_heater_cav_b], 																knight_attrib_5,wp(300),knight_skills_5, 0x0000000c0a08038736db74c6a396a8e500000000001db8eb0000000000000000, swadian_face_older_2],
  ["knight_1_7", "Count Kanmir", "Kanmir", tf_hero, 0, reserved,  fac_kingdom_1, [          itm_tabard,      itm_swordsman_armor,               itm_leather_boots,          itm_hose_kneecops_red,                      itm_lithuanian_helmet, itm_plate_mittens, itm_kreigsmesser,itm_tab_shield_heater_cav_b], 																knight_attrib_5,wp(300),knight_skills_5, 0x0000000c1e001500589dae4094aa291c00000000001e37a80000000000000000, swadian_face_young_2],
  ["knight_1_8", "Count Longinus", "Longinus", tf_hero, 0, reserved,  fac_kingdom_1, [		itm_nobleman_outfit,     itm_surcoa_over_mail_and_plate_heraldic,                 itm_leather_boots,          itm_rus_cav_boots,        itm_great_helmet_f,  itm_mail_gauntlets,itm_military_hammer, itm_tab_shield_pavise_d],  													knight_attrib_4,wp(260),knight_skills_4, 0x0000000c330855054aa9aa431a48d74600000000001ed5240000000000000000, swadian_face_older_2],

  ["knight_1_9", "Count Miler", "Miler", tf_hero, 0, reserved,  fac_kingdom_1, [itm_courser,      itm_gambeson,     itm_lithuanian_ducal_armor,                 itm_blue_hose,              itm_splinted_greaves_spurs,                      itm_lithuanian_helmet,  itm_mail_gauntlets,     itm_cav_sword,   itm_tab_shield_heater_cav_b],    											knight_attrib_3,wp(220),knight_skills_3, 0x0000000c0f08000458739a9a1476199800000000001fb6f10000000000000000, swadian_face_old_2],
  ["knight_1_10", "Count Mungano", "Mungano", tf_hero, 0, reserved,  fac_kingdom_1, [itm_plated_charger,           itm_blue_gambeson,        itm_corrazina_red,                   itm_woolen_hose,            itm_iron_greaves,                   itm_zitta_bascinet,    itm_hourglass_gauntlets_a,    itm_cav_sword, itm_great_lance,      itm_tab_shield_heater_cav_b],   			knight_attrib_3,wp(220),knight_skills_3, 0x0000000c0610351048e325361d7236cd00000000001d532a0000000000000000, swadian_face_older_2],
  ["knight_1_11", "Count Leper", "Leper", tf_hero, 0, reserved,  fac_kingdom_1, [		           itm_red_gambeson,      itm_churburg_b,               itm_nomad_boots,            itm_iron_greaves,                    itm_sugarloaf_a,   itm_hourglass_gauntlets_b,       itm_flambard_a		,itm_tab_shield_heater_cav_b		],       											knight_attrib_5,wp(300),knight_skills_5, 0x0000000c03104490280a8cb2a24196ab00000000001eb4dc0000000000000000, swadian_face_older_2],
  ["knight_1_12", "Count Nazgul", "Nazgul", tf_hero, 0, reserved,  fac_kingdom_1, [				itm_rich_outfit,        itm_lithuanian_lamellar,                    itm_nomad_boots,            itm_mail_chausses,                      itm_lithuanian_helmet,   itm_mail_gauntlets,         itm_steel_pick,   itm_lithuanian_shield],    												knight_attrib_3,wp(220),knight_skills_3, 0x0000000c2a0805442b2c6cc98c8dbaac00000000001d389b0000000000000000, swadian_face_older_2],
  ["knight_1_13", "Count Czarniecki", "Czarniecki", tf_hero, 0, reserved,  fac_kingdom_1, [ 	      itm_ragged_outfit,      itm_surcoa_over_mail_and_plate_heraldic,           itm_nomad_boots,            itm_norman_shoes,                itm_zitta_bascinet,   itm_mail_gloves,         itm_steel_pick,     itm_tab_shield_pavise_d],   											knight_attrib_3,wp(220),knight_skills_3, 0x0000000c380c30c2392a8e5322a5392c00000000001e5c620000000000000000, swadian_face_older_2],
  ["knight_1_14", "Count Raven", "Raven", tf_hero, 0, reserved,  fac_kingdom_1, [     itm_short_tunic,       itm_brigandine_red_b,           itm_leather_boots,          itm_hose_kneecops_red,                   itm_gotland_helmet_b,  itm_mail_gloves,     itm_steel_pick,    itm_tab_shield_pavise_d],    													knight_attrib_2,wp(180),knight_skills_2, 0x0000000c3f10000532d45203954e192200000000001e47630000000000000000, swadian_face_older_2],
  ["knight_1_15", "Count Matafiks", "Matafiks", tf_hero, 0, reserved,  fac_kingdom_1, [	           itm_rich_outfit,        itm_churburg_c,                   itm_woolen_hose,            itm_shynbaulds,                   itm_pigface_klappvisier,   itm_hourglass_gauntlets_b,       itm_morningstar_a,itm_tab_shield_heater_cav_b],      											knight_attrib_3,wp(220),knight_skills_3, 0x0000000c5c0840034895654c9b660c5d00000000001e34530000000000000000, swadian_face_young_2],
  ["knight_1_16", "Lady Aela", "Aela", tf_hero|tf_female, 0, reserved,  fac_kingdom_1, [itm_courser,		    itm_courtly_outfit,      itm_kaftan_over_mail_c,                     itm_nomad_boots,            itm_mail_chausses,                itm_lithuanian_helmet,   itm_gloves_a,         itm_sword_khergit_3   ,itm_tab_shield_small_round_c       ],   	knight_attrib_5,wp(300),knight_skills_5, 0x000000095108144657a1ba3ad456e8cb00000000001e325a0000000000000000, swadian_face_young_2],
  ["knight_1_17", "Count Akford", "Akford", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_gambeson,     itm_brigandine_red_c,                 itm_blue_hose,              itm_hose_kneecops_red,                      itm_kettle_hat_d,   itm_mail_gloves,    itm_nobleman_sword_b,   itm_tab_shield_heater_cav_a],   												knight_attrib_1,wp(120),knight_skills_1, 0x0000000c010c42c14d9d6918bdb336e200000000001dd6a30000000000000000, swadian_face_young_2],
  ["knight_1_18", "Count Mieszko", "Mieszko", tf_hero, 0, reserved,  fac_kingdom_1, [itm_courser,           itm_blue_gambeson,        itm_brigandine_white_a,                   itm_woolen_hose,            itm_hose_kneecops_green,                   itm_nasal_helmet_c,   itm_mail_gloves,    itm_nobleman_sword_a, itm_lance,         itm_tab_shield_heater_cav_a],   				knight_attrib_1,wp(120),knight_skills_1, 0x0000000c150045c6365d8565932a8d6400000000001ec6940000000000000000, swadian_face_young_2],
  ["knight_1_19", "Count GoodBass", "GoodBass", tf_hero, 0, reserved,  fac_kingdom_1, [		      itm_rich_outfit,        itm_surcoat_over_mail_heraldic,                    itm_nomad_boots,            itm_rus_cav_boots,                      itm_nasal_helmet_c, itm_mail_gloves,           itm_poleaxe_d,itm_tab_shield_heater_cav_b ],    											knight_attrib_1,wp(120),knight_skills_1, 0x00000008200012033d9b6d4a92ada53500000000001cc1180000000000000000, swadian_face_young_2],
  ["knight_1_20", "Lady Ewa*", "Ewa", tf_hero|tf_female, 0, reserved,  fac_kingdom_1, [itm_courser,      itm_ragged_outfit,      itm_kaftan_over_mail_c,           itm_nomad_boots,            itm_mail_chausses,                itm_lithuanian_helmet, itm_gloves_a,           itm_sword_khergit_3,   itm_tab_shield_small_round_c],   												knight_attrib_2,wp(180),knight_skills_2, 0x000000019f0c100128a276c295663b5a000000000016a7640000000000000000, swadian_face_young_2],


#                                                                             Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield
  
  ["knight_2_1", "Grey Harpag", "Harpag", tf_hero, 0, reserved,  fac_kingdom_2, [	itm_fur_coat,     itm_kuyak_a,                   itm_nomad_boots,            itm_rus_cav_boots,        itm_chapel_de_fer_g,    itm_wisby_gauntlets_black,       itm_byzantine_spathion,           itm_triangle_shield],    																	knight_attrib_3,wp(220),knight_skills_3, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],
  ["knight_2_2", "Grey Gryfita", "Gryfita", tf_hero, 0, reserved,  fac_kingdom_2, [		itm_rich_outfit,        itm_milanese_armour,               itm_woolen_hose,            itm_shynbaulds,             itm_milanese_sallet,	itm_hourglass_gauntlets_b,      itm_long_maul,	itm_tab_shield_heater_cav_b],    																	knight_attrib_5,wp(220),knight_skills_3, 0x0000000c2a0015d249b68b46a98e176400000000001d95a40000000000000000, vaegir_face_old_2],
  ["knight_2_3", "Grey Erasmas", "Erasmas", tf_hero, 0, reserved,  fac_kingdom_2, [		itm_short_tunic,        itm_milanese_armour,                   itm_woolen_hose,            itm_iron_greaves,		itm_sugarloaf_a, itm_hourglass_gauntlets_b,           itm_morningstar,	itm_tab_shield_heater_cav_b],     															knight_attrib_5,wp(220),knight_skills_3, 0x0000000c131031c546a38a2765b4c86000000000001e58d30000000000000000, vaegir_face_older_2],
  ["knight_2_4", "Grey Pawiu", "Pawiu", tf_hero, 0, reserved,  fac_kingdom_2, [		itm_courtly_outfit,     itm_transitional_heraldic,               itm_leather_boots,          itm_iron_greaves,                      itm_winged_great_helmet,	 itm_wisby_gauntlets_red,         itm_poleaxe_d,itm_tab_shield_heater_cav_b],    											knight_attrib_5,wp(300),knight_skills_5, 0x0000000c2f0832c748f272540d8ab65900000000001d34e60000000000000000, vaegir_face_older_2],
  ["knight_2_5", "Grey Danior", "Danior", tf_hero, 0, reserved,  fac_kingdom_2, [		itm_rich_outfit,        itm_kuyak_b,                     itm_leather_boots,          itm_rus_cav_boots,                   itm_tagancha_helmet_a, itm_plate_mittens,   itm_sword_viking_a_long,   itm_tab_shield_heater_cav_b],       													knight_attrib_5,wp(300),knight_skills_5, 0x0000000e310061435d76bb5f55bad9ad00000000001ed8ec0000000000000000, vaegir_face_older_2],
  ["knight_2_6", "Grey Melsar", "Melsar", tf_hero, 0, reserved,  fac_kingdom_2, [		itm_nomad_vest,      itm_mail_shirt_with_fur,                   itm_woolen_hose,            itm_rus_shoes,                   itm_nasal_helmet,  itm_mail_gauntlets,          itm_military_pick, itm_sniper_crossbow, itm_steel_bolts,itm_tab_shield_kite_cav_b],    					knight_attrib_1,wp(120),knight_skills_1, 0x0000000a0100421038da7157aa4e430a00000000001da8bc0000000000000000, vaegir_face_middle_2],
  ["knight_2_7", "Grey ObiWan*", "ObiWan", tf_hero, 0, reserved,  fac_kingdom_2, [ 		itm_leather_jacket,     itm_kuyak_a,                   itm_leather_boots,          itm_rus_cav_boots,                      itm_norman_helmet_c,  itm_hourglass_gauntlets_a,          itm_ranseur,itm_tab_shield_heater_cav_b],     														knight_attrib_4,wp(260),knight_skills_4, 0x0000000c04100153335ba9390b2d277500000000001d89120000000000000000, vaegir_face_old_2],
  ["knight_2_8", "Grey Jacu", "Jacu", tf_hero, 0, reserved,  fac_kingdom_2, [		itm_nomad_robe,             itm_surcoa_over_mail_and_plate_heraldic,                     itm_woolen_hose,            itm_rus_cav_boots,                   itm_zitta_bascinet, itm_hourglass_gloves,       itm_scimitar_b,    itm_tab_shield_kite_cav_b],    								knight_attrib_4,wp(260),knight_skills_4, 0x0000000c00046581234e8da2cdd248db00000000001f569c0000000000000000, vaegir_face_older_2],
  ["knight_2_9", "Grey Kalp", "Kalp", tf_hero, 0, reserved,  fac_kingdom_2, [		itm_rich_outfit,        itm_milanese_armour,                     itm_leather_boots,          itm_shynbaulds,                   itm_sugarloaf_a,  itm_hourglass_gauntlets_b,        itm_great_bardiche,   itm_tab_shield_kite_d],    														knight_attrib_5,wp(300),knight_skills_5, 0x0000000c160451d2136469c4d9b159ad00000000001e28f10000000000000000, vaegir_face_older_2],
  ["knight_2_10", "Grey Nuuks", "Nuuks", tf_hero, 0, reserved,  fac_kingdom_2, [itm_warhorse,          itm_fur_coat,        itm_kuyak_b,               itm_woolen_hose,            itm_iron_greaves,                      itm_norman_helmet_d,  itm_hourglass_gauntlets_a,      itm_heavy_lance, itm_scimitar_b,   itm_tab_shield_kite_cav_b], 									knight_attrib_3,wp(220),knight_skills_3, 0x0000000f7c00520e66b76edd5cd5eb6e00000000001f691e0000000000000000, vaegir_face_older_2],
  ["knight_2_11", "Grey Kasztelan", "Kasztelan", tf_hero, 0, reserved,  fac_kingdom_2, [		itm_leather_jacket,     itm_mail_shirt_with_fur,                   itm_nomad_boots,            itm_rus_shoes,        itm_leather_gloves,           itm_sword_medieval_c_small, itm_long_bow , itm_bodkin_arrows, itm_bodkin_arrows,itm_tab_shield_heater_cav_b],    			knight_attrib_2,wpe(180,260,180,180),knight_skills_2|knows_power_draw_8, 0x0000000c1d0821d236acd6991b74d69d00000000001e476c0000000000000000, vaegir_face_middle_2],
  ["knight_2_12", "Grey JokeeQ", "JokeeQ", tf_hero, 0, reserved,  fac_kingdom_2, [itm_warhorse,      itm_rich_outfit,        itm_grey_tabard_over_mail_and_plate,               itm_woolen_hose,            itm_iron_greaves,                   itm_litchina_helmet,  itm_gilded_hourglass_gloves,      itm_heavy_lance,	itm_scimitar_b,    itm_tab_shield_kite_cav_b],    	knight_attrib_4,wp(260),knight_skills_4, 0x0000000c0f04024b2509d5d53944c6a300000000001d5b320000000000000000, vaegir_face_old_2],
  ["knight_2_13", "Grey Jaheira", "Jaheira", tf_hero, 0, reserved,  fac_kingdom_2, [		itm_short_tunic,        itm_transitional_heraldic,                   itm_woolen_hose,            itm_iron_greaves,                   itm_weimar_helmet,  itm_gauntlets,          itm_long_axe,           itm_tab_shield_kite_cav_b],     											knight_attrib_4,wp(260),knight_skills_4, 0x0000000c680432d3392230cb926d56ca00000000001da69b0000000000000000, vaegir_face_older_2],
  ["knight_2_14", "Grey Nogu", "Nogu", tf_hero, 0, reserved,  fac_kingdom_2, [		itm_courtly_outfit,     itm_kuyak_a,               itm_leather_boots,          itm_rus_cav_boots,                      itm_norman_helmet_d,  itm_mail_gloves,        itm_one_handed_bar_mace,   itm_tab_shield_kite_d],    																	knight_attrib_5,wp(300),knight_skills_5, 0x0000000c27046000471bd2e93375b52c00000000001dd5220000000000000000, vaegir_face_older_2],
  ["knight_2_15", "Grey Opset", "Opset", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,            itm_rich_outfit,        itm_kuyak_b,                     itm_leather_boots,          itm_rus_cav_boots,                   itm_great_helmet, itm_mail_gloves,   itm_great_lance,  itm_military_hammer, itm_tab_shield_kite_cav_a],       									knight_attrib_2,wp(180),knight_skills_2, 0x0000000de50052123b6bb36de5d6eb7400000000001dd72c0000000000000000, vaegir_face_older_2],
#  ["knight_2_16", "Grey Redbul", "Redbul", tf_hero, 0, reserved,  fac_kingdom_2, [		itm_nomad_vest,      itm_kuyak_a,                   itm_woolen_hose,            itm_hose_kneecops_red,                   itm_gnezdovo_helmet,  itm_mail_gauntlets,          itm_sword_medieval_d_long,           itm_tab_shield_kite_c],   												knight_attrib_4,wp(260),knight_skills_4, 0x000000085f00000539233512e287391d00000000001db7200000000000000000, vaegir_face_middle_2],
  ["knight_2_16", "Grey Tamra", "Tamra", tf_hero|tf_female, 0, reserved,  fac_kingdom_2, [		itm_nomad_vest,      itm_varangopoulos_armor,                   itm_woolen_hose,            itm_shynbaulds,                   itm_visored_sallet_coif,  itm_gloves_a,          itm_great_long_bardiche,           itm_tab_shield_kite_c],   									knight_attrib_4,wp(260),knight_skills_4, 0x000000003f003006461b6db6da6904d800000000001c36430000000000000000, vaegir_face_middle_2],
  ["knight_2_17", "Grey Sraka", "Sraka", tf_hero, 0, reserved,  fac_kingdom_2, [		itm_leather_jacket,     itm_kuyak_a,                   itm_leather_boots,          itm_iron_greaves,                      itm_open_sallet,   itm_mail_gauntlets,         itm_great_long_bardiche,    itm_tab_shield_kite_cav_a],     													knight_attrib_4,wp(260),knight_skills_4, 0x0000000a070c4387374bd19addd2a4ab00000000001e32cc0000000000000000, vaegir_face_old_2],
  ["knight_2_18", "Grey Varadin", "Varadin", tf_hero, 0, reserved,  fac_kingdom_2, [	itm_nomad_robe,             itm_grey_tabard_over_mail_and_plate,                     itm_woolen_hose,            itm_iron_greaves,                   itm_visored_sallet_coif,  itm_hourglass_gauntlets_a,      itm_great_bardiche,    itm_tab_shield_kite_cav_a],    					knight_attrib_5,wp(360),knight_skills_5, 0x0000000b670012c23d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_older_2],
  ["knight_2_19", "Lady Angelica", "Angelica", tf_hero|tf_female, 0, reserved,  fac_kingdom_2, [		itm_rich_outfit,        itm_ritterbruder_armor,                     itm_leather_boots,          itm_iron_greaves,                   itm_litchina_helmet, itm_mail_gauntlets,         itm_steel_pick,   itm_tab_shield_pavise_d],    									knight_attrib_1,wp(120),knight_skills_1, 0x0000000195041001249291328d4d36cc000000000016bf1c0000000000000000, vaegir_face_older_2],
  ["knight_2_20", "Grey Hasul", "Hasul", tf_hero, 0, reserved,  fac_kingdom_2, [itm_warhorse_steppe,          itm_fur_coat,        itm_byrnie,               itm_woolen_hose,            itm_hose_kneecops_red,                      itm_litchina_helmet,  itm_gilded_hourglass_gloves,      itm_heavy_lance,	itm_scimitar ,   itm_tab_shield_kite_cav_a],     				knight_attrib_3,wp(220),knight_skills_3, 0x0000000f800021c63b0a6e4994ae272a00000000001db4e10000000000000000, vaegir_face_older_2],

#                                                                               Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield
 
 #khergit civilian clothes: itm_leather_vest, itm_nomad_vest, itm_nomad_robe, itm_lamellar_vest,itm_tribal_warrior_outfit
  ["knight_3_1", "Vercngetorix Noyan", "Vercngetorix", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_leather_vest,  itm_sipahi_jawshan,itm_nomad_boots,  itm_sarranid_boots_c, itm_ottoman_elite_cavalry_chichak, itm_lamellar_gauntlets,  itm_heavy_lance,itm_arabian_sword_d, itm_tab_shield_small_round_c],  	knight_attrib_5,wp(300),knight_skills_5, 0x000000043000318b54b246b7094dc39c00000000001d31270000000000000000, khergit_face_middle_2],
  ["knight_3_2", "Dodosa Noyan",  "Dodosa", tf_hero, 0, reserved,  fac_kingdom_3, [		itm_nomad_vest,   itm_heavy_yawshan, itm_hide_boots,  itm_sarranid_boots_c, itm_ghulam_helmet_a, itm_scale_gloves_a, itm_sarranid_axe_b,  itm_plate_covered_round_shield], 															knight_attrib_5,wp(300),knight_skills_5, 0x0000000c280461004929b334ad632aa200000000001e05120000000000000000, khergit_face_old_2],
  ["knight_3_3", "Hunefa Noyan",  "Hunefa", tf_hero, 0, reserved,  fac_kingdom_3, [		itm_nomad_robe, itm_saracen_lamellar_a,itm_nomad_boots,  itm_sarranid_boots_b,  itm_ottoman_elite_cavalry_chichak, itm_scale_gloves_b, itm_scimitar_b,  itm_tab_shield_kite_c],  													knight_attrib_4,wp(260),knight_skills_4, 0x0000000e880062c53b0a6e4994ae272a00000000001db4e10000000000000000, khergit_face_older_2],
  ["knight_3_4", "Marji Noyan", "Marji", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_lamellar_vest_khergit,  itm_saracen_mail_a, itm_hide_boots,  itm_sarranid_boots_d,   itm_saracen_helmet_c, itm_scale_gloves_b, itm_sarranid_cavalry_sword, itm_lance,  itm_tab_shield_small_round_c],  					knight_attrib_3,wp(220),knight_skills_3, 0x0000000c23085386391b5ac72a96d95c00000000001e37230000000000000000, khergit_face_older_2],
  ["knight_3_5", "Denis Noyan",  "Denis", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_ragged_outfit,  itm_heavy_yawshan, itm_hide_boots,  itm_sarranid_boots_c, itm_saracen_helmet_c, itm_lamellar_gauntlets, itm_sarranid_cavalry_sword, itm_lance, itm_tab_shield_small_round_c], 							knight_attrib_4,wp(260),knight_skills_4, 0x0000000efe0051ca4b377b4964b6eb6500000000001f696c0000000000000000, khergit_face_older_2],
  ["knight_3_6", "PARADOX1 Noyan", "PARADOX1", tf_hero, 0, reserved,  fac_kingdom_3, [		itm_nomad_robe,itm_saracen_lamellar_a,itm_hide_boots, itm_sarranid_boots_d,  itm_ghulam_helmet_a,  itm_scale_gloves_a, itm_ashwood_pike,  itm_tab_shield_small_round_b], 														knight_attrib_1,wp(130),knight_skills_1, 0x00000006f600418b54b246b7094dc31a00000000001d37270000000000000000, khergit_face_middle_2],
  ["knight_3_7", "Moment Noyan","Moment", tf_hero, 0, reserved,  fac_kingdom_3, [		itm_leather_vest,itm_saracen_mail_a,itm_leather_boots, itm_sarranid_boots_d, itm_ghulam_helmet_a, itm_scale_gloves_a,  itm_sarranid_two_handed_axe_a, itm_tab_shield_small_round_b], 												knight_attrib_4,wp(260),knight_skills_4, 0x0000000bdd00510a44be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_old_2],
  ["knight_3_8", "Blooodaxe Noyan", "Blooodaxe", tf_hero, 0, reserved,  fac_kingdom_3, [		itm_nomad_vest, itm_saracen_lamellar_a, itm_woolen_hose, itm_sarranid_boots_b, itm_ottoman_chichak, itm_scale_gauntlets,   itm_sarranid_two_handed_mace_1,  itm_tab_shield_small_round_c],  								knight_attrib_3,wp(220),knight_skills_3, 0x0000000abc00518b5af4ab4b9c8e596400000000001dc76d0000000000000000, khergit_face_older_2],
  ["knight_3_9", "Tomayus Noyan","Tomayus", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse,  itm_nomad_robe, itm_arabian_armor_b,  itm_leather_boots, itm_sarranid_boots_d,  itm_saracen_helmet_d, itm_scale_gloves_b,  itm_arabian_sword_b,itm_lance,  itm_tab_shield_small_round_c],  								knight_attrib_5,wp(300),knight_skills_5, 0x0000000a180441c921a30ea68b54971500000000001e54db0000000000000000, khergit_face_older_2],
  ["knight_3_10", "ONUR Noyan","ONUR", tf_hero, 0, reserved,  fac_kingdom_3, [		itm_lamellar_vest_khergit, itm_arabian_armor_b, itm_hide_boots, itm_sarranid_boots_c,  itm_sarranid_mail_coif, itm_lamellar_gauntlets,  itm_sarranid_two_handed_axe_b,  itm_tab_shield_small_round_c], 									knight_attrib_4,wp(260),knight_skills_4, 0x0000000a3b00418c5b36c686d920a76100000000001c436f0000000000000000, khergit_face_older_2],
  ["knight_3_11", "TigirER Noyan", "TigirER", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_leather_vest, itm_sarranid_mail_shirt, itm_nomad_boots, itm_sarranid_boots_d,  itm_sarranid_mail_coif,  itm_scale_gloves_a, itm_sarranid_mace_1,itm_lance,  itm_tab_shield_small_round_b],  							knight_attrib_3,wp(220),knight_skills_3, 0x00000007d100534b44962d14d370c65c00000000001ed6df0000000000000000, khergit_face_middle_2],
  ["knight_3_12", "Lapis Noyan", "Lapis", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_nomad_vest, itm_saracen_mail_c, itm_hide_boots, itm_sarranid_boots_b,  itm_saracen_helmet_d,  itm_scale_gloves_a, itm_scimitar_b,itm_lance,  itm_tab_shield_small_round_b], 												knight_attrib_3,wp(220),knight_skills_3, 0x0000000bf400610c5b33d3c9258edb6c00000000001eb96d0000000000000000, khergit_face_old_2],
  ["knight_3_13", "Aygir Noyan","Aygir", tf_hero, 0, reserved,  fac_kingdom_3, [		itm_nomad_robe,  itm_sarranid_cavalry_robe, itm_nomad_boots, itm_sarranid_boots_b,  itm_sarranid_helmet1, itm_leather_gloves, itm_sarranid_axe_a,  itm_tab_shield_small_round_b],  													knight_attrib_3,wp(220),knight_skills_3, 0x0000000bfd0061c65b6eb33b25d2591d00000000001f58eb0000000000000000, khergit_face_older_2],
  ["knight_3_14", "Feronia Noyan",  "Feronia", tf_hero, 0, reserved,  fac_kingdom_3, [	itm_ragged_outfit,	itm_arabian_armor_a2, itm_hide_boots, itm_sarranid_boots_d, itm_saracen_helmet_b, itm_scale_gloves_b, itm_hafted_blade_a,  itm_tab_shield_small_round_c],  														knight_attrib_5,wp(300),knight_skills_5, 0x0000000b6900514144be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_older_2],
  ["knight_3_15", "Karatekeli Noyan", "Karatekeli", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse,   itm_ragged_outfit, itm_saracen_mail_b, itm_hide_boots, itm_sarranid_boots_b,  itm_saracen_helmet_b, itm_scale_gloves_b ,itm_sarranid_cavalry_sword, itm_plate_covered_round_shield],  							knight_attrib_2,wp(180),knight_skills_2, 0x0000000c360c524b6454465b59b9d93500000000001ea4860000000000000000, khergit_face_older_2],
  ["knight_3_16", "Sipahi Noyan","Sipahi", tf_hero, 0, reserved,  fac_kingdom_3, [		itm_tribal_warrior_outfit,  itm_saracen_mail_b,  itm_hide_boots,  itm_sarranid_boots_d,  itm_saracen_helmet_d, itm_scale_gloves_b,   itm_scimitar, itm_tab_shield_kite_d],  														knight_attrib_2,wp(180),knight_skills_2, 0x0000000c350c418438ab85b75c61b8d300000000001d21530000000000000000, khergit_face_middle_2],
  ["knight_3_17", "Turkpromaster Noyan", "Turkpromaster", tf_hero, 0, reserved,  fac_kingdom_3, [		itm_leather_vest, itm_saracen_mail_a, itm_leather_boots, itm_sarranid_boots_d, itm_saracen_helmet_d, itm_scale_gloves_b,   itm_hafted_blade_b, itm_tab_shield_small_round_c],  										knight_attrib_1,wp(120),knight_skills_1, 0x0000000c3c0821c647264ab6e68dc4d500000000001e42590000000000000000, khergit_face_old_2],
  ["knight_3_18", "Glaxor Noyan", "Glaxor", tf_hero, 0, reserved,  fac_kingdom_3, [		itm_nomad_vest, itm_saracen_mail_a, itm_hide_boots, itm_sarranid_boots_b,  itm_janissary_boerk_b, itm_leather_gloves,   itm_sarranid_axe_b, itm_strong_bow, itm_khergit_arrows,itm_tab_shield_small_round_b],   													knight_attrib_5,wp(300),knight_skills_5|knows_power_draw_7, 0x0000000c0810500347ae7acd0d3ad74a00000000001e289a0000000000000000, khergit_face_older_2],
  ["knight_3_19", "Lykiaa Noyan","Lykiaa", tf_hero, 0, reserved,  fac_kingdom_3, [		itm_nomad_robe, itm_saracen_mail_c, itm_leather_boots, itm_sarranid_boots_b,  itm_ottoman_chichak, itm_leather_gloves, itm_sarranid_mace_1,itm_strong_bow, itm_bodkin_arrows,itm_tab_shield_small_round_b],  													knight_attrib_4,wp(260),knight_skills_4|knows_power_draw_5, 0x0000000c1500510528f50d52d20b152300000000001d66db0000000000000000, khergit_face_older_2],
  ["knight_3_20", "Noshimuri Noyan","Noshimuri", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_lamellar_vest, itm_sarranid_cavalry_robe, itm_hide_boots, itm_sarranid_boots_b, itm_sarranid_mail_coif, itm_leather_gloves, itm_arabian_sword_a, itm_tab_shield_small_round_b],  									knight_attrib_1,wp(120),knight_skills_1, 0x0000000f7800620d66b76edd5cd5eb6e00000000001f691e0000000000000000, khergit_face_older_2],
 

  ["knight_4_1", "Jarl Arn", "Arn", tf_hero, 0, reserved,  fac_kingdom_4, [		itm_rich_outfit,  itm_heraldic_mail_with_tabard,   itm_woolen_hose,  itm_mail_boots,  itm_barbuta_2, itm_hourglass_gauntlets_b,	 itm_ashwood_pike,	itm_tab_shield_round_d], 																	knight_attrib_5,wp(300),knight_skills_5, 0x0000000c13002254340eb1d91159392d00000000001eb75a0000000000000000, nord_face_middle_2],
  ["knight_4_2", "Jarl Mr K*", "Mr K*", tf_hero, 0, reserved,  fac_kingdom_4, [ 	itm_short_tunic,  	itm_plate_armor_c, 	itm_blue_hose,  	itm_iron_greaves, itm_great_bascinet_a, itm_hourglass_gauntlets_a,  itm_long_axe_c,  itm_tab_shield_round_d], 																	knight_attrib_5,wp(300),knight_skills_5, 0x0000000c1610218368e29744e9a5985b00000000001db2a10000000000000000, nord_face_old_2],
  ["knight_4_3", "Jarl Larvae", "Larvae", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter, itm_rich_outfit,  itm_transitional_heraldic,   itm_nomad_boots,  itm_iron_greaves,	itm_great_helmet_i, itm_hourglass_gauntlets_a,      itm_military_cleaver_c, itm_tab_shield_heater_cav_b],  										knight_attrib_5,wp(300),knight_skills_5, 0x0000000c03040289245a314b744b30a400000000001eb2a90000000000000000, nord_face_older_2],
  ["knight_4_4", "Jarl Crojo", "Crojo", tf_hero, 0, reserved,  fac_kingdom_4, [		itm_leather_vest,   itm_surcoa_over_mail_and_plate_blue,   itm_woolen_hose,  itm_iron_greaves,	itm_great_helmet_h, itm_hourglass_gauntlets_a,   itm_glaive2, itm_tab_shield_round_e],  													knight_attrib_5,wp(300),knight_skills_5, 0x0000000c3f1001ca3d6955b26a8939a300000000001e39b60000000000000000, nord_face_older_2],
  ["knight_4_5", "Jarl Granny", "Granny", tf_hero, 0, reserved,  fac_kingdom_4, [	  itm_fur_coat,   itm_banded_armor,   itm_leather_boots,  itm_splinted_leather_greaves, itm_great_bascinet_a, itm_hourglass_gauntlets_a,  itm_one_handed_warhammer, itm_plate_covered_round_shield], 										knight_attrib_4,wp(260),knight_skills_4, 0x0000000ff508330546dc4a59422d450c00000000001e51340000000000000000, nord_face_older_2],
  ["knight_4_6", "Jarl Woody", "Woody", tf_hero, 0, reserved,  fac_kingdom_4, [  	 itm_nomad_robe,   itm_corrazina_grey,  itm_nomad_boots,  itm_shynbaulds,   itm_pigface_klappvisier, itm_wisby_gauntlets_red,   itm_great_axe, itm_tab_shield_round_d],   																	knight_attrib_3,wp(220),knight_skills_3, 0x00000005b00011813d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_middle_2],
  ["knight_4_7", "Jarl WolvenSpirit", "WolvenSpirit", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_fur_coat,   itm_brigandine_blue_a,   itm_nomad_boots,  itm_hose_kneecops_red,  itm_kettle_hat_f, itm_mail_gloves,   itm_long_bow, itm_bodkin_arrows,itm_bodkin_arrows, itm_fighting_pick,  itm_tab_shield_round_d],  		knight_attrib_3,wpe(160,260,180,180),knight_skills_3|knows_power_draw_8, 0x00000006690002873d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_old_2],
  ["knight_4_8", "Jarl Odysseus*", "Odysseus", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse,	itm_rich_outfit,  itm_transitional_heraldic,   itm_woolen_hose,  itm_splinted_greaves_spurs,   itm_great_helmet_i, itm_gauntlets, itm_morningstar,  itm_tab_shield_heater_cav_b],   										knight_attrib_2,wp(120),knight_skills_1, 0x0000000f830051c53b026e4994ae272a00000000001db4e10000000000000000, nord_face_older_2],
  ["knight_4_9", "Jarl GTX", "GTX", tf_hero, 0, reserved,  fac_kingdom_4, [		itm_nomad_robe,   itm_lamellar_armor, itm_blue_hose,  itm_rus_splint_greaves,  itm_nordic_warlord_helmet, itm_scale_gauntlets,   itm_sword_of_war,  itm_tab_shield_round_e],  																	knight_attrib_5,wp(300),knight_skills_5, 0x00000000080c54c1345bd21349b1b67300000000001c90c80000000000000000, nord_face_older_2],
  ["knight_4_10", "Jarl Phreak", "Phreak", tf_hero, 0, reserved,  fac_kingdom_4, [   itm_courtly_outfit,   itm_surcoa_over_mail_and_plate_heraldic,   itm_nomad_boots,  itm_hose_kneecops_green, itm_wisby_gloves_red,  itm_morion_a,itm_two_handed_cleaver, itm_tab_shield_round_e],  											knight_attrib_4,wp(260),knight_skills_4, 0x000000084b0002063d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_older_2],
  ["knight_4_11", "Jarl Telford", "Telford", tf_hero, 0, reserved,  fac_kingdom_4, [itm_courser, itm_rich_outfit,  itm_surcoa_over_mail_and_plate_yellow,   itm_woolen_hose,  itm_iron_greaves,  itm_great_helmet_d,  itm_hourglass_gauntlets_a,  itm_heavy_lance,itm_military_hammer, itm_tab_shield_heater_cav_b], 			knight_attrib_4,wp(260),knight_skills_4, 0x000000002d100005471d4ae69ccacb1d00000000001dca550000000000000000, nord_face_middle_2],
  ["knight_4_12", "Jarl Wiltzu", "Wiltzu", tf_hero, 0, reserved,  fac_kingdom_4, [ 	itm_short_tunic,  itm_surcoat_over_mail_heraldic, itm_blue_hose,  itm_hose_kneecops_red,  itm_nordic_warlord_helmet,  itm_mail_gauntlets,  itm_one_handed_battle_axe_c,  itm_tab_shield_round_d],  											knight_attrib_4,wp(260),knight_skills_4, 0x0000000b9500020824936cc51cb5bb2500000000001dd4d80000000000000000, nord_face_old_2],
  ["knight_4_13", "Jarl Frank", "Frank", tf_hero, 0, reserved,  fac_kingdom_4, [	itm_rich_outfit,  itm_black_armor_b,   itm_nomad_boots,  itm_splinted_greaves_spurs,	itm_morion_b,  itm_wisby_gloves_red,     itm_danish_greatsword, itm_tab_shield_round_e],  															knight_attrib_4,wp(260),knight_skills_4, 0x0000000a300012c439233512e287391d00000000001db7200000000000000000, nord_face_older_2],
  ["knight_4_14", "Lady Alimalia*", "Alimalia", tf_hero|tf_female, 0, reserved,  fac_kingdom_4, [  itm_leather_vest,   itm_brigandine_red_c,   itm_woolen_hose,  itm_hose_kneecops_red,  itm_kettle_hat_e, itm_leather_gloves, itm_military_cleaver_b,itm_long_bow,itm_bodkin_arrows,itm_bodkin_arrows, itm_tab_shield_round_e],knight_attrib_3,wp(220),knight_skills_3, 0x00000001bb0000013ae39737148e14b4000000000009c9490000000000000000, nord_face_older_2],
  ["knight_4_15", "Jarl Reymann", "Reymann", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_leather_jacket,   itm_brigandine_red_b,   itm_leather_boots,  itm_hose_kneecops_red,  itm_klappvisier,	itm_wisby_gauntlets_red, itm_lance,itm_falchion_c, itm_tab_shield_heater_cav_a], 								knight_attrib_3,wp(220),knight_skills_3, 0x0000000d920801831715d1aa9221372300000000001ec6630000000000000000, nord_face_older_2],
  ["knight_4_16", "Jarl Syggelekokle", "Syggelekokle", tf_hero, 0, reserved,  fac_kingdom_4, [  	 itm_nomad_robe,   itm_brigandine_blue,  itm_nomad_boots,  itm_hose_kneecops_green,   itm_kettle_hat_f, itm_mail_gauntlets,   itm_ashwood_pike, itm_tab_shield_round_d],   													knight_attrib_3,wp(220),knight_skills_3, 0x000000099700124239233512e287391d00000000001db7200000000000000000, nord_face_middle_2],
  ["knight_4_17", "Jarl Lexie", "Lexie", tf_hero, 0, reserved,  fac_kingdom_4, [  	itm_fur_coat,   itm_black_armor_c,   itm_nomad_boots,  itm_hose_kneecops_red,  itm_great_bascinet_a, itm_wisby_gauntlets_red,   itm_warhammer,  itm_tab_shield_round_d],   																	knight_attrib_3,wp(180),knight_skills_2, 0x0000000c2f0442036d232a2324b5b81400000000001e55630000000000000000, nord_face_old_2],
  ["knight_4_18", "Jarl Jonasr", "Jonasr", tf_hero, 0, reserved,  fac_kingdom_4, [itm_saddle_horse, itm_rich_outfit,  itm_surcoa_over_mail_and_plate_blue,   itm_woolen_hose,  itm_hose_kneecops_green,   itm_klappvisier, itm_mail_gloves, itm_lance,itm_morningstar,  itm_tab_shield_heater_cav_a],   						knight_attrib_3,wp(180),knight_skills_2, 0x0000000c0d00118866e22e3d9735a72600000000001eacad0000000000000000, nord_face_older_2],
  ["knight_4_19", "Jarl Qodsonn", "QodsonN", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse, itm_nomad_robe,   itm_transitional_heraldic, itm_blue_hose,  itm_shynbaulds,  itm_great_helmet_d, itm_hourglass_gauntlets_a,   itm_lance,itm_one_handed_warhammer,  itm_tab_shield_heater_cav_b],  							knight_attrib_3,wp(120),knight_skills_1, 0x0000000c0308225124e26d4a6295965a00000000001d23e40000000000000000, nord_face_older_2],
  ["knight_4_20", "Jarl Eddy*", "Eddy", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_courtly_outfit,   itm_plate_armor_c,   itm_nomad_boots,  itm_iron_greaves,  itm_pigface_klappvisier, itm_hourglass_gauntlets_a,  itm_long_axe, itm_tab_shield_round_e],  														knight_attrib_3,wp(180),knight_skills_2, 0x0000000f630052813b6bb36de5d6eb7400000000001dd72c0000000000000000, nord_face_older_2],
 

  ["knight_5_1", "Count Vovka", "Vovka", tf_hero, 0, reserved,  fac_kingdom_5, [   itm_tabard,   itm_rus_scale_d,       itm_leather_boots,    itm_iron_greaves,    itm_litchina_helmet, itm_hourglass_gauntlets_b,     itm_steel_pick,   itm_tab_shield_kite_d],     																			knight_attrib_4,wp(260),knight_skills_4, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_5_2", "Count Oscar", "Oscar", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse_b,    itm_red_gambeson,       itm_rus_scale_b,    itm_leather_boots,    itm_shynbaulds,    itm_nikolskoe_helmet, itm_hourglass_gauntlets_b,      itm_scimitar_b,  itm_heavy_lance,   itm_tab_shield_kite_cav_b],     								knight_attrib_1,wp(120),knight_skills_1, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_5_3", "Count Archer", "Archer", tf_hero, 0, reserved,  fac_kingdom_5, [    itm_short_tunic,  itm_tribal_warrior_outfit,     itm_nomad_boots,      itm_kazakh_boots,  itm_nomad_cap, itm_leather_gloves, itm_war_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_one_handed_war_axe_b,  itm_tab_shield_kite_cav_b],    				knight_attrib_3,wpe(160,260,180,180),knight_skills_3|knows_power_draw_8, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_5_4", "Count Bars", "Bars", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_leather_jacket,     itm_rus_scale,       itm_woolen_hose,      itm_rus_splint_greaves,    itm_rus_helmet_b, itm_mail_gauntlets, itm_fauchard_fork,    itm_tab_shield_kite_d],    																		knight_attrib_5,wp(300),knight_skills_5, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_5_5", "Count Emperor", "Emperor", tf_hero, 0, reserved,  fac_kingdom_5, [  itm_rich_outfit,  itm_drz_elite_lamellar_armor,     itm_leather_boots,    itm_iron_greaves,    itm_norman_pot_helmet, itm_hourglass_gauntlets_a, itm_one_handed_warhammer,  itm_tab_shield_kite_d], 														knight_attrib_3,wp(220),knight_skills_3, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_5_6", "Count Eldar*", "Eldar", tf_hero, 0, reserved,  fac_kingdom_5, [    itm_ragged_outfit,      itm_tribal_warrior_outfit,       itm_woolen_hose,      itm_leather_boots,	itm_byzantion_helmet_g,  itm_leather_gloves,       itm_military_hammer, itm_war_bow, itm_bodkin_arrows, itm_bodkin_arrows,   itm_tab_shield_kite_d],    knight_attrib_4,wpe(160,260,180,180),knight_skills_4|knows_power_draw_8, 0x000000001100000648d24d36cd964b1d00000000001e2dac0000000000000000, rhodok_face_middle_2],
  ["knight_5_7", "Count Autobus", "Autobus", tf_hero, 0, reserved,  fac_kingdom_5, [itm_courser,     itm_coarse_tunic,       itm_rus_scale_c,   itm_leather_boots,    itm_iron_greaves,  itm_gnezdovo_helmet,  itm_hourglass_gauntlets_b,           itm_heavy_lance, itm_scimitar_b,    itm_tab_shield_kite_cav_b],     						knight_attrib_4,wp(260),knight_skills_4, 0x0000000c3a0455c443d46e4c8b91291a00000000001ca51b0000000000000000, rhodok_face_old_2],
  ["knight_5_8", "Count Luke", "Luke", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter, itm_courtly_outfit,     itm_drz_lamellar_armor_b,    itm_woolen_hose,      itm_splinted_greaves,    itm_nikolskoe_helmet,  itm_mail_gauntlets,      itm_scimitar,  itm_tab_shield_kite_cav_a],    													knight_attrib_3,wp(220),knight_skills_3, 0x0000000c2c0844d42914d19b2369b4ea00000000001e331b0000000000000000, rhodok_face_older_2],
  ["knight_5_9", "Count Naduril", "Naduril", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse_b,     itm_leather_jacket,     itm_drz_lamellar_armor,   itm_leather_boots,    itm_iron_greaves,       itm_rus_helmet_b, itm_hourglass_gloves,   itm_heavy_lance, itm_bardiche,   itm_tab_shield_kite_cav_b],   								knight_attrib_5,wp(300),knight_skills_5, 0x00000000420430c32331b5551c4724a100000000001e39a40000000000000000, rhodok_face_older_2],
  ["knight_5_10", "Count Pepel", "Pepel", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_rich_outfit,  itm_transitional_heraldic,     itm_blue_hose,  itm_shynbaulds,       itm_tagancha_helmet_b, itm_hourglass_gauntlets_b,       itm_great_bardiche,   itm_tab_shield_kite_cav_a],  														knight_attrib_3,wp(220),knight_skills_3, 0x00000008e20011063d9b6d4a92ada53500000000001cc1180000000000000000, rhodok_face_older_2],
  ["knight_5_11", "Count Seka", "Seka", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_tabard,       itm_drz_mail_shirt,       itm_leather_boots,    itm_rus_cav_boots,    itm_spiked_helmet,  itm_mail_gauntlets,    itm_steel_pick,	itm_heavy_crossbow,	itm_steel_bolts,   itm_tab_shield_kite_c],     										knight_attrib_1,wpe(120,120,220,120),knight_skills_1, 0x0000000c170c14874752adb6eb3228d500000000001c955c0000000000000000, rhodok_face_middle_2],
  ["knight_5_12", "Count Slavimir", "Slavimir", tf_hero, 0, reserved,  fac_kingdom_5, [    itm_red_gambeson,       itm_drz_lamellar_armor_a,    itm_leather_boots,    itm_rus_splint_greaves,    itm_tagancha_helmet_a,  itm_mail_gauntlets,      itm_great_long_bardiche,   itm_tab_shield_kite_c],     										knight_attrib_2,wp(180),knight_skills_2, 0x0000000c080c13d056ec8da85e3126ed00000000001d4ce60000000000000000, rhodok_face_old_2],
  ["knight_5_13", "Count Kypak", "Kypak", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,     itm_short_tunic,  itm_kuyak_b,     itm_nomad_boots,      itm_rus_cav_boots,  itm_rus_helmet_b, itm_mail_gloves,       itm_light_lance,	itm_one_handed_war_axe_b,  itm_tab_shield_kite_cav_a],    												knight_attrib_3,wp(220),knight_skills_3, 0x0000000cbf10100562a4954ae731588a00000000001d6b530000000000000000, rhodok_face_older_2],
  ["knight_5_14", "Count Melendil", "Melendil", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_leather_jacket,     itm_kuyak_a,       itm_woolen_hose,      itm_rus_cav_boots,    itm_nikolskoe_helmet, itm_hourglass_gauntlets_b, itm_danish_greatsword,    itm_tab_shield_kite_c],    														knight_attrib_4,wp(260),knight_skills_4, 0x0000000c330805823baa77556c4e331a00000000001cb9110000000000000000, rhodok_face_older_2],
  ["knight_5_15", "Count Legolas", "Legolas", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_drz_kaftan,  itm_drz_kaftan,     itm_leather_boots,    itm_steppe_cap, itm_leather_gloves,       itm_scimitar, itm_war_bow , itm_bodkin_arrows, itm_bodkin_arrows,  itm_tab_shield_kite_c], 														knight_attrib_2,wpe(160,260,180,180),knight_skills_2|knows_power_draw_7, 0x0000000d51000106370c4d4732b536de00000000001db9280000000000000000, rhodok_face_older_2],
  ["knight_5_16", "Count Vitovt", "Vitovt", tf_hero, 0, reserved,  fac_kingdom_5, [    itm_ragged_outfit,      itm_studded_leather_coat,       itm_woolen_hose,      itm_splinted_leather_greaves,    itm_tagancha_helmet_a, itm_hourglass_gauntlets_a,     itm_warhammer,   itm_tab_shield_kite_c],    										knight_attrib_5,wp(300),knight_skills_5, 0x0000000c06046151435b5122a37756a400000000001c46e50000000000000000, rhodok_face_middle_2],
  ["knight_5_17", "Count NoobSaibot", "NoobSaibot", tf_hero, 0, reserved,  fac_kingdom_5, [itm_rus_horse,     itm_coarse_tunic,       itm_drz_mail_shirt,   itm_leather_boots,    itm_rus_cav_boots,       itm_rus_helmet_b,  itm_mail_gauntlets,      itm_lance, itm_scimitar,    itm_tab_shield_kite_cav_a],     								knight_attrib_4,wp(260),knight_skills_4, 0x0000000c081001d3465c89a6a452356300000000001cda550000000000000000, rhodok_face_old_2],
  ["knight_5_18", "Count Masalski", "Masalski", tf_hero, 0, reserved,  fac_kingdom_5, [ itm_courtly_outfit,     itm_norman_armor_a,    itm_woolen_hose,      itm_norman_shoes,    itm_norman_pot_helmet, itm_scale_gauntlets,       itm_one_handed_warhammer,   itm_norman_shield_3],    														knight_attrib_3,wp(180),knight_skills_3, 0x0000000a3d0c13c3452aa967276dc95c00000000001dad350000000000000000, rhodok_face_older_2],
  ["knight_5_19", "Count mrZhidovt*", "mrZhidovt", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_leather_jacket,     itm_drz_elite_lamellar_armor,   itm_leather_boots,    itm_iron_greaves,       itm_litchina_helmet, itm_hourglass_gauntlets_b,  itm_morningstar, itm_tab_shield_kite_c],   												knight_attrib_5,wp(300),knight_skills_5, 0x0000000038043194092ab4b2d9adb44c00000000001e072c0000000000000000, rhodok_face_older_2],
  ["knight_5_20", "Count Aleksey", "Aleksey", tf_hero, 0, reserved,  fac_kingdom_5, [     itm_rich_outfit,  itm_tribal_warrior_outfit,     itm_blue_hose,  itm_rus_shoes,       itm_litchina_helmet, itm_mail_gloves,       itm_bardiche,   itm_tab_shield_kite_c],  																			knight_attrib_5,wp(300),knight_skills_5, 0x000000003600420515a865b45c64d64c00000000001d544b0000000000000000, rhodok_face_older_2],
  
  
  ["knight_6_1", "Count Boby", "Boby", tf_hero, 0, reserved,  fac_kingdom_6, [	itm_courtly_outfit,itm_transitional_heraldic,          itm_leather_boots,    itm_steel_greaves_a,    itm_crusader_helmet_a, itm_hourglass_gauntlets_a,    itm_morningstar,   itm_tab_shield_small_round_c],     														knight_attrib_5,wp(300),knight_skills_5, 0x00000000600c2084486195383349eae500000000001d16a30000000000000000, rhodok_face_middle_2],
  ["knight_6_2", "Count TomMyyY*", "TomMyyY", tf_hero, 0, reserved,  fac_kingdom_6, [itm_barded_warhorse,   itm_courtly_outfit, itm_transitional_white,       itm_sarranid_boots_c,    itm_shynbaulds,    itm_great_helmet_c, itm_hourglass_gloves,   itm_heavy_lance,   itm_longsword_c,   itm_tab_shield_kite_cav_b],     							knight_attrib_5,wp(300),knight_skills_5, 0x00000001380825d444cb68b92b8d3b1d00000000001dd71e0000000000000000, rhodok_face_old_2],
  ["knight_6_3", "Count Vincent Ruth*", "Vincent", tf_hero, 0, reserved,  fac_kingdom_6, [itm_barded_warhorse,    itm_courtly_outfit, itm_surcoa_over_mail_and_plate_white,       itm_nomad_boots,      itm_crusader_face_plate_c, itm_mail_gauntlets, itm_crusader_sword,   itm_tab_shield_kite_cav_b],    												knight_attrib_4,wp(260),knight_skills_4, 0x000000002208428579723147247ad4e500000000001f14d40000000000000000, rhodok_face_older_2],
  ["knight_6_4", "Count Berg", "Berg", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saddle_horse,   itm_courtly_outfit,  itm_surcoa_over_mail_and_plate_heraldic,            itm_iron_greaves,          itm_helmet_a,	itm_mail_gloves,  itm_heavy_lance, itm_sword_medieval_c,    itm_tab_shield_kite_cav_a],    											knight_attrib_4,wp(260),knight_skills_4, 0x00000009bf084285050caa7d285be51a00000000001d11010000000000000000, rhodok_face_older_2],
  ["knight_6_5", "Count Medic", "Medic", tf_hero, 0, reserved,  fac_kingdom_6, [	itm_courtly_outfit, itm_surcoa_over_mail_and_plate_white,       itm_nomad_boots,	itm_iron_greaves,     itm_nasal_helmet_c, itm_mail_gauntlets, itm_sniper_crossbow, itm_steel_bolts, itm_steel_bolts, itm_military_hammer, itm_tab_shield_kite_d], 									knight_attrib_2,wpe(120,80,260,80),knight_skills_2, 0x000000002a084003330175aae175da9c00000000001e02150000000000000000, rhodok_face_older_2],
  ["knight_6_6", "Count Dolphin", "Dolphin", tf_hero, 0, reserved,  fac_kingdom_6, [	itm_courtly_outfit, itm_surcoa_over_mail_and_plate_heraldic,            itm_leather_boots,      itm_mail_chausses,    itm_chapel_de_fer_b, itm_heavy_crossbow, itm_steel_bolts,  itm_steel_bolts,   itm_sword_medieval_c,   itm_tab_shield_kite_d],    			knight_attrib_4,wp(260),knight_skills_4, 0x00000001830043834733294c89b128e200000000001259510000000000000000, rhodok_face_middle_2],
  ["knight_6_7", "Count Leprikon", "Leprikon", tf_hero, 0, reserved,  fac_kingdom_6, [itm_barded_warhorse, itm_courtly_outfit,    itm_transitional_heraldic,      itm_leather_boots,	itm_mail_chausses,    itm_steel_greaves_a,          itm_crusader_helmet_b,  itm_hourglass_gloves,     itm_crusader_sword,    itm_tab_shield_kite_cav_b],     							knight_attrib_3,wp(220),knight_skills_3, 0x0000000cbf10434020504bbbda9135d500000000001f62380000000000000000, rhodok_face_old_2],
  ["knight_6_8", "Count Thibaut de Champagne", "Thibaut de Champagne", tf_hero, 0, reserved,  fac_kingdom_6, [itm_barded_warhorse, itm_courtly_outfit, itm_surcoa_over_mail_and_plate_heraldic,         itm_leather_boots,      itm_iron_greaves,    itm_crusader_face_plate_b,  itm_hourglass_gloves,      itm_crusader_sword, itm_lance,  itm_tab_shield_kite_cav_b],    	knight_attrib_2,wp(180),knight_skills_2, 0x0000000190044003336dcd3ca2cacae300000000001f47640000000000000000, rhodok_face_older_2],
  ["knight_6_9", "Count Brede", "Brede", tf_hero, 0, reserved,  fac_kingdom_6, [	itm_courtly_outfit,itm_transitional_white,  itm_leather_boots,      itm_mail_and_plate_boots_a,    itm_crusader_face_plate_c, itm_hourglass_gauntlets_a,   itm_bec_de_corbin_a, itm_tab_shield_kite_cav_b],   														knight_attrib_3,wp(220),knight_skills_3, 0x0000000dde0040c4549dd5ca6f4dd56500000000001e291b0000000000000000, rhodok_face_older_2],
  ["knight_6_10", "Count Steevee", "Steevee", tf_hero, 0, reserved,  fac_kingdom_6, [	itm_courtly_outfit, itm_padded_cloth_c,       itm_woolen_hose,  itm_woolen_hose,     itm_chapel_de_fer_e, itm_leather_gloves,   itm_one_handed_battle_axe_a,     itm_long_bow, itm_bodkin_arrows, itm_bodkin_arrows,   itm_tab_shield_kite_cav_b],  			knight_attrib_3,wpe(120,260,80,80),knight_skills_3|knows_power_draw_8, 0x00000001a60441c66ce99256b4ad4b3300000000001d392c0000000000000000, rhodok_face_older_2],
  ["knight_6_11", "Count CossacK", "CossacK", tf_hero, 0, reserved,  fac_kingdom_6, [	itm_saddle_horse,    itm_courtly_outfit, itm_surcoa_over_mail_and_plate_white,              itm_woolen_hose,    itm_iron_greaves,    itm_crusader_face_plate_b,  itm_mail_gauntlets,    itm_crusader_sword,   itm_tab_shield_kite_cav_b],     					knight_attrib_4,wp(260),knight_skills_4, 0x0000000fff08134726c28af8dc96e4da00000000001e541d0000000000000000, rhodok_face_middle_2],
  ["knight_6_12", "Count Eskil", "Eskil", tf_hero, 0, reserved,  fac_kingdom_6, [   itm_padded_cloth, itm_padded_cloth,           itm_woolen_hose,    itm_woolen_hose,    itm_kettle_hat_g, itm_long_bow, itm_bodkin_arrows, itm_bodkin_arrows,    itm_fighting_pick,   itm_tab_shield_small_round_c],    											knight_attrib_1,wpe(80,180,60,60),knight_skills_1|knows_power_draw_6, 0x0000000035104084635b74ba5491a7a400000000001e46d60000000000000000, rhodok_face_old_2],
  ["knight_6_13", "Count Xardas", "Xardas", tf_hero, 0, reserved,  fac_kingdom_6, [    itm_courtly_outfit, itm_transitional_heraldic,       itm_woolen_hose,      itm_shynbaulds,  itm_great_helmet_c,   itm_hourglass_gauntlets_a,     itm_flamberge,  itm_tab_shield_small_round_c],    																knight_attrib_3,wp(220),knight_skills_3, 0x00000000001021435b734d4ad94eba9400000000001eb8eb0000000000000000, rhodok_face_older_2],
  ["knight_6_14", "Count Alpha", "Alpha", tf_hero, 0, reserved,  fac_kingdom_6, [    itm_courtly_outfit, itm_surcoat_over_mail_heraldic,       itm_woolen_hose,      itm_mail_chausses,    itm_segmented_helmet_b,   itm_one_handed_battle_axe_a,    itm_tab_shield_kite_d],    																		knight_attrib_2,wp(180),knight_skills_2, 0x000000000c0c45c63a5b921ac22db8e200000000001cca530000000000000000, rhodok_face_older_2],
  ["knight_6_15", "Count Grubby", "Grubby", tf_hero, 0, reserved,  fac_kingdom_6, [itm_courtly_outfit, itm_surcoat_over_mail_heraldic,       itm_woolen_hose,    itm_iron_greaves,    itm_segmented_helmet_b,  itm_longsword_c,  itm_tab_shield_kite_d], 																								knight_attrib_1,wp(120),knight_skills_1, 0x000000001b0c4185369a6938cecde95600000000001f25210000000000000000, rhodok_face_older_2], 
  ["knight_6_16", "Count Jacoob", "Jacoob", tf_hero, 0, reserved,  fac_kingdom_6, [  itm_courtly_outfit,  itm_surcoa_over_mail_and_plate_white,             itm_woolen_hose,      itm_iron_greaves,    itm_crusader_face_plate_a, itm_mail_gloves,    itm_warhammer,   itm_tab_shield_kite_d],    														knight_attrib_4,wp(260),knight_skills_4, 0x00000007770841c80a01e1c5eb51ffff00000000001f12d80000000000000000, rhodok_face_middle_2],
  ["knight_6_17", "Count PolePoop", "PolePoop", tf_hero, 0, reserved,  fac_kingdom_6, [   itm_courtly_outfit,  itm_transitional_heraldic,          itm_woolen_hose,    itm_steel_greaves_a,       itm_crusader_helmet_b,  itm_hourglass_gauntlets_a,      itm_poleaxe_d,    itm_tab_shield_kite_d],     												knight_attrib_5,wp(300),knight_skills_5, 0x000000007f0462c32419f47a1aba8bcf00000000001e7e090000000000000000, rhodok_face_old_2],
  ["knight_6_18", "Count Hawk*", "Hawk", tf_hero, 0, reserved,  fac_kingdom_6, [ itm_courtly_outfit, itm_surcoa_over_mail_and_plate_white,     itm_woolen_hose,      itm_iron_greaves,    itm_helmet_a,       itm_heavy_great_sword,   itm_tab_shield_kite_d],    																						knight_attrib_5,wp(300),knight_skills_5, 0x000000003410410070d975caac91aca500000000001c27530000000000000000, rhodok_face_older_2],
  ["knight_6_19", "Count Warder", "Warder", tf_hero, 0, reserved,  fac_kingdom_6, [   itm_courtly_outfit, itm_surcoa_over_mail_and_plate_heraldic,        itm_woolen_hose,    itm_mail_chausses,       itm_skullcap_c, itm_leather_gloves,   itm_war_spear, itm_large_shield],   																		knight_attrib_3,wp(220),knight_skills_3, 0x000000018a08618016ac36bc8b6e4a9900000000001dd45d0000000000000000, rhodok_face_older_2],
  ["knight_6_20", "Count Witch", "Witch", tf_hero, 0, reserved,  fac_kingdom_6, [itm_barded_warhorse,    itm_courtly_outfit, itm_surcoa_over_mail_and_plate_white,       itm_woolen_hose,  itm_iron_greaves,       itm_crusader_helmet_b,   itm_heavy_lance,      itm_crusader_sword,   itm_tab_shield_kite_cav_b],  									knight_attrib_5,wp(300),knight_skills_5, 0x00000001bd0040c0281a899ac956b94b00000000001ec8910000000000000000, rhodok_face_older_2],  

  ["knight_7_1", "Count Black_Bird", "Black_Bird", tf_hero, 0, reserved,  fac_kingdom_7, [itm_saddle_horse,   itm_tabard,   itm_heavy_gothic_armor_b,       itm_leather_boots,    itm_black_greaves,    itm_heavy_gothic_helmet_b, itm_wisby_gloves,     itm_morningstar,   itm_tab_shield_heater_cav_b],     										knight_attrib_5,wp(300),knight_skills_5, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_7_2", "Count Tomoenage", "Tomoenage", tf_hero, 0, reserved,  fac_kingdom_7, [   itm_red_gambeson,       itm_gothic_knightly_plate_b,    itm_leather_boots,    itm_black_greaves,    itm_visored_sallet_with_coif_b, itm_wisby_gloves,      itm_sword_two_handed_a,   itm_tab_shield_pavise_c],     										knight_attrib_5,wp(300),knight_skills_5, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_7_3", "Count Esca", "Esca", tf_hero, 0, reserved,  fac_kingdom_7, [     itm_short_tunic,  itm_padded_cloth_b,     itm_khergit_leather_boots,      itm_khergit_leather_boots,  itm_kettle_hat_i, itm_black_leather_gloves, itm_sniper_crossbow,	itm_steel_bolts,	itm_steel_bolts,	itm_grosse_messer_a,  itm_tab_shield_pavise_c],    			knight_attrib_3,wpe(160,80,260,80),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_7_4", "Count Hektor", "Hektor", tf_hero, 0, reserved,  fac_kingdom_7, [     itm_leather_jacket,     itm_coat_of_plates,       itm_woolen_hose,      itm_norman_shoes,    itm_great_helmet_b, itm_wisby_gloves_black, itm_long_axe_c,    itm_tab_shield_pavise_c],    																	knight_attrib_3,wp(220),knight_skills_3, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_7_5", "Count EtzelJO", "EtzelJO", tf_hero, 0, reserved,  fac_kingdom_7, [     itm_rich_outfit,  itm_transitional_black,     itm_leather_boots,    itm_norman_shoes,    itm_topfhelm, itm_wisby_gloves_red, itm_bec_de_corbin_a,  itm_tab_shield_pavise_c], 																				knight_attrib_4,wp(260),knight_skills_4, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_7_6", "Count Eragen", "Eragen", tf_hero, 0, reserved,  fac_kingdom_7, [itm_warhorse_b,    itm_ragged_outfit,      itm_plated_light_brigandine,       itm_woolen_hose,      itm_norman_shoes,    itm_topfhelm_b,	itm_wisby_gauntlets_black,     itm_heavy_lance,itm_sword_medieval_d_long,   itm_tab_shield_heater_cav_b],    			knight_attrib_3,wp(220),knight_skills_3, 0x000000001100000648d24d36cd964b1d00000000001e2dac0000000000000000, rhodok_face_middle_2],
  ["knight_7_7", "Count Vekk", "Vekk", tf_hero, 0, reserved,  fac_kingdom_7, [itm_hunter,     itm_coarse_tunic,       itm_ritterbruder_armor,   itm_leather_boots,    itm_norman_shoes,       itm_great_helmet_c, itm_bnw_gauntlets,       itm_lance,	itm_lombardic_sword,     itm_tab_shield_heater_cav_b],     									knight_attrib_3,wp(220),knight_skills_3, 0x0000000c3a0455c443d46e4c8b91291a00000000001ca51b0000000000000000, rhodok_face_old_2],
  ["knight_7_8", "Count Aprassimov", "Aprassimov", tf_hero, 0, reserved,  fac_kingdom_7, [ itm_courtly_outfit,     itm_heraldic_mail_with_tabard,    itm_woolen_hose,      itm_mail_chausses,    itm_chapel_de_fer_b,  itm_wisby_gauntlets_black,      itm_khergit_sword_two_handed_a,   itm_tab_shield_pavise_c],    								knight_attrib_4,wp(260),knight_skills_4, 0x0000000c2c0844d42914d19b2369b4ea00000000001e331b0000000000000000, rhodok_face_older_2],
  ["knight_7_9", "Count Falk", "Falk", tf_hero, 0, reserved,  fac_kingdom_7, [     itm_leather_jacket,     itm_banded_armor_b,   itm_leather_boots,    itm_iron_greaves,       itm_guard_helmet, itm_mail_gauntlets,   itm_poleaxe_c,    itm_tab_shield_pavise_c],   																				knight_attrib_4,wp(260),knight_skills_4, 0x00000000420430c32331b5551c4724a100000000001e39a40000000000000000, rhodok_face_older_2],
  ["knight_7_10", "Count Dirty_Maik", "Dirty_Maik", tf_hero, 0, reserved,  fac_kingdom_7, [     itm_rich_outfit,  itm_banded_armor_b,     itm_blue_hose,  itm_iron_greaves,       itm_gotland_helmet, itm_mail_gauntlets,       itm_bastard_sword_b,    itm_tab_shield_pavise_d],  																	knight_attrib_4,wp(260),knight_skills_4, 0x00000008e20011063d9b6d4a92ada53500000000001cc1180000000000000000, rhodok_face_older_2],
  ["knight_7_11", "Count HeGu", "HeGu", tf_hero, 0, reserved,  fac_kingdom_7, [     itm_tabard,       itm_heavy_gotland_armor,       itm_leather_boots,    itm_shynbaulds,    itm_gotland_helmet,  itm_gloves_a,    itm_one_handed_warhammer,    itm_tab_shield_pavise_d],     																		knight_attrib_2,wp(180),knight_skills_2, 0x0000000c170c14874752adb6eb3228d500000000001c955c0000000000000000, rhodok_face_middle_2],
  ["knight_7_12", "Count Quadri", "Quadri", tf_hero, 0, reserved,  fac_kingdom_7, [    itm_red_gambeson,       itm_surcoa_over_mail_and_plate_heraldic,    itm_leather_boots,    itm_norman_shoes,    itm_helmet_with_neckguard,  itm_wisby_gloves_black,      itm_bearded_axe,    itm_tab_shield_pavise_c],     									knight_attrib_2,wp(180),knight_skills_2, 0x0000000c080c13d056ec8da85e3126ed00000000001d4ce60000000000000000, rhodok_face_old_2],
  ["knight_7_13", "Count Sebb", "Sebb", tf_hero, 0, reserved,  fac_kingdom_7, [     itm_short_tunic,  itm_padded_cloth_b,     itm_turkish_shoes,      itm_turkish_shoes,  itm_chapel_de_fer_c, itm_black_leather_gloves,       itm_heavy_crossbow,	itm_steel_bolts,	itm_steel_bolts,	itm_mace_2,  itm_tab_shield_pavise_c],    				knight_attrib_1,wpe(80,60,180,60),knight_skills_1, 0x0000000cbf10100562a4954ae731588a00000000001d6b530000000000000000, rhodok_face_older_2],
  ["knight_7_14", "Count Tschinken", "Tschinken", tf_hero, 0, reserved,  fac_kingdom_7, [itm_warhorse_b,     itm_leather_jacket,     itm_heavy_gotland_armor,       itm_woolen_hose,      itm_norman_shoes,    itm_norman_pot_helmet, itm_mail_gauntlets, itm_heavy_lance,	itm_bastard_sword_b,     itm_tab_shield_heater_cav_b],    				knight_attrib_4,wp(260),knight_skills_4, 0x0000000c330805823baa77556c4e331a00000000001cb9110000000000000000, rhodok_face_older_2],
  ["knight_7_15", "Count Wayyyyyne", "Wayyyyyne", tf_hero, 0, reserved,  fac_kingdom_7, [     itm_rich_outfit,  itm_tribal_warrior_outfit,     itm_leather_boots,    itm_nomad_boots,    itm_nasal_helmet, itm_leather_gloves,       itm_german_greatsword,   itm_tab_shield_pavise_c], 															knight_attrib_5,wp(300),knight_skills_5, 0x0000000d51000106370c4d4732b536de00000000001db9280000000000000000, rhodok_face_older_2],
  ["knight_7_16", "Count Biene", "Biene", tf_hero, 0, reserved,  fac_kingdom_7, [    itm_ragged_outfit,      itm_brigandine_black_a,       itm_woolen_hose,      itm_hose_kneecops_red,    itm_chapel_de_fer_b, itm_mail_gauntlets,     itm_grosse_messer_a,    itm_tab_shield_pavise_c],    														knight_attrib_1,wp(120),knight_skills_1, 0x0000000c06046151435b5122a37756a400000000001c46e50000000000000000, rhodok_face_middle_2],
  ["knight_7_17", "Count AcEian", "AcEian", tf_hero, 0, reserved,  fac_kingdom_7, [itm_saddle_horse,     itm_coarse_tunic,       itm_surcoa_over_mail_and_plate_black,   itm_leather_boots,    itm_hose_kneecops_red,       itm_chapel_de_fer_b,  itm_wisby_gloves_black,      itm_grosse_messer_b,	itm_lance,    itm_tab_shield_heater_cav_a],     knight_attrib_3,wp(220),knight_skills_3, 0x0000000c081001d3465c89a6a452356300000000001cda550000000000000000, rhodok_face_old_2],
  ["knight_7_18", "Count NeXiN", "NeXiN", tf_hero, 0, reserved,  fac_kingdom_7, [ itm_courtly_outfit,     itm_brigandine_black,    itm_woolen_hose,      itm_hose_kneecops_red,    itm_chapel_de_fer_e, itm_mail_gloves,       itm_great_axe,    itm_tab_shield_pavise_c],    																		knight_attrib_1,wp(120),knight_skills_1, 0x0000000a3d0c13c3452aa967276dc95c00000000001dad350000000000000000, rhodok_face_older_2],
  ["knight_7_19", "Count Jogel", "Jogiel", tf_hero, 0, reserved,  fac_kingdom_7, [     itm_leather_jacket,     itm_transitional_black,   itm_leather_boots,    itm_iron_greaves,       itm_guard_helmet, itm_wisby_gloves_black,   itm_grosse_messer_a, itm_tab_shield_round_e],   																	knight_attrib_5,wp(300),knight_skills_5, 0x0000000038043194092ab4b2d9adb44c00000000001e072c0000000000000000, rhodok_face_older_2],
  ["knight_7_20", "Count Habi", "Habi", tf_hero, 0, reserved,  fac_kingdom_7, [    itm_rich_outfit,  itm_rus_scale,     itm_blue_hose,  itm_rus_cav_boots,       itm_nikolskoe_helmet, itm_scale_gauntlets,       itm_hafted_blade_a,    itm_tab_shield_pavise_c],  																				knight_attrib_5,wp(300),knight_skills_5, 0x000000003600420515a865b45c64d64c00000000001d544b0000000000000000, rhodok_face_older_2],  
  
  ["knight_8_1", "Jarl Gjallar", "Gjallar", tf_hero, 0, reserved,  fac_kingdom_8, [		itm_rich_outfit,  itm_banded_armor_b,   itm_woolen_hose,  itm_norman_shoes,  itm_gjermundbu_helmet, itm_lamellar_gauntlets,	 itm_long_axe_c,	itm_tab_shield_round_e], 																			knight_attrib_5,wp(300),knight_skills_5, 0x0000000c13002254340eb1d91159392d00000000001eb75a0000000000000000, nord_face_middle_2],
  ["knight_8_2", "Jarl Torr", "Torr", tf_hero, 0, reserved,  fac_kingdom_8, [ 	itm_short_tunic,  	itm_banded_armor, 	itm_blue_hose,  itm_nomad_boots,	itm_splinted_leather_greaves, itm_gjermundbu_helmet, itm_mail_gauntlets,itm_nordic_nobleman_sword,  itm_tab_shield_round_e], 																							knight_attrib_5,wp(300),knight_skills_5, 0x0000000c1610218368e29744e9a5985b00000000001db2a10000000000000000, nord_face_old_2],
  ["knight_8_3", "Jarl Jonasr", "Jonasr", tf_hero, 0, reserved,  fac_kingdom_8, [ itm_rich_outfit,  itm_studded_leather_coat,   itm_nomad_boots,  itm_norman_shoes,    itm_gjermundbu_helmet,	itm_lamellar_gauntlets,   itm_one_handed_battle_axe_c, itm_tab_shield_round_d],  															knight_attrib_4,wp(260),knight_skills_4, 0x0000000c03040289245a314b744b30a400000000001eb2a90000000000000000, nord_face_older_2],
  ["knight_8_4", "Jarl Apsod", "Apsod", tf_hero, 0, reserved,  fac_kingdom_8, [		itm_leather_vest,   itm_coat_of_plates,   itm_woolen_hose,  itm_norman_shoes,  itm_nordic_warlord_helmet, 	itm_lamellar_gauntlets, itm_celtic_axe, itm_tab_shield_round_e],  																			knight_attrib_4,wp(260),knight_skills_4, 0x0000000c3f1001ca3d6955b26a8939a300000000001e39b60000000000000000, nord_face_older_2],
  ["knight_8_5", "Jarl Eijnar", "Eijnar", tf_hero, 0, reserved,  fac_kingdom_8, [	  itm_fur_coat,   itm_coat_of_plates_red,   itm_leather_boots,  itm_splinted_leather_greaves,   itm_nordic_huscarl_helmet, itm_mail_gauntlets,	itm_sword_viking_3, itm_tab_shield_round_e], 															knight_attrib_4,wp(260),knight_skills_4, 0x0000000ff508330546dc4a59422d450c00000000001e51340000000000000000, nord_face_older_2],
  ["knight_8_6", "Jarl Shaggaa", "Shaggaa", tf_hero, 0, reserved,  fac_kingdom_8, [  	 itm_nomad_robe,   itm_cuir_bouilli,  itm_nomad_boots,  itm_splinted_leather_greaves,   itm_gjermundbu_helmet, itm_mail_gloves,   itm_great_axe, itm_tab_shield_round_d],   																		knight_attrib_4,wp(260),knight_skills_4, 0x00000005b00011813d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_middle_2],
  ["knight_8_7", "Jarl Thorkan", "Thorkan", tf_hero, 0, reserved,  fac_kingdom_8, [  itm_fur_coat,   itm_coat_of_plates_green,   itm_nomad_boots,  itm_mail_chausses,  itm_nordic_warlord_helmet, itm_lamellar_gauntlets,   itm_long_axe_c,  itm_tab_shield_round_d],   																	knight_attrib_5,wp(300),knight_skills_5, 0x00000006690002873d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_old_2],
  ["knight_8_8", "Jarl Withold", "Withold", tf_hero, 0, reserved,  fac_kingdom_8, [itm_saddle_horse,	itm_rich_outfit,  itm_black_studded_leather_mail,   itm_woolen_hose,  itm_norman_shoes,   itm_nordic_warlord_helmet, itm_heavy_plate_gloves, itm_nordic_nobleman_sword,  itm_tab_shield_round_d],  					 				knight_attrib_4,wp(260),knight_skills_4, 0x0000000f830051c53b026e4994ae272a00000000001db4e10000000000000000, nord_face_older_2],
  ["knight_8_9", "Jarl Zeltino", "Zeltino", tf_hero, 0, reserved,  fac_kingdom_8, [		itm_nomad_robe,   itm_heraldic_mail_with_tabard, itm_blue_hose,  itm_norman_shoes,  itm_nordic_warlord_helmet, itm_lamellar_gauntlets,   itm_one_handed_battle_axe_b,  itm_tab_shield_round_d],  													knight_attrib_5,wp(300),knight_skills_5, 0x00000000080c54c1345bd21349b1b67300000000001c90c80000000000000000, nord_face_older_2],
  ["knight_8_10", "Jarl Thomas Cadarn", "Thomas Cadarn", tf_hero, 0, reserved,  fac_kingdom_8, [   itm_leather_jerkin,   itm_leather_jerkin,   itm_nomad_boots,  itm_leather_boots,   itm_nordic_footman_helmet, itm_leather_gloves,itm_long_bow,itm_bodkin_arrows,itm_bodkin_arrows,itm_one_handed_battle_axe_a, itm_tab_shield_round_e],  	knight_attrib_1,wp(120),knight_skills_1|knows_power_draw_8|knows_shield_1, 0x000000084b0002063d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_older_2],
  ["knight_8_11", "Jarl jtobiasm", "jtobiasm", tf_hero, 0, reserved,  fac_kingdom_8, [ itm_rich_outfit,  itm_byrnie,   itm_woolen_hose,  itm_leather_boots,  itm_nordic_fighter_helmet,  itm_mail_gloves,  itm_long_bow,	itm_bodkin_arrows,	itm_bodkin_arrows,	itm_sword_viking_3_small, itm_tab_shield_round_e], 						knight_attrib_2,wp(180),knight_skills_2|knows_power_draw_8, 0x000000002d100005471d4ae69ccacb1d00000000001dca550000000000000000, nord_face_middle_2],
  ["knight_8_12", "Jarl Aethelwolf", "Aethelwolf", tf_hero, 0, reserved,  fac_kingdom_8, [ 	itm_short_tunic,  itm_byrnja, itm_blue_hose,  itm_splinted_leather_greaves,  itm_nordic_helmet,  itm_mail_gauntlets,  itm_war_spear,  itm_tab_shield_round_d],  																				knight_attrib_3,wp(220),knight_skills_3, 0x0000000b9500020824936cc51cb5bb2500000000001dd4d80000000000000000, nord_face_old_2],
  ["knight_8_13", "Jarl Reymann", "Reymann", tf_hero, 0, reserved,  fac_kingdom_8, [itm_saddle_horse,	itm_rich_outfit,  itm_heraldic_mail_with_tabard,   itm_nomad_boots,  itm_splinted_leather_greaves,   itm_nordic_huscarl_helmet, itm_lamellar_gauntlets,   itm_lance,	itm_sword_viking_a_long, itm_tab_shield_round_c],  			knight_attrib_3,wp(220),knight_skills_3, 0x0000000a300012c439233512e287391d00000000001db7200000000000000000, nord_face_older_2],
  ["knight_8_14", "Jarl Rod", "Rod", tf_hero, 0, reserved,  fac_kingdom_8, [  itm_leather_vest,   itm_mail_hauberk,   itm_woolen_hose,  itm_mail_chausses,  itm_nordic_helmet, itm_mail_mittens, itm_long_axe, itm_tab_shield_round_e],  																									knight_attrib_3,wp(220),knight_skills_3, 0x00000001bb0000013ae39737148e14b4000000000009c9490000000000000000, nord_face_older_2],
  ["knight_8_15", "Jarl Lehir", "Lehir", tf_hero, 0, reserved,  fac_kingdom_8, [   itm_leather_jacket,   itm_mail_shirt,   itm_leather_boots,  itm_mail_chausses,  itm_nordic_fighter_helmet,	itm_mail_gloves, itm_one_handed_battle_axe_a, itm_tab_shield_round_c], 																		knight_attrib_3,wp(220),knight_skills_3, 0x0000000d920801831715d1aa9221372300000000001ec6630000000000000000, nord_face_older_2],
  ["knight_8_16", "Jarl Mephala", "Mephala", tf_hero, 0, reserved,  fac_kingdom_8, [  	 itm_nomad_robe,   itm_dark_hauberk,  itm_nomad_boots,  itm_norman_shoes,   itm_nordic_huscarl_helmet, itm_mail_gauntlets,   itm_thegn_sword, itm_tab_shield_round_d],   																			knight_attrib_3,wp(220),knight_skills_3, 0x000000099700124239233512e287391d00000000001db7200000000000000000, nord_face_middle_2],
  ["knight_8_17", "Jarl Jurik", "Jurik", tf_hero, 0, reserved,  fac_kingdom_8, [  	itm_fur_coat,   itm_byrnja_d,   itm_nomad_boots,  itm_norman_shoes,  itm_gjermundbu_helmet, itm_mail_gauntlets,   itm_long_axe_b,itm_throwing_axes,itm_throwing_axes,  itm_tab_shield_round_d],   														knight_attrib_2,wp(180),knight_skills_2|knows_power_throw_6, 0x0000000c2f0442036d232a2324b5b81400000000001e55630000000000000000, nord_face_old_2],
  ["knight_8_18", "Jarl Brucia", "Brucia", tf_hero, 0, reserved,  fac_kingdom_8, [ itm_rich_outfit,  itm_arabian_armor_b,   itm_woolen_hose,  itm_leather_boots,   itm_byzantion_helmet_h, itm_mail_gauntlets, itm_danish_greatsword,  itm_tab_shield_round_d],   																			knight_attrib_5,wp(300),knight_skills_5, 0x0000000c0d00118866e22e3d9735a72600000000001eacad0000000000000000, nord_face_older_2],
  ["knight_8_19", "Jarl Yorvik", "Yorvik", tf_hero, 0, reserved,  fac_kingdom_8, [ itm_nomad_robe,   itm_byrnie, itm_blue_hose,  itm_leather_boots,  itm_nordic_fighter_helmet, itm_mail_gloves,   itm_sword_viking_3,  itm_tab_shield_round_c],  																							knight_attrib_1,wp(120),knight_skills_1, 0x0000000c0308225124e26d4a6295965a00000000001d23e40000000000000000, nord_face_older_2],
  ["knight_8_20", "Jarl Raedwald", "Raedwald", tf_hero, 0, reserved,  fac_kingdom_8, [   itm_courtly_outfit,   itm_byrnja_b,   itm_nomad_boots,  itm_norman_shoes, itm_nordic_huscarl_helmet, itm_scale_gloves_a, 	itm_sword_viking_3_small, itm_tab_shield_round_c],  																	knight_attrib_1,wp(120),knight_skills_1, 0x0000000f630052813b6bb36de5d6eb7400000000001dd72c0000000000000000, nord_face_older_2],

  ["knight_9_1", "Count Butan", "Butan", tf_hero, 0, reserved,  fac_kingdom_9, [   itm_tabard,   itm_transitional_blue,       itm_leather_boots,    itm_iron_greaves,    itm_visored_sallet_coif, itm_hourglass_gauntlets_b,     itm_warhammer,   itm_tab_shield_heater_d],     																				knight_attrib_5,wp(300),knight_skills_5, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_9_2", "Count Squall", "Squall", tf_hero, 0, reserved,  fac_kingdom_9, [    itm_red_gambeson,       itm_churburg_a,    itm_leather_boots,    itm_shynbaulds,    itm_visored_sallet, itm_hourglass_gauntlets_b,      itm_french_greatsword,   itm_tab_shield_heater_cav_b],     																		knight_attrib_5,wp(300),knight_skills_5, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_9_3", "Count Antoine", "Antoine", tf_hero, 0, reserved,  fac_kingdom_9, [itm_warhorse,    itm_short_tunic,  itm_french_plate,     itm_nomad_boots,      itm_iron_greaves,  itm_pepperpot_helmet_e, itm_hourglass_gauntlets_a, itm_heavy_lance, itm_espada_eslavona_b,  itm_tab_shield_heater_cav_b],    												knight_attrib_5,wp(300),knight_skills_5, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_9_4", "Count Bigboule", "Bigboule", tf_hero, 0, reserved,  fac_kingdom_9, [itm_hunter,     itm_leather_jacket,     itm_french_plate,       itm_woolen_hose,      itm_shynbaulds,    itm_french_pepperpot_helmet, itm_hourglass_gauntlets_a, itm_great_lance,itm_bastard_sword_b,    itm_tab_shield_heater_cav_b],    								knight_attrib_5,wp(300),knight_skills_5, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_9_5", "Count Balian", "Balian", tf_hero, 0, reserved,  fac_kingdom_9, [itm_saddle_horse,  itm_rich_outfit,  itm_surcoa_over_mail_and_plate_blue,     itm_leather_boots,    itm_hose_kneecops_red,    itm_open_sallet_coif, itm_hourglass_gauntlets_b, itm_lance,itm_french_longsword,  itm_tab_shield_heater_cav_b], 								knight_attrib_5,wp(300),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_9_6", "Count Bourprifette", "Bourprifette", tf_hero, 0, reserved,  fac_kingdom_9, [    itm_ragged_outfit,      itm_churburg_a,       itm_woolen_hose,      itm_splinted_greaves_spurs,	itm_visored_sallet,  itm_hourglass_gauntlets_a,       itm_bec_de_corbin_a,   itm_tab_shield_heater_d],    													knight_attrib_4,wp(260),knight_skills_4, 0x000000001100000648d24d36cd964b1d00000000001e2dac0000000000000000, rhodok_face_middle_2],
  ["knight_9_7", "Count Cuyeres", "Cuyeres", tf_hero, 0, reserved,  fac_kingdom_9, [     itm_coarse_tunic,       itm_transitional_heraldic,   itm_leather_boots,    itm_iron_greaves,  itm_visored_sallet,  itm_hourglass_gauntlets_b,           itm_spetum_b,    itm_tab_shield_heater_d],     																knight_attrib_4,wp(260),knight_skills_4, 0x0000000c3a0455c443d46e4c8b91291a00000000001ca51b0000000000000000, rhodok_face_old_2],
  ["knight_9_8", "Count Dagobert", "Dagobert", tf_hero, 0, reserved,  fac_kingdom_9, [itm_hunter, itm_courtly_outfit,     itm_brigandine_blue_a,    itm_woolen_hose,      itm_hose_kneecops_red,    itm_chapel_de_fer_g,  itm_gilded_hourglass_gloves,      itm_espada_eslavona_b,  itm_tab_shield_heater_cav_b],    											knight_attrib_4,wp(260),knight_skills_4, 0x0000000c2c0844d42914d19b2369b4ea00000000001e331b0000000000000000, rhodok_face_older_2],
  ["knight_9_9", "Count Dupond", "Dupond", tf_hero, 0, reserved,  fac_kingdom_9, [itm_warhorse,     itm_leather_jacket,     itm_mail_and_plate,   itm_leather_boots,    itm_hose_kneecops_green,       itm_open_sallet, itm_hourglass_gloves,   itm_lance, itm_espada_eslavona_a,   itm_tab_shield_heater_cav_b],   											knight_attrib_4,wp(260),knight_skills_4, 0x00000000420430c32331b5551c4724a100000000001e39a40000000000000000, rhodok_face_older_2],
  ["knight_9_10", "Count Dylan", "Dylan", tf_hero, 0, reserved,  fac_kingdom_9, [     itm_rich_outfit,  itm_french_plate,     itm_blue_hose,  itm_shynbaulds,       itm_french_pepperpot_helmet_b, itm_hourglass_gauntlets_b,       itm_long_voulge,   itm_tab_shield_heater_d],  																				knight_attrib_4,wp(260),knight_skills_4, 0x00000008e20011063d9b6d4a92ada53500000000001cc1180000000000000000, rhodok_face_older_2],
  ["knight_9_11", "Count Forax", "Forax", tf_hero, 0, reserved,  fac_kingdom_9, [     itm_tabard,       itm_surcoa_over_mail_and_plate_blue,       itm_leather_boots,    itm_hose_kneecops_red,    itm_chapel_de_fer_g,  itm_hourglass_gloves,    itm_falchion_b,   itm_tab_shield_heater_d],     																knight_attrib_3,wp(220),knight_skills_3, 0x0000000c170c14874752adb6eb3228d500000000001c955c0000000000000000, rhodok_face_middle_2],
  ["knight_9_12", "Count Guilhem", "Guilhem", tf_hero, 0, reserved,  fac_kingdom_9, [    itm_red_gambeson,       itm_brigandine_blue_a,    itm_leather_boots,    itm_hose_kneecops_red,    itm_full_helm,  itm_hourglass_gauntlets_a,      itm_military_hammer,   itm_tab_shield_heater_d],     																knight_attrib_3,wp(220),knight_skills_3, 0x0000000c080c13d056ec8da85e3126ed00000000001d4ce60000000000000000, rhodok_face_old_2],
  ["knight_9_13", "Count Jean", "Jean", tf_hero, 0, reserved,  fac_kingdom_9, [     itm_short_tunic,  itm_palace_guard,     itm_nomad_boots,      itm_splinted_leather_greaves,  itm_helmet_a, itm_mail_mittens,       itm_sniper_crossbow,itm_steel_bolts,itm_steel_bolts,	itm_espada_eslavona_a,  itm_tab_shield_heater_d],   								knight_attrib_1,wpe(80,60,180,60),knight_skills_1, 0x0000000cbf10100562a4954ae731588a00000000001d6b530000000000000000, rhodok_face_older_2],
  ["knight_9_14", "Count Borgne", "Borgne", tf_hero, 0, reserved,  fac_kingdom_9, [     itm_leather_jacket,     itm_heraldic_mail_with_tunic_b,       itm_woolen_hose,      itm_splinted_leather_greaves,    itm_chapel_de_fer_a, itm_mail_mittens, itm_military_hammer,itm_sniper_crossbow,itm_steel_bolts,itm_steel_bolts,    itm_tab_shield_heater_d],    	knight_attrib_2,wpe(120,80,220,80),knight_skills_2, 0x0000000c330805823baa77556c4e331a00000000001cb9110000000000000000, rhodok_face_older_2],
  ["knight_9_15", "Count Leragan", "Leragan", tf_hero, 0, reserved,  fac_kingdom_9, [     itm_rich_outfit,  itm_palace_guard,     itm_splinted_leather_greaves,    itm_chapel_de_fer_a, itm_mail_gloves,       itm_military_pick, itm_sniper_crossbow,itm_steel_bolts,itm_steel_bolts,  itm_tab_shield_heater_d], 												knight_attrib_2,wpe(120,80,220,80),knight_skills_2, 0x0000000d51000106370c4d4732b536de00000000001db9280000000000000000, rhodok_face_older_2],
  ["knight_9_16", "Count Olgarth", "Olgarth", tf_hero, 0, reserved,  fac_kingdom_9, [itm_saddle_horse,    itm_ragged_outfit,      itm_surcoat_over_mail_blue,       itm_woolen_hose,      itm_hose_kneecops_green,    itm_open_sallet, itm_hourglass_gauntlets_a,     itm_light_lance,itm_espada_eslavona_a,   itm_tab_shield_heater_cav_a],    				knight_attrib_3,wp(220),knight_skills_3, 0x0000000c06046151435b5122a37756a400000000001c46e50000000000000000, rhodok_face_middle_2],
  ["knight_9_17", "Count Pleutre", "Pleutre", tf_hero, 0, reserved,  fac_kingdom_9, [     itm_coarse_tunic,       itm_scale_armor,   itm_rus_shoes,    itm_rus_shoes,       itm_helmet_with_neckguard,  itm_mail_gloves,      itm_falchion_b,    itm_tab_shield_heater_d],     																					knight_attrib_3,wp(220),knight_skills_3, 0x0000000c081001d3465c89a6a452356300000000001cda550000000000000000, rhodok_face_old_2],
  ["knight_9_18", "Count Profy", "Profy", tf_hero, 0, reserved,  fac_kingdom_9, [ itm_courtly_outfit,     itm_palace_guard,    itm_woolen_hose,      itm_mail_chausses,    itm_pepperpot_helmet_f, itm_mail_gauntlets,       itm_battle_fork,   itm_tab_shield_heater_d],    																					knight_attrib_3,wp(220),knight_skills_3, 0x0000000a3d0c13c3452aa967276dc95c00000000001dad350000000000000000, rhodok_face_older_2],
  ["knight_9_19", "Count Wolfryme", "Wolfryme", tf_hero, 0, reserved,  fac_kingdom_9, [     itm_leather_jacket,     itm_heraldic_mail_with_tunic,   itm_leather_boots,    itm_leather_boots,       itm_kettle_hat, itm_mail_gloves,  itm_falchion_c,itm_crossbow,itm_steel_bolts,itm_bolts, itm_tab_shield_heater_d],   										knight_attrib_1,wpe(80,60,180,60),knight_skills_1, 0x0000000038043194092ab4b2d9adb44c00000000001e072c0000000000000000, rhodok_face_older_2],
  ["knight_9_20", "Count Etolas", "Etolas", tf_hero, 0, reserved,  fac_kingdom_9, [     itm_rich_outfit,  itm_haubergeon,     itm_blue_hose,  itm_mail_chausses,       itm_helmet_a, itm_mail_mittens,       itm_falchion,itm_steel_bolts,itm_bolts,   itm_tab_shield_heater_d],  																				knight_attrib_1,wp(120),knight_skills_1, 0x000000003600420515a865b45c64d64c00000000001d544b0000000000000000, rhodok_face_older_2],

  ["kingdom_1_pretender",  "Lady Isolla of Suno",       "Isolla",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_1,[itm_charger,   itm_rich_outfit,  itm_blue_hose,      itm_iron_greaves,         itm_mail_shirt,      itm_sword_medieval_c_small,      itm_tab_shield_small_round_c,       itm_bascinet],          lord_attrib,wp(220),knight_skills_5, 0x00000000ef00000237dc71b90c31631200000000001e371b0000000000000000],


  ["kingdom_2_pretender",  "Prince Valdym the Bastard", "Valdym",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_2,[itm_hunter,    itm_courtly_outfit,      itm_leather_boots,              itm_mail_chausses,              itm_lamellar_armor,       itm_military_pick,      itm_tab_shield_heater_b,      itm_flat_topped_helmet],    lord_attrib,wp(220),knight_skills_5, 0x00000000200412142452ed631b30365c00000000001c94e80000000000000000, vaegir_face_middle_2],


  ["kingdom_3_pretender",  "Dustum Khan",               "Dustum",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_3,[itm_courser,   itm_nomad_robe,             itm_leather_boots,              itm_splinted_greaves,           itm_khergit_guard_armor,         itm_sword_khergit_2,              itm_tab_shield_small_round_c,       itm_segmented_helmet],      lord_attrib,wp(220),knight_skills_5, 0x000000065504310b30d556b51238f66100000000001c256d0000000000000000, khergit_face_middle_2],


  ["kingdom_4_pretender",  "Lethwin Far-Seeker",   "Lethwin",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_4,[itm_hunter,    itm_tabard,    itm_leather_boots,              itm_mail_boots,                 itm_brigandine_red,           itm_sword_medieval_c,           itm_tab_shield_heater_cav_a,    itm_kettle_hat],            lord_attrib,wp(220),knight_skills_5, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, nord_face_young_2],


  ["kingdom_5_pretender",  "Lord Kastor of Veluca",  "Kastor",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_5,[itm_warhorse,  itm_nobleman_outfit,             itm_leather_boots,              itm_splinted_leather_greaves,   itm_mail_hauberk,           itm_sword_medieval_c,         itm_tab_shield_heater_d,        itm_spiked_helmet],         lord_attrib,wp(220),knight_skills_5, 0x0000000bed1031051da9abc49ecce25e00000000001e98680000000000000000, rhodok_face_old_2],


  ["kingdom_6_pretender",  "Arwa the Pearled One",       "Arwa",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_6,[itm_arabian_horse_b, itm_sarranid_mail_shirt, itm_sarranid_boots_c, itm_sarranid_cavalry_sword,      itm_tab_shield_small_round_c],          lord_attrib,wp(220),knight_skills_5, 0x000000050b003004072d51c293a9a70b00000000001dd6a90000000000000000],

  ["kingdom_7_pretender",  "Count Otton",       "Count Otton",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_7,[itm_arabian_horse_b, itm_sarranid_mail_shirt, itm_sarranid_boots_c, itm_sarranid_cavalry_sword,      itm_tab_shield_small_round_c],          lord_attrib,wp(220),knight_skills_5, 0x000000050b003004072d51c293a9a70b00000000001dd6a90000000000000000],

  ["kingdom_8_pretender",  "Jarl Leif",   "Jarl Leif",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_8,[itm_hunter,    itm_leather_boots,              itm_mail_chausses, itm_tabard	,  itm_mail_hauberk,           itm_thegn_sword, 	itm_tab_shield_round_d,    itm_nordic_huscarl_helmet],            lord_attrib|str_28,wp(220),knight_skills_5, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, nord_face_young_2],

  ["kingdom_9_pretender",  "Prince Philip",   "Prince Philip",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_9,[itm_plated_charger, itm_hourglass_gauntlets_b,              itm_shynbaulds,                 itm_french_plate,    itm_chapel_de_fer_a,   itm_lance,    itm_french_longsword,           itm_tab_shield_heater_cav_b,    itm_tabard,    itm_leather_boots],            lord_attrib|str_28,wp(220),knight_skills_5, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, swadian_face_young_2],



#Royal family members

  ["knight_1_1_wife","Error - knight_1_1_wife should not appear in game","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],

  #Swadian ladies - eight mothers, eight daughters, four sisters
  ["kingdom_1_lady_1","Lady Anna","Anna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [          itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_1_lady_2","Lady Nelda","Nelda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["knight_1_lady_3","Lady Bela","Bela",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["knight_1_lady_4","Lady Elina","Elina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_l_lady_5","Lady Constanis","Constanis",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_6","Lady Vera","Vera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_1_lady_7","Lady Auberina","Auberina",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_8","Lady Tibal","Tibal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_1_lady_9","Lady Magar","Magar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_10","Lady Thedosa","Thedosa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_1_lady_11","Lady Melisar","Melisar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_12","Lady Irena","Irena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_l_lady_13","Lady Philenna","Philenna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_14","Lady Sonadel","Sonadel",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_1_lady_15","Lady Boadila","Boadila",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_16","Lady Elys","Elys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_1_lady_17","Lady Johana","Johana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_1_lady_18","Lady Bernatys","Bernatys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_1_lady_19","Lady Enricata","Enricata",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_1_lady_20","Lady Gaeta","Gaeta",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],
  
  #Vaegir ladies
  ["kingdom_2_lady_1","Lady Junitha","Junitha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_2","Lady Katia","Katia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_3","Lady Seomis","Seomis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_4","Lady Drina","Drina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_5","Lady Nesha","Nesha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_6","Lady Tabath","Tabath",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_7","Lady Pelaeka","Pelaeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_8","Lady Haris","Haris",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_9","Lady Vayen","Vayen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_10","Lady Joaka","Joaka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_11","Lady Tejina","Tejina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_12","Lady Olekseia","Olekseia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_13","Lady Myntha","Myntha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_14","Lady Akilina","Akilina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_15","Lady Sepana","Sepana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_16","Lady Iarina","Iarina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_17","Lady Sihavan","Sihavan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_18","Lady Erenchina","Erenchina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_19","Lady Tamar","Tamar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_20","Lady Valka","Valka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [itm_green_dress,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],


  ["kingdom_3_lady_1","Lady Borge","Borge",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_2","Lady Tuan","Tuan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_3","Lady Mahraz","Mahraz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_4","Lady Ayasu","Ayasu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_5","Lady Ravin","Ravin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_6","Lady Ruha","Ruha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_7","Lady Chedina","Chedina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_8","Lady Kefra","Kefra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_9","Lady Nirvaz","Nirvaz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
  ["kingdom_3_lady_10","Lady Dulua","Dulua",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_11","Lady Selik","Selik",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
  ["kingdom_3_lady_12","Lady Thalatha","Thalatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_13","Lady Yasreen","Yasreen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_14","Lady Nadha","Nadha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_15","Lady Zenur","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_16","Lady Arjis","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],
  ["kingdom_3_lady_17","Lady Atjahan", "Atjahan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000],
  ["kingdom_3_lady_18","Lady Qutala","Qutala",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_19","Lady Hindal","Hindal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_20","Lady Mechet","Mechet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  
  
  
  ["kingdom_4_lady_1","Lady Jadeth","Jadeth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_2","Lady Miar","Miar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_3","Lady Dria","Dria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress, itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_4","Lady Glunde","Glunde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_5","Lady Loeka","Loeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_6","Lady Bryn","Bryn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_7","Lady Eir","Eir",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter_1","Lady Thera","Thera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_9","Lady Hild","Hild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife_1","Lady Endegrid","Endegrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_11","Lady Herjasa","Herjasa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2c_daughter","Lady Svipul","Svipul",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["knight_4_1b_wife","Lady Ingunn","Ingunn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_14","Lady Kaeteli","Kaeteli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1b_daughter","Lady Eilif","Eilif",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter_2","Lady Gudrun","Gudrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_17","Lady Bergit","Bergit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife_2","Lady Aesa","Aesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1c_daughter","Lady Alfrun","Alfrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_20","Lady Afrid","Afrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],


  ["kingdom_5_lady_1","Lady Brina","Brina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_lady_2","Lady Aliena","Aliena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_lady_3","Lady Aneth","Aneth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_4","Lady Reada","Reada",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_5_wife","Lady Saraten","Saraten",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_5_2b_wife_1","Lady Baotheia","Baotheia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000bf0400035913aa236b4d975a00000000001eb69c0000000000000000],
  ["kingdom_5_1c_daughter_1","Lady Eleandra","Eleandra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_1","Lady Meraced","Meraced",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_1","Lady Adelisa","Adelisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_1","Lady Calantina","Calantina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_2","Lady Forbesa","Forbesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_2","Lady Claudora","Claudora",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1b_wife","Lady Anais","Anais",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2b_wife_2","Lady Miraeia","Miraeia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_3","Lady Agasia","Agasia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_16","Lady Geneiava","Geneiava",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_2","Lady Gwenael","Gwenael",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_2","Lady Ysueth","Ysueth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_4","Lady Ellian","Ellian",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_20","Lady Timethi","Timethi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  
#Sarranid ladies
  ["kingdom_6_lady_1","Lady Rayma","Rayma",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_6_lady_2","Lady Thanaikha","Thanaikha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_6_lady_3","Lady Sulaha","Sulaha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_6_lady_4","Lady Shatha","Shatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_6_lady_5","Lady Bawthan","Bawthan",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_6","Lady Mahayl","Mahayl",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_6_lady_7","Lady Isna","Isna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_8","Lady Siyafan","Siyafan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_6_lady_9","Lady Ifar","Ifar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_10","Lady Yasmin","Yasmin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_6_lady_11","Lady Dula","Dula",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_12","Lady Ruwa","Ruwa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_6_lady_13","Lady Luqa","Luqa",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_14","Lady Zandina","Zandina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_6_lady_15","Lady Lulya","Lulya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_16","Lady Zahara","Zahara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_6_lady_17","Lady Safiya","Safiya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_6_lady_18","Lady Khalisa","Khalisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_6_lady_19","Lady Janab","Janab",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_6_lady_20","Lady Sur","Sur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],


  ["kingdom_7_lady_1","Lady Borge","Borge",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_7_lady_2","Lady Tuan","Tuan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_7_lady_3","Lady Mahraz","Mahraz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_7_lady_4","Lady Ayasu","Ayasu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [    itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_7_lady_5","Lady Ravin","Ravin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_7_lady_6","Lady Ruha","Ruha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_7_lady_7","Lady Chedina","Chedina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [    itm_brown_dress,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_7_lady_8","Lady Kefra","Kefra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_7_lady_9","Lady Nirvaz","Nirvaz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
  ["kingdom_7_lady_10","Lady Dulua","Dulua",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_7_lady_11","Lady Selik","Selik",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
  ["kingdom_7_lady_12","Lady Thalatha","Thalatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_7_lady_13","Lady Yasreen","Yasreen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_7_lady_14","Lady Nadha","Nadha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_7_lady_15","Lady Zenur","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_7_lady_16","Lady Arjis","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],
  ["kingdom_7_lady_17","Lady Atjahan", "Atjahan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000],
  ["kingdom_7_lady_18","Lady Qutala","Qutala",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_7_lady_19","Lady Hindal","Hindal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_7_lady_20","Lady Mechet","Mechet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  
  ["kingdom_8_lady_1","Lady Jadeth","Jadeth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_8_lady_2","Lady Miar","Miar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_8_lady_3","Lady Dria","Dria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [    itm_peasant_dress, itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_8_lady_4","Lady Glunde","Glunde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_8_lady_5","Lady Loeka","Loeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_8_lady_6","Lady Bryn","Bryn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_8_lady_7","Lady Eir","Eir",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_8_lady_8","Lady Thera","Thera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_8_lady_9","Lady Hild","Hild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_court_dress ,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_8_lady_10","Lady Endegrid","Endegrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_8_lady_11","Lady Herjasa","Herjasa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_8_lady_12","Lady Svipul","Svipul",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_8_lady_13","Lady Ingunn","Ingunn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_8_lady_14","Lady Kaeteli","Kaeteli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_8_lady_15","Lady Eilif","Eilif",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_8_lady_16","Lady Gudrun","Gudrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_8_lady_17","Lady Bergit","Bergit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_court_dress ,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_8_lady_18","Lady Aesa","Aesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_8_lady_19","Lady Alfrun","Alfrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_8_lady_20","Lady Afrid","Afrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],

  ["kingdom_9_lady_1","Lady Jadeth","Jadeth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_9_lady_2","Lady Miar","Miar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_9_lady_3","Lady Dria","Dria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [    itm_peasant_dress, itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_9_lady_4","Lady Glunde","Glunde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_9_lady_5","Lady Loeka","Loeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_9_lady_6","Lady Bryn","Bryn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_9_lady_7","Lady Eir","Eir",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_9_lady_8","Lady Thera","Thera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_9_lady_9","Lady Hild","Hild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [      itm_court_dress ,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_9_lady_10","Lady Endegrid","Endegrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_9_lady_11","Lady Herjasa","Herjasa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_9_lady_12","Lady Svipul","Svipul",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_9_lady_13","Lady Ingunn","Ingunn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_9_lady_14","Lady Kaeteli","Kaeteli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_9_lady_15","Lady Eilif","Eilif",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_9_lady_16","Lady Gudrun","Gudrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_9_lady_17","Lady Bergit","Bergit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [      itm_court_dress ,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_9_lady_18","Lady Aesa","Aesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_9_lady_19","Lady Alfrun","Alfrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_9_lady_20","Lady Afrid","Afrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],

  ["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],
#Merchants                                                                              AT                      SILAH                   ZIRH                        BOT                         Head_wear
##  ["merchant_1", "merchant_1_F", "merchant_1_F",tf_hero|tf_female,  0,0, fac_kingdom_1,[itm_courser,            itm_fighting_axe,       itm_leather_jerkin,         itm_leather_boots,          itm_straw_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008200201e54c137a940c91],
##  ["merchant_2", "merchant_2", "merchant_2", tf_hero,               0,0, fac_kingdom_2,[itm_saddle_horse,       itm_arming_sword,       itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000000601db6db6db6db6db],
##  ["merchant_3", "merchant_3", "merchant_3", tf_hero,               0,0, fac_kingdom_3,[itm_courser,            itm_nordic_sword,       itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008100701db6db6db6db6db],
##  ["merchant_4", "merchant_4_F", "merchant_4_F",tf_hero|tf_female,  0,0, fac_kingdom_4,[itm_saddle_horse,       itm_falchion,           itm_light_leather,          itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401e54c137a945c91],
##  ["merchant_5", "merchant_5", "merchant_5", tf_hero,               0,0, fac_kingdom_5,[itm_saddle_horse,       itm_sword,              itm_ragged_outfit,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008038001e54c135a945c91],
##  ["merchant_6", "merchant_6", "merchant_6", tf_hero,               0,0, fac_kingdom_1,[itm_saddle_horse,      itm_scimitar,           itm_leather_jerkin,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000248e01e54c1b5a945c91],
##  ["merchant_7", "merchant_7_F", "merchant_7_F",tf_hero|tf_female,  0,0, fac_kingdom_2,[itm_hunter,            itm_arming_sword,       itm_padded_leather,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004200601c98ad39c97557a],
##  ["merchant_8", "merchant_8", "merchant_8", tf_hero,               0,0, fac_kingdom_3,[itm_saddle_horse,      itm_nordic_sword,       itm_light_leather,          itm_leather_boots,          itm_woolen_hood],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001095ce01d6aad3a497557a],
##  ["merchant_9", "merchant_9", "merchant_9", tf_hero,               0,0, fac_kingdom_4,[itm_saddle_horse,      itm_sword,              itm_padded_leather,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010519601ec26ae99898697],
##  ["merchant_10","merchant_10","merchant_10",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000884c401f6837d3294e28a],
##  ["merchant_11","merchant_11","merchant_11",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c450501e289dd2c692694],
##  ["merchant_12","merchant_12","merchant_12",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_falchion,           itm_leather_jerkin,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c660a01e5af3cb2763401],
##  ["merchant_13","merchant_13","merchant_13",tf_hero,               0,0, fac_merchants,[itm_sumpter_horse,      itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001001d601ec912a89e4d534],
##  ["merchant_14","merchant_14","merchant_14",tf_hero,               0,0, fac_merchants,[itm_courser,            itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004335601ea2c04a8b6a394],
##  ["merchant_15","merchant_15","merchant_15",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_padded_leather,         itm_woolen_hose,            itm_fur_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008358e01dbf27b6436089d],
##  ["merchant_16","merchant_16_F","merchant_16_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c300101db0b9921494add],
##  ["merchant_17","merchant_17","merchant_17",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008740f01e945c360976a0a],
##  ["merchant_18","merchant_18","merchant_18",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008020c01fc2db3b4c97685],
##  ["merchant_19","merchant_19","merchant_19",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_falchion,           itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008118301f02af91892725b],
##  ["merchant_20","merchant_20_F","merchant_20_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_courser,            itm_arming_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401f6837d27688212],

  
#Seneschals
  ["town_1_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_2_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_3_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_4_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_17_seneschal", "{!}Town17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],

  ["castle_1_seneschal", "{!}Castle 1 Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_seneschal", "{!}Castle 10 Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_41_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_42_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_43_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_44_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_45_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_46_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_47_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_48_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],

#Arena Masters
  ["town_1_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_1_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_2_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_2_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_3_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_3_arena|entry(52),reserved,   fac_commoners,[itm_nomad_armor,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_4_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_4_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_5_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_5_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_6_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_6_arena|entry(52),reserved,   fac_commoners,[itm_leather_jerkin,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_7_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_7_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_8_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_8_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_9_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_9_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_10_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_10_arena|entry(52),reserved,  fac_commoners,[itm_nomad_armor,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_11_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_11_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_12_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_12_arena|entry(52),reserved,  fac_commoners,[itm_leather_jerkin,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_13_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_13_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_14_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_14_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_15_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_15_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_16_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_16_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_17_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_17_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_18_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_18_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_19_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_19_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_20_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_20_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_21_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_21_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_22_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_22_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],



# Underground 

##  ["town_1_crook","Town 1 Crook","Town 1 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_leather_boots       ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004428401f46e44a27144e3],
##  ["town_2_crook","Town 2 Crook","Town 2 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_lady_dress_ruby,    itm_turret_hat_ruby     ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004300101c36db6db6db6db],
##  ["town_3_crook","Town 3 Crook","Town 3 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_apron,      itm_hide_boots          ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c530701f17944a25164e1],
##  ["town_4_crook","Town 4 Crook","Town 4 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c840501f36db6db7134db],
##  ["town_5_crook","Town 5 Crook","Town 5 Crook",tf_hero,                0,0, fac_neutral,[itm_red_gambeson,       itm_blue_hose           ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c000601f36db6db7134db],
##  ["town_6_crook","Town 6 Crook","Town 6 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c10c801db6db6dd7598aa],
##  ["town_7_crook","Town 7 Crook","Town 7 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_woolen_dress,       itm_woolen_hood         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010214101de2f64db6db58d],
##  
##  ["town_8_crook","Town 8 Crook","Town 8 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_jacket,     itm_leather_boots       ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010318401c96db4db6db58d],
##  ["town_9_crook","Town 9 Crook","Town 9 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008520501f16db4db6db58d],
##  ["town_10_crook","Town 10 Crook","Town 10 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008600701f35144db6db8a2],
##  ["town_11_crook","Town 11 Crook","Town 11 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_blue_dress,        itm_wimple_with_veil    ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008408101f386c4db4dd514],
##  ["town_12_crook","Town 12 Crook","Town 12 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000870c501f386c4f34dbaa1],
##  ["town_13_crook","Town 13 Crook","Town 13 Crook",tf_hero,             0,0, fac_neutral,[itm_blue_gambeson,     itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c114901f245caf34dbaa1],
##  ["town_14_crook","Town 14 Crook","Town 14 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_woolen_dress,      itm_turret_hat_ruby     ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000001021c001f545a49b6eb2bc],

# Armor Merchants
  #arena_masters_end = zendar_armorer

  ["town_1_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_2_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,          itm_straw_hat       ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_3_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,        itm_hide_boots      ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_blue_hose       ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_leather,       itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_9_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_sarranid_common_dress,         itm_sarranid_head_cloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],

# Weapon merchants

  ["town_1_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,     itm_nomad_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_3_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,   itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,     itm_wrapping_boots,itm_straw_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_9_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_leather_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_blue,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_15_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_19_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],

#Tavern keepers

  ["town_1_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_1_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_2_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_2_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_3_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_3_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_4_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_4_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_5_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_5_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_6_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_6_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_7_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_7_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_leather_boots,      itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_8_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_8_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,      itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_9_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_9_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_10_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_10_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_11_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_11_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_12_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_12_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_13_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_13_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_14_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_14_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_15_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_15_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_16_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_16_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_17_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_17_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_18_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_18_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_19_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_19_tavern|entry(9),0,  fac_commoners,[itm_sarranid_dress_a,        itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_20_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_20_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe,       itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_21_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_21_tavern|entry(9),0,  fac_commoners,[itm_sarranid_common_dress,        itm_sarranid_boots_a,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_22_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_22_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe_b,               itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],

#Goods Merchants

  ["town_1_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_1_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_2_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_3_store|entry(9),0, fac_commoners,     [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_4_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_4_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_5_store|entry(9),0, fac_commoners,     [itm_nomad_armor,   itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_6_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_6_store|entry(9),0, fac_commoners,     [itm_woolen_dress,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_7_store|entry(9),0, fac_commoners,     [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_8_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,    [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_11_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_11_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_12_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_13_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_13_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_14_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_14_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_15_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_15_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_16_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_17_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_17_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_18_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_18_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_19_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_19_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_20_store|entry(9),0, fac_commoners,    [itm_sarranid_common_dress_b,  itm_sarranid_boots_a, itm_sarranid_felt_head_cloth_b  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_21_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_21_store|entry(9),0, fac_commoners,    [itm_sarranid_dress_a,         itm_sarranid_boots_a,  itm_sarranid_felt_head_cloth  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_22_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_22_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],

  ["salt_mine_merchant","Barezan","Barezan",                tf_hero|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [itm_leather_apron, itm_leather_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c528601ea69b6e46dbdb6],

# Horse Merchants

  ["town_1_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_horse_merchant","Horse Merchant","{!}Town 3 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_nomad_armor,          itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_4_horse_merchant","Horse Merchant","{!}Town 4 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_horse_merchant","Horse Merchant","{!}Town 5 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_dress,                itm_woolen_hose,    itm_woolen_hood],   def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_6_horse_merchant","Horse Merchant","{!}Town 6 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_horse_merchant","Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_horse_merchant","Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_horse_merchant","Horse Merchant","{!}Town 9 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_woolen_hose],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_horse_merchant","Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_blue_dress,          itm_blue_hose,      itm_straw_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_11_horse_merchant","Horse Merchant","{!}Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_13_horse_merchant","Horse Merchant","{!}Town 13 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_14_horse_merchant","Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_17_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_18_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_sarranid_boots_a],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe,      itm_sarranid_boots_a],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_21_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe_b,        itm_sarranid_boots_a],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_22_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_sarranid_common_dress_b,       itm_blue_hose,      itm_sarranid_felt_head_cloth_b],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],


#Town Mayors    #itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit
  ["town_1_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_2_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_gambeson,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_3_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_blue_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_4_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_fur_coat,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_5_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_nobleman_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_6_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_7_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_rich_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_8_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_9_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_10_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_11_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_12_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_red_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_13_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_14_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_15_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_16_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_fur_coat,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_17_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_18_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_19_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,     itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_20_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,       itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_21_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,    itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_22_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_sarranid_boots_a],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],


#Village stores
  ["village_1_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_2_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_3_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_4_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_5_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_6_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_7_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_8_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_9_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,         man_face_old_1, man_face_older_2],
  ["village_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_24_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_25_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_26_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_27_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_28_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_29_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_30_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_31_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_32_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_33_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_34_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_35_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_36_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_37_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_38_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_39_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_40_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_41_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_42_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_43_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_44_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_45_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_46_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_47_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_48_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_49_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_50_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_51_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_52_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_53_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_54_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_55_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_56_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_57_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_58_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_59_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_60_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_61_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_62_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_63_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_64_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_65_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_66_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_67_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_68_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_69_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_70_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_71_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_72_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_73_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_74_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_75_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_76_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_77_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_78_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_79_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_80_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_81_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_82_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_83_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_84_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_85_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_86_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_87_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_88_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_89_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_90_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_91_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_92_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_93_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_94_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_95_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_96_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_97_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_98_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_99_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_100_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_101_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_102_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_103_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_104_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_105_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_106_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_107_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_108_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_109_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_110_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
# Place extra merchants before this point
  ["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  #Used for player enterprises
  ["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
  ["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
  ["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  ["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
  ["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_12_master_craftsman", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_13_master_craftsman", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
  ["town_14_master_craftsman", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
  ["town_15_master_craftsman", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_16_master_craftsman", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
  ["town_17_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
  ["town_18_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_19_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
  ["town_20_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
  ["town_21_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
  ["town_22_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
  
  
  
# Chests
  ["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,
   [],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_crossbow, itm_tutorial_bolts, itm_tutorial_throwing_daggers],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

  ["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],  
  
# These are used as arrays in the scripts.
  ["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_d","{!}temp_array_d","{!}temp_array_d",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

  ["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

##Mod Begin
    ["added_items_to_recruit","{!} added items_array_to_recruit","{!} added items_array_to_recruit",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  
    ["added_items_temp","{!} added_items_temp_array","{!} added_items_temp_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
    
	["player_items_backup","{!} player_items_backup","{!} player_items_backup",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
	["temp_items_troop","{!} temp_items_troop","{!} temp_items_troop",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common|knows_inventory_management_10,0],

	
###mod end
  
  
  ["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

##  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard",tf_mounted|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
##   [itm_arrows,itm_nomad_sabre,itm_scimitar,itm_winged_mace,itm_lance,itm_khergit_bow,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_nomad_shield,itm_steppe_horse,itm_warhorse],
##   def_attrib|level(28),wp(140),knows_riding_6|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6,khergit_face1, khergit_face2],


# Add Extra Quest NPCs below this point  

  ["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["tax_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["trainee_peasant","Peasant","Peasants",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["fugitive","Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_medieval_b, itm_throwing_daggers],
   def_attrib|str_24|agi_25|level(26),wp(180),knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,man_face_middle_1, man_face_old_2],
   
  ["belligerent_drunk","Belligerent Drunk","Belligerent Drunks",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_8|level(15),wp(120),knows_common|knows_power_strike_2|knows_ironflesh_9,    bandit_face1, bandit_face2],

  ["hired_assassin","Hired Assassin","Hired Assassin",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, #they look like belligerent drunks
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

  ["fight_promoter","Rough-Looking Character","Rough-Looking Character",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

   
   
  ["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_viking_1,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(20),wp(130),knows_common,man_face_middle_1, man_face_older_2],
   
  ["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],

   ["nurse_for_lady","Nurse","Nurse",tf_female|tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_robe, itm_black_hood, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,woman_face_1, woman_face_2],   
   ["temporary_minister","Minister","Minister",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,
   [itm_rich_outfit, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],   
   
   
##  ["conspirator","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["conspirator_leader","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["peasant_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_peasant_rebels,
##   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
##   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
##  ["noble_refugee","Noble Refugee","Noble Refugees",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_noble_refugees,
##   [itm_sword,itm_leather_jacket,itm_hide_boots, itm_saddle_horse, itm_leather_jacket, itm_leather_cap],
##   def_attrib|level(9),wp(100),knows_common,swadian_face1, swadian_face2],
##  ["noble_refugee_woman","Noble Refugee Woman","Noble Refugee Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_noble_refugees,
##   [itm_knife,itm_dagger,itm_hunting_crossbow,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
##   def_attrib|level(3),wp(45),knows_common,refugee_face1,refugee_face2],


  ["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [itm_padded_cloth,itm_nomad_boots, itm_splinted_leather_greaves, itm_skullcap, itm_sword_medieval_b,  itm_crossbow, itm_bolts, itm_plate_covered_round_shield],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

#Multiplayer ai troops
  ["swadian_crossbowman_multiplayer_ai","Polan's Crossbowman","Polan's Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_light_crossbow,itm_sword_medieval_b,itm_sword_medieval_a,itm_mace_2,itm_one_handed_war_axe_a,
    itm_red_gambeson,itm_white_gambeson_a,itm_nasal_helmet,itm_mail_coif,itm_leather_boots,itm_ankle_boots,itm_serbian_ankle_boots,itm_leather_gloves,itm_mail_gloves],
   def_attrib_multiplayer|str_14|agi_15|level(19),wpe(90,60,180,90),knows_common|knows_ironflesh_2|knows_athletics_5|knows_shield_5|knows_power_strike_2|knows_riding_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer_ai","Polan's Infantry","Polan's Infantry",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_sword_medieval_c,itm_fighting_pick,itm_sword_medieval_c_small,itm_tab_shield_pavise_b,itm_tab_shield_pavise_c,itm_spear,itm_mail_mittens,itm_mail_gloves,itm_javelin,
    itm_kaftan_over_mail_c,itm_brigandine_white,itm_brigandine_red_c,itm_kaftan_over_mail_d,itm_surcoat_over_mail_heraldic,itm_lithuanian_helmet,itm_helmet_with_neckguard,itm_mail_coif,itm_hose_kneecops_red,itm_mail_chausses,itm_rus_cav_boots],
   def_attrib_multiplayer|str_21|agi_15|level(20),wpex(155,150,150,40,60,110),knows_common|knows_ironflesh_5|knows_shield_6|knows_power_strike_7|knows_power_throw_3|knows_athletics_6|knows_riding_1,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai","Polan's Man at Arms","Polan's Men at Arms",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_lance,itm_cav_sword,itm_sword_medieval_d_long,itm_lithuanian_shield,itm_military_hammer,
    itm_lithuanian_ducal_armor,itm_surcoa_over_mail_and_plate_heraldic,itm_mail_and_plate_boots_b,itm_splinted_greaves_spurs,itm_lithuanian_helmet,itm_novogrod_helmet,itm_hourglass_gloves,itm_hourglass_gauntlets_a,itm_hunter,itm_courser],
   def_attrib_multiplayer|str_21|agi_15|level(20),wpex(150,150,150,40,60,110),knows_common|knows_riding_5|knows_ironflesh_3|knows_shield_5|knows_power_throw_2|knows_horse_archery_1|knows_power_strike_6|knows_athletics_3,swadian_face_young_1, swadian_face_old_2],
 
  ["vaegir_archer_multiplayer_ai","Grey Archer","Grey Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_war_bow,itm_bodkin_arrows,itm_one_handed_war_axe_a,itm_mace_2,
    itm_skullcap,itm_nasal_helmet,itm_coarse_tunic,itm_nomad_armor,itm_wrapping_boots,itm_hide_boots],
   def_attrib_multiplayer|str_14|agi_15|level(19),wpe(80,180,60,80),knows_ironflesh_2|knows_power_draw_6|knows_athletics_4|knows_shield_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer_ai","Grey Infantry","Grey Infantry",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_sword_medieval_d_long,itm_scimitar_b,itm_pike_b,itm_one_handed_bar_mace,itm_morningstar,itm_celtic_axe,itm_longsword,itm_bec_de_corbin_a,itm_steel_pick,itm_tab_shield_kite_cav_b,itm_long_bardiche,itm_javelin,
    itm_kuyak_a,itm_kuyak_b,itm_norman_helmet_b,itm_norman_helmet_c,itm_norman_helmet_d,itm_pronoia_helmet,itm_rus_cav_boots,itm_mail_gloves,itm_gilded_hourglass_gloves],
   def_attrib_multiplayer|str_21|agi_15|level(19),wpex(150,150,150,30,50,120),knows_ironflesh_4|knows_shield_5|knows_power_throw_3|knows_power_strike_7|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer_ai","Grey Horseman","Grey Horsemen",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_lance,itm_scimitar_b,itm_sword_medieval_d_long,itm_tab_shield_kite_cav_b,
    itm_kuyak_a,itm_kuyak_b,itm_norman_helmet_b,itm_norman_helmet_c,itm_norman_helmet_d,itm_pronoia_helmet,itm_rus_cav_boots,itm_mail_gloves,itm_gilded_hourglass_gloves,itm_saddle_horse,itm_courser],
   def_attrib_multiplayer|str_21|agi_15|level(19),wpe(150,90,60,110),knows_riding_5|knows_horse_archery_1|knows_ironflesh_3|knows_power_strike_6|knows_shield_5|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2],
  
  ["khergit_dismounted_lancer_multiplayer_ai","Tengri Warrior","Tengri Warrior",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_arabian_sword_d,itm_scimitar_b,itm_sarranid_two_handed_axe_a,itm_sarranid_two_handed_mace_1,itm_sarranid_axe_b,itm_hafted_blade_a,itm_plate_covered_round_shield,itm_tab_shield_kite_d,itm_ashwood_pike,itm_jarid,
    itm_ghulam_helmet_a,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_saracen_mail_c,itm_saracen_mail_b,itm_saracen_mail_a,itm_sarranid_boots_d,itm_sarranid_boots_c,itm_lamellar_gauntlets,itm_scale_gloves_a],
   def_attrib_multiplayer|str_21|agi_15|level(19),wpex(150,150,150,30,50,120),knows_ironflesh_4|knows_shield_5|knows_power_throw_3|knows_power_strike_7|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer_ai","Tengri Archer","Tengri Archers",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_khergit_bow,itm_bodkin_arrows,itm_arrows,itm_strong_bow,itm_scimitar_b,itm_arabian_sword_b,itm_sarranid_mace_1,
    itm_janissary_boerk_b,itm_janissary_boerk_a,itm_janissary_boerk_c,itm_sarranid_leather_armor,itm_deli_robe,itm_khergit_leather_boots,itm_leather_gloves],
   def_attrib_multiplayer|str_12|agi_15|level(21),wpe(70,180,60,100),knows_riding_2|knows_power_draw_3|knows_horse_archery_2|knows_athletics_4,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer_ai","Tengri Lancer","Tengri Lancers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_heavy_lance,itm_arabian_sword_d,itm_scimitar_b,itm_sarranid_two_handed_axe_b,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_jarid,
    itm_saracen_helmet_b,itm_saracen_helmet_d,itm_mamluke_mail,itm_sipahi_jawshan,itm_sarranid_boots_c,itm_sarranid_boots_d,itm_scale_gauntlets,itm_scale_gloves_a,itm_warhorse_b,itm_courser],
   def_attrib_multiplayer|str_21|agi_15|level(21),wp(155),knows_riding_5|knows_horse_archery_2|knows_ironflesh_3|knows_power_throw_3|knows_shield_5|knows_power_strike_6|knows_athletics_5,khergit_face_middle_1, khergit_face_older_2],
 
  ["nord_veteran_multiplayer_ai","Kalmarunionen Footman","Kalmarunionen Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_4,
   [itm_long_axe_b,itm_military_cleaver_b,itm_two_handed_battle_axe_2,itm_sledgehammer,itm_ashwood_pike,itm_plate_covered_round_shield,itm_round_shield,
    itm_kettle_hat_f,itm_kettle_hat_e,itm_brigandine_red_c,itm_brigandine_yellow_a,itm_brigandine_blue_a,itm_chapel_de_fer_d,itm_brigandine_blue,itm_brigandine_yellow,itm_brigandine_red_b,itm_hose_kneecops_red,itm_hose_kneecops_green,itm_wisby_gloves_red,itm_wisby_gauntlets_red],
   def_attrib_multiplayer|str_21|agi_15|level(24),wpex(150,150,150,40,60,140),knows_ironflesh_4|knows_power_strike_7|knows_power_throw_4|knows_athletics_6|knows_shield_5|knows_riding_1,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer_ai","Kalmarunionen Horseman","Kalmarunionen Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_lance,itm_sword_viking_c_long,itm_sword_viking_a_long,itm_plate_covered_round_shield,itm_tab_shield_heater_cav_a,
    itm_great_helmet_i,itm_great_helmet_h,itm_great_helmet_d,itm_topfhelm_f,itm_surcoa_over_mail_and_plate_blue,itm_wisby_gloves,itm_surcoat_over_mail_blue,itm_splinted_greaves_spurs,itm_hourglass_gauntlets_a,itm_saddle_horse,itm_courser,],
   def_attrib_multiplayer|str_21|agi_15|level(19),wp(155),knows_riding_5|knows_ironflesh_2|knows_power_strike_5|knows_shield_5|knows_horse_archery_2|knows_power_throw_3|knows_athletics_3,vaegir_face_young_1, vaegir_face_older_2],
  ["nord_archer_multiplayer_ai","Kalmarunionen Archer","Kalmarunionen Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_khergit_arrows,itm_short_bow,itm_long_bow,itm_bodkin_arrows,itm_mace_4,itm_sword_viking_1,itm_sword_viking_2_small,
    itm_nordic_veteran_archer_helmet,itm_nordic_archer_helmet,itm_peltastos_armor,itm_leather_scale_armor,itm_hide_boots,itm_leather_gloves],
   def_attrib_multiplayer|str_12|agi_15|level(15),wpe(90,180,60,80),knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_power_draw_5|knows_athletics_4|knows_riding_1,nord_face_young_1, nord_face_old_2],
  
  ["rhodok_veteran_crossbowman_multiplayer_ai","Druzhina Archer","Druzhina Archers",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_nomad_bow,itm_war_bow,itm_scimitar,itm_mace_4,itm_one_handed_war_axe_a,itm_arrows,itm_bodkin_arrows,
    itm_rus_helmet_b,itm_vaegir_lamellar_helmet,itm_tribal_warrior_outfit,itm_rus_cav_boots,itm_mail_gloves,itm_mail_gauntlets],
   def_attrib_multiplayer|str_12|agi_15|level(20),wpe(100,180,60,90),knows_common|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_power_draw_6|knows_athletics_5|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman_multiplayer_ai","Druzhina Footman","Druzhina Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_5,
   [itm_scimitar_b,itm_military_hammer,itm_bardiche,itm_maul,itm_long_bardiche,itm_pike,itm_tab_shield_kite_c,itm_javelin,
    itm_nikolskoe_helmet,itm_tagancha_helmet_b,itm_drz_lamellar_armor,itm_gnezdovo_helmet,itm_drz_lamellar_armor_a,itm_drz_lamellar_armor_a,itm_rus_cav_boots,itm_hourglass_gloves,itm_gilded_hourglass_gloves],
   def_attrib_multiplayer|str_21|agi_15|level(20),wpex(150,150,150,30,50,110),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_7|knows_power_throw_1|knows_athletics_6|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai","Druzhina Horseman","Druzhina Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_lance,itm_scimitar,itm_bardiche,itm_tab_shield_kite_cav_a,
    itm_rus_helmet_b,itm_tagancha_helmet_a,itm_kuyak_a,itm_rus_cav_boots,itm_mail_gloves,itm_mail_gauntlets,itm_saddle_horse,itm_rus_horse],
   def_attrib_multiplayer|str_21|agi_15|level(20),wp(150),knows_riding_4|knows_ironflesh_3|knows_shield_6|knows_power_strike_6|knows_power_throw_1|knows_horse_archery_1|knows_athletics_3,rhodok_face_middle_1, rhodok_face_older_2],
  
  ["sarranid_infantry_multiplayer_ai","Templar Infantry","Templar Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_sword_medieval_c,itm_sword_medieval_c_small,itm_one_handed_battle_axe_a,itm_longsword_c,itm_war_spear,itm_tab_shield_kite_c,itm_tab_shield_kite_d,itm_javelin,
    itm_helmet_a,itm_nasal_helmet_c,itm_segmented_helmet_b,itm_skullcap_c,itm_skullcap_d,itm_surcoat_over_mail_heraldic,itm_padded_cloth_c,itm_surcoa_over_mail_and_plate_white,itm_mail_chausses,itm_nomad_boots,itm_leather_gloves],
   def_attrib_multiplayer|str_21|agi_15|level(19),wpex(150,150,150,30,50,120),knows_ironflesh_4|knows_shield_5|knows_power_throw_3|knows_power_strike_7|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["sarranid_archer_multiplayer_ai","Templar Crossbowman","Templar Crossbowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_steel_bolts,itm_heavy_crossbow,itm_fighting_pick,itm_one_handed_battle_axe_a,itm_sword_medieval_c,
    itm_kettle_hat_g,itm_chapel_de_fer_e,itm_padded_cloth_c,itm_padded_cloth,itm_woolen_hose,itm_leather_gloves],
   def_attrib_multiplayer|str_14|agi_15|level(19),wpe(80,60,180,80),knows_ironflesh_2|knows_athletics_5|knows_power_strike_2|knows_shield_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["sarranid_horseman_multiplayer_ai","Templar Horseman","Templar Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_lance,itm_sword_medieval_c,itm_sword_medieval_c_long,itm_tab_shield_kite_cav_a,itm_tab_shield_kite_cav_b,
    itm_helmet_a,itm_nasal_helmet_c,itm_surcoat_over_mail_heraldic,itm_surcoa_over_mail_and_plate_white,itm_mail_chausses,itm_nomad_boots,itm_leather_gloves,itm_hunter,itm_saddle_horse,itm_courser],
   def_attrib_multiplayer|str_21|agi_15|level(19),wpe(150,90,60,110),knows_riding_5|knows_ironflesh_3|knows_power_strike_6|knows_shield_5|knows_power_throw_2|knows_horse_archery_1,vaegir_face_young_1, vaegir_face_older_2],

  ["eques_veteran_crossbowman_multiplayer_ai","Eques Crossbowman","Eques Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_fighting_pick,itm_winged_mace,itm_sword_medieval_b_small,itm_sword_medieval_b,itm_crossbow,itm_heavy_crossbow,itm_steel_bolts,itm_bolts,
    itm_kettle_hat_i,itm_black_hood,itm_padded_cloth_b,itm_ragged_outfit,itm_khergit_leather_boots,itm_black_leather_gloves],
   def_attrib_multiplayer|str_14|agi_15|level(20),wpe(100,60,180,90),knows_common|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_5|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["eques_veteran_spearman_multiplayer_ai","Eques Sergeant","Eques Sergeant",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_7,
   [itm_grosse_messer_a,itm_grosse_messer_b,itm_bastard_sword_b,itm_great_axe,itm_sword_two_handed_a,itm_long_axe_c,itm_pike,itm_tab_shield_pavise_c,itm_tab_shield_pavise_d,
    itm_guard_helmet,itm_gotland_helmet,itm_banded_armor_b,itm_heavy_gotland_armor,itm_norman_shoes,itm_wisby_gauntlets_black,itm_wisby_gloves_black],
   def_attrib_multiplayer|str_21|agi_15|level(20),wpex(150,150,150,30,50,110),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_7|knows_power_throw_3|knows_athletics_6|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["eques_scout_multiplayer_ai","Eques Horseman","Eques Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_lance,itm_sword_medieval_d_long,itm_great_axe,itm_executioner_sword_a,itm_tab_shield_heater_cav_b,
    itm_great_helmet_j,itm_topfhelm,itm_gotland_helmet,itm_plated_light_brigandine,itm_transitional_black,itm_norman_shoes,itm_iron_greaves,itm_wisby_gloves,itm_wisby_gauntlets_black,itm_hunter,itm_saddle_horse,itm_courser],
   def_attrib_multiplayer|str_21|agi_15|level(20),wp(150),knows_riding_5|knows_ironflesh_3|knows_shield_5|knows_power_strike_6|knows_power_throw_1|knows_horse_archery_1|knows_athletics_3,rhodok_face_middle_1, rhodok_face_older_2],
    
  ["norse_veteran_multiplayer_ai","Norse Footman","Norse Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_8,
   [itm_sword_viking_3,itm_war_spear,itm_thegn_sword,itm_tab_shield_round_d,
    itm_nordic_huscarl_helmet,itm_nordic_helmet,itm_heraldic_mail_with_tabard,itm_studded_leather_coat,itm_mail_chausses,itm_norman_shoes,itm_lamellar_gauntlets,itm_scale_gloves_a],
   def_attrib_multiplayer|str_21|agi_15|level(24),wpex(150,150,150,40,60,140),knows_ironflesh_8|knows_power_strike_8|knows_power_throw_4|knows_athletics_6|knows_shield_7|knows_riding_1,nord_face_young_1, nord_face_older_2],
  ["norse_scout_multiplayer_ai","Norse Scout","Norse Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_sword_viking_3,itm_sword_viking_a_long,itm_tab_shield_round_d,
    itm_nordic_huscarl_helmet,itm_nordic_helmet,itm_mail_hauberk,itm_dark_hauberk,itm_mail_chausses,itm_norman_shoes,itm_mail_mittens,itm_mail_gauntlets,itm_saddle_horse,itm_sumpter_horse],
   def_attrib_multiplayer|str_21|agi_15|level(19),wp(155),knows_riding_5|knows_ironflesh_3|knows_power_strike_6|knows_shield_6|knows_horse_archery_2|knows_power_throw_3|knows_horse_archery_2|knows_athletics_3,vaegir_face_young_1, vaegir_face_older_2],
  ["norse_archer_multiplayer_ai","Norse Archer","Norse Archers",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_long_bow,itm_bodkin_arrows,itm_one_handed_battle_axe_a,itm_sword_viking_2,itm_sword_viking_2_small,
    itm_nordic_fighter_helmet,itm_nordic_helmet,itm_byrnja,itm_byrnja_b,itm_leather_boots,itm_nomad_boots,itm_leather_gloves],
   def_attrib_multiplayer|str_12|agi_15|level(15),wpe(90,180,60,80),knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_power_draw_5|knows_athletics_4|knows_riding_1,nord_face_young_1, nord_face_old_2],

  ["order_crossbowman_multiplayer_ai","ODE Crossbowman","ODE Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_9,
   [itm_crossbow,itm_heavy_crossbow,itm_bolts,itm_steel_bolts,itm_military_hammer,itm_fighting_pick,itm_falchion_c,itm_falchion,
    itm_kettle_hat,itm_helmet_with_neckguard,itm_heraldic_mail_with_tunic,itm_haubergeon,itm_mail_chausses,itm_leather_boots,itm_mail_mittens,itm_mail_gloves],
   def_attrib_multiplayer|str_14|agi_15|level(20),wpe(100,60,180,90),knows_common|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_5|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["order_footman_multiplayer_ai","ODE Footman","ODE Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_9,
   [itm_falchion_b,itm_military_hammer,itm_morningstar,itm_bastard_sword_a,itm_french_longsword,itm_battle_fork,itm_tab_shield_heater_d,itm_tab_shield_heater_c,
    itm_full_helm,itm_chapel_de_fer_g,itm_surcoa_over_mail_and_plate_blue,itm_brigandine_blue_a,itm_hose_kneecops_red,itm_hose_kneecops_green,itm_hourglass_gauntlets_a,itm_hourglass_gloves],
   def_attrib_multiplayer|str_21|agi_15|level(20),wpex(150,150,150,30,50,110),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_7|knows_power_throw_1|knows_athletics_6|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["order_knight_multiplayer_ai","ODE Knight","ODE Knights",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_9,
   [itm_lance,itm_heavy_lance,itm_bastard_sword_a,itm_espada_eslavona_a,itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_a,
    itm_open_sallet,itm_open_sallet_coif,itm_surcoa_over_mail_and_plate_blue,itm_surcoat_over_mail_blue,itm_hose_kneecops_green,itm_hose_kneecops_red,itm_hourglass_gauntlets_a,itm_hourglass_gloves,itm_hunter,itm_courser],
   def_attrib_multiplayer|str_21|agi_15|level(20),wp(150),knows_riding_6|knows_ironflesh_3|knows_shield_5|knows_power_strike_6|knows_power_throw_1|knows_horse_archery_1|knows_athletics_3,rhodok_face_middle_1, rhodok_face_older_2],
       
#Multiplayer troops (they must have the base items only, nothing else)
  ["swadian_crossbowman_multiplayer","Polan's Crossbowman","Polan's Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_sword_medieval_b_small,itm_tab_shield_heater_a,
   itm_white_kaftan,itm_hide_boots],
   def_attrib_multiplayer|str_14|agi_15|level(19),wpe(90,60,180,90),knows_common|knows_ironflesh_2|knows_athletics_5|knows_shield_5|knows_power_strike_2|knows_riding_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer","Polan's Infantry","Polan's Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_tab_shield_pavise_a,
   itm_red_kaftan,itm_serbian_ankle_boots],
   def_attrib_multiplayer|str_21|agi_15|level(20),wpex(155,150,150,40,60,110),knows_common|knows_ironflesh_5|knows_shield_6|knows_power_strike_7|knows_power_throw_3|knows_athletics_6|knows_riding_1,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer","Polan's Man at Arms","Polan's Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_lance,itm_sword_medieval_a,itm_tab_shield_heater_cav_a,
    itm_red_shirt,itm_ankle_boots,itm_courser],
   def_attrib_multiplayer|str_21|agi_15|level(20),wpex(150,150,150,40,60,110),knows_common|knows_riding_5|knows_ironflesh_3|knows_shield_5|knows_power_throw_2|knows_power_strike_6|knows_athletics_3,swadian_face_young_1, swadian_face_old_2],


  ["vaegir_archer_multiplayer","Grey Archer","Grey Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_scimitar,itm_hunting_bow,
    itm_tunic_with_green_cape,itm_wrapping_boots],
   def_attrib_multiplayer|str_14|agi_15|level(19),wpe(80,180,60,80),knows_ironflesh_2|knows_power_draw_6|knows_athletics_4|knows_shield_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_crossbowman_multiplayer","Grey Crossboman","Grey Crossbomen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_bolts,itm_mace_2,itm_light_crossbow,
    itm_tunic_with_green_cape,itm_wrapping_boots],
   def_attrib_multiplayer|str_13|agi_15|level(19),wpe(80,60,180,80),knows_ironflesh_2|knows_power_draw_6|knows_athletics_4|knows_shield_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer","Grey Footman","Grey Footmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_tab_shield_kite_a, itm_mace_2,
    itm_tunic_with_green_cape,itm_wrapping_boots],
   def_attrib_multiplayer|str_21|agi_15|level(19),wpex(150,150,150,30,50,120),knows_ironflesh_4|knows_shield_5|knows_power_throw_3|knows_power_strike_7|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer","Grey Horseman","Grey Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_scimitar,itm_lance,itm_tab_shield_heater_cav_a,
    itm_tunic_with_green_cape,itm_wrapping_boots,itm_saddle_horse],
   def_attrib_multiplayer|str_21|agi_15|level(19),wpe(150,90,60,110),knows_riding_5|knows_ironflesh_3|knows_power_strike_6|knows_shield_5|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2],
  
  ["tengri_archer_multiplayer","Tengri Archer","Tengri Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_arabian_sword_a,itm_nomad_bow,itm_arrows,
    itm_skirmisher_armor,itm_deli_cap,itm_turkish_shoes],
   def_attrib_multiplayer|str_12|agi_15|level(21),wpe(70,180,60,100),knows_riding_2|knows_power_draw_3|knows_horse_archery_2|knows_athletics_4,khergit_face_middle_1, khergit_face_older_2],
  ["tengri_infantry_multiplayer","Tengri Infantry","Tengri Infantry",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_arabian_sword_a,itm_tab_shield_kite_a,itm_spear,
    itm_sarranid_cloth_robe,itm_deli_cap,itm_turkish_shoes],
   def_attrib_multiplayer|str_21|agi_15|level(19),wpex(150,150,150,30,50,120),knows_ironflesh_4|knows_shield_5|knows_power_throw_3|knows_power_strike_7|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["tengri_lancer_multiplayer","Tengri Lancer","Tengri Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_arabian_sword_a,itm_lance,itm_tab_shield_small_round_a,
    itm_sarranid_cloth_robe,itm_deli_cap,itm_turkish_shoes,itm_saddle_horse],
   def_attrib_multiplayer|str_21|agi_15|level(21),wp(155),knows_riding_5|knows_ironflesh_3|knows_power_throw_3|knows_shield_5|knows_power_strike_6|knows_athletics_5,khergit_face_middle_1, khergit_face_older_2],
  
  ["kalmarunionen_archer_multiplayer","Kalmarunionen Archer","Kalmarunionen Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_2_small,itm_hunting_bow,
    itm_rawhide_coat,itm_hide_boots],
   def_attrib_multiplayer|str_12|agi_15|level(15),wpe(90,180,60,80),knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_power_draw_5|knows_athletics_4|knows_riding_1,nord_face_young_1, nord_face_old_2],
  ["kalmarunionen_veteran_multiplayer","Kalmarunionen Huscarl","Kalmarunionen Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_wooden_shield,
    itm_coarse_tunic,itm_hide_boots],
   def_attrib_multiplayer|str_21|agi_15|level(24),wpex(150,150,150,40,60,140),knows_ironflesh_4|knows_power_strike_7|knows_power_throw_4|knows_athletics_6|knows_shield_5|knows_riding_1,nord_face_young_1, nord_face_older_2],
  ["kalmarunionen_scout_multiplayer","Kalmarunionen Horseman","Kalmarunionen Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_lance,itm_tab_shield_small_round_a,
    itm_coarse_tunic,itm_hide_boots,itm_saddle_horse],
   def_attrib_multiplayer|str_21|agi_15|level(19),wp(155),knows_riding_5|knows_ironflesh_2|knows_power_strike_5|knows_shield_5|knows_horse_archery_2|knows_power_throw_3|knows_athletics_3,vaegir_face_young_1, vaegir_face_older_2],
  ["kalmarunionen_pikeman_multiplayer","Kalmarunionen Pikeman","Kalmarunionen Pikemen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_spear,
    itm_coarse_tunic,itm_hide_boots],
   def_attrib_multiplayer|str_21|agi_15|level(24),wpex(110,135,180,40,60,140),knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_athletics_6|knows_riding_1,nord_face_young_1, nord_face_older_2],


   
  ["druzhina_veteran_archer_multiplayer","Druzhina Archer","Druzhina Archers",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_hunting_bow,itm_arrows,itm_mace_4,
    itm_short_tunic,itm_rus_shoes],
   def_attrib_multiplayer|str_12|agi_15|level(20),wpe(100,180,60,90),knows_common|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_power_draw_6|knows_athletics_5|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["druzhina_sergeant_multiplayer","Druzhina Sergeant","Druzhina Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_spiked_club,itm_tab_shield_kite_a,itm_spear,
    itm_short_tunic,itm_rus_shoes],
   def_attrib_multiplayer|str_21|agi_15|level(20),wpex(150,150,150,30,50,110),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_7|knows_power_throw_1|knows_athletics_6|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["druzhina_horseman_multiplayer","Druzhina Horseman","Druzhina Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_scimitar,itm_tab_shield_kite_cav_a, itm_light_lance, 
    itm_short_tunic,itm_rus_shoes,itm_saddle_horse],
   def_attrib_multiplayer|str_21|agi_15|level(20),wp(150),knows_riding_4|knows_ironflesh_3|knows_shield_6|knows_power_strike_6|knows_power_throw_1|knows_athletics_3,rhodok_face_middle_1, rhodok_face_older_2],
 
  ["templar_crossbowman_multiplayer","Templar Crossbowman","Templar Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_bolts,itm_mace_2,itm_light_crossbow,
    itm_linen_tunic, itm_wrapping_boots],
   def_attrib_multiplayer|str_14|agi_15|level(19),wpe(80,60,180,80),knows_ironflesh_2|knows_athletics_5|knows_power_strike_2|knows_shield_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["templar_footman_multiplayer","Templar Footman","Templar footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_tab_shield_kite_a, itm_sword_medieval_a,
    itm_linen_tunic, itm_wrapping_boots],
   def_attrib_multiplayer|str_21|agi_15|level(19),wpex(150,150,150,30,50,120),knows_ironflesh_4|knows_shield_5|knows_power_throw_3|knows_power_strike_7|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["templar_knight_multiplayer","Templar Knight","Templar Knights",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_sword_medieval_b,itm_lance,itm_tab_shield_kite_cav_a,
    itm_linen_tunic, itm_wrapping_boots,itm_saddle_horse],
   def_attrib_multiplayer|str_21|agi_15|level(19),wpe(150,90,60,110),knows_riding_5|knows_ironflesh_3|knows_power_strike_6|knows_shield_5|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2],

  ["eques_veteran_crossbowman_multiplayer","Eques Crossbowman","Eques Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_crossbow,itm_bolts,itm_winged_mace,
    itm_shirt,itm_hide_boots],
   def_attrib_multiplayer|str_14|agi_15|level(20),wpe(100,60,180,90),knows_common|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_5|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["eques_sergeant_multiplayer","Eques Sergeant","Eques Sergeants",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_fighting_pick,itm_tab_shield_pavise_a,itm_spear,
    itm_shirt,itm_hide_boots],
   def_attrib_multiplayer|str_21|agi_15|level(20),wpex(150,150,150,30,50,110),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_7|knows_power_throw_1|knows_athletics_6|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["eques_horseman_multiplayer","Eques Horseman","Eques Horsemen",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_sword_medieval_a,itm_tab_shield_heater_cav_a, itm_light_lance, 
    itm_shirt,itm_hide_boots,itm_saddle_horse],
   def_attrib_multiplayer|str_21|agi_15|level(20),wp(150),knows_riding_5|knows_ironflesh_3|knows_shield_5|knows_power_strike_6|knows_power_throw_1|knows_athletics_3,rhodok_face_middle_1, rhodok_face_older_2],
 
  ["norse_archer_multiplayer","Norse Archer","Norse Archers",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_arrows,itm_sword_viking_2_small,itm_hunting_bow,
    itm_linen_shirt_a,itm_hide_boots],
   def_attrib_multiplayer|str_12|agi_15|level(15),wpe(90,180,60,80),knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_power_draw_5|knows_athletics_4|knows_riding_1,nord_face_young_1, nord_face_old_2],
  ["norse_veteran_multiplayer","Norse Huscarl","Norse Huscarls",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_sword_viking_1,itm_tab_shield_round_a,
    itm_linen_shirt_a,itm_hide_boots],
   def_attrib_multiplayer|str_21|agi_15|level(24),wpex(150,150,150,40,60,140),knows_ironflesh_8|knows_power_strike_8|knows_power_throw_4|knows_athletics_6|knows_shield_7|knows_riding_1,nord_face_young_1, nord_face_older_2],
  ["norse_axeman_multiplayer","Norse Axeman","Norse Axemen",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_one_handed_war_axe_a,itm_tab_shield_round_a,
    itm_linen_shirt_a,itm_hide_boots],
   def_attrib_multiplayer|level(24),wpex(150,150,150,40,60,140),knows_ironflesh_8|knows_power_strike_8|knows_power_throw_4|knows_athletics_6|knows_shield_7|knows_riding_1,nord_face_young_1, nord_face_older_2],
  ["norse_scout_multiplayer","Norse Scout","Norse Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_sword_viking_1,itm_tab_shield_round_a,
    itm_linen_shirt_a,itm_hide_boots,itm_saddle_horse],
   def_attrib_multiplayer|str_21|agi_15|level(19),wp(155),knows_riding_5|knows_ironflesh_3|knows_power_strike_6|knows_shield_6|knows_horse_archery_2|knows_power_throw_3|knows_athletics_3,vaegir_face_young_1, vaegir_face_older_2],
 
  ["order_crossbowman_multiplayer","ODE Crossbowman","ODE Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_9,
   [itm_crossbow,itm_bolts,itm_falchion,
    itm_blue_tunic,itm_blue_hose],
   def_attrib_multiplayer|str_14|agi_15|level(20),wpe(100,60,180,90),knows_common|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_5|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["order_footman_multiplayer","ODE Footman","ODE Footmen",tf_guarantee_all,0,0,fac_kingdom_9,
   [itm_falchion,itm_tab_shield_heater_a,itm_military_fork,
    itm_blue_tunic,itm_blue_hose],
   def_attrib_multiplayer|str_21|agi_15|level(20),wpex(150,150,150,30,50,110),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_7|knows_power_throw_1|knows_athletics_6|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["order_knight_multiplayer","ODE Knight","ODE Knights",tf_guarantee_all,0,0,fac_kingdom_9,
   [itm_military_pick,itm_tab_shield_heater_cav_a, itm_light_lance, 
    itm_blue_tunic,itm_blue_hose,itm_saddle_horse],
   def_attrib_multiplayer|str_21|agi_15|level(20),wp(150),knows_riding_6|knows_ironflesh_3|knows_shield_5|knows_power_strike_6|knows_power_throw_1|knows_athletics_3,rhodok_face_middle_1, rhodok_face_older_2],
 


   ["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   
   #Player history array
  ["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],

  ["quick_battle_troop_1","Rodrigo de Braganca","Rodrigo de Braganca", tf_hero,0,0,fac_kingdom_1,
   [itm_long_hafted_knobbed_mace, itm_wooden_shield, itm_staff, itm_throwing_daggers,
    itm_felt_hat, itm_fur_coat, itm_light_leather_boots, itm_leather_gloves],
   str_9|agi_15|int_12|cha_12|level(15),wpex(109,33,132,15,32,100),knows_riding_3|knows_athletics_5|knows_shield_3|knows_weapon_master_3|knows_power_throw_3|knows_power_strike_2|knows_ironflesh_3,0x0000000e240070cd598bb02b9556428c00000000001eabce0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_2","Usiatra","Usiatra", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_nomad_bow, itm_barbed_arrows, itm_scimitar, itm_tab_shield_small_round_c, itm_sumpter_horse,
    itm_leather_armor, itm_splinted_greaves],
   str_12|agi_14|int_11|cha_18|level(22),wpex(182,113,112,159,82,115),knows_horse_archery_2|knows_riding_3|knows_athletics_4|knows_shield_2|knows_weapon_master_4|knows_power_draw_2|knows_power_throw_1|knows_power_strike_3|knows_ironflesh_4,0x000000007f004000719b69422165b71300000000001d5d1d0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_3","Hegen","Hegen", tf_hero,0,0,fac_kingdom_1,
   [itm_heavy_lance, itm_sword_two_handed_b, itm_sword_medieval_c, itm_tab_shield_heater_c, itm_warhorse,
    itm_guard_helmet, itm_coat_of_plates, itm_mail_mittens, itm_mail_boots],
   str_18|agi_16|int_12|cha_11|level(24),wpex(90,152,102,31,33,34),knows_riding_5|knows_athletics_5|knows_shield_3|knows_weapon_master_5|knows_power_strike_6|knows_ironflesh_6,0x000000018000324428db8a431491472400000000001e44a90000000000000000, swadian_face_old_2],
  ["quick_battle_troop_4","Konrad","Konrad", tf_hero,0,0,fac_kingdom_1,
   [itm_sword_two_handed_a, itm_mace_4, itm_tab_shield_kite_d,
    itm_bascinet_3, itm_scale_armor, itm_mail_mittens, itm_mail_boots],
   str_18|agi_15|int_12|cha_12|level(24),wpex(130,150,130,30,50,90),knows_riding_2|knows_athletics_5|knows_shield_4|knows_weapon_master_5|knows_power_throw_3|knows_power_strike_6|knows_ironflesh_6,0x000000081700205434db6df4636db8e400000000001db6e30000000000000000, swadian_face_old_2],
  ["quick_battle_troop_5","Sverre","Sverre", tf_hero,0,0,fac_kingdom_1,
   [itm_long_axe, itm_sword_viking_1, itm_light_throwing_axes, itm_tab_shield_round_d,
    itm_nordic_fighter_helmet, itm_byrnie, itm_leather_gloves, itm_leather_boots],
   str_15|agi_15|int_12|cha_12|level(21),wpex(110,130,110,80,15,110),knows_riding_1|knows_athletics_5|knows_shield_4|knows_weapon_master_5|knows_power_draw_2|knows_power_throw_4|knows_power_strike_5|knows_ironflesh_5,0x000000048a00024723134e24cb51c91b00000000001dc6aa0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_6","Borislav","Borislav", tf_hero,0,0,fac_kingdom_1,
   [itm_strong_bow, itm_barbed_arrows, itm_barbed_arrows, itm_shortened_spear,
    itm_leather_warrior_cap, itm_leather_jerkin, itm_leather_gloves, itm_ankle_boots],
   str_12|agi_15|int_15|cha_9|level(18),wpex(70,70,100,140,15,100),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_weapon_master_3|knows_power_draw_4|knows_power_throw_3|knows_power_strike_2|knows_ironflesh_2,0x000000089e00444415136e36e34dc8e400000000001d46d90000000000000000, swadian_face_old_2],
  ["quick_battle_troop_7","Stavros","Stavros", tf_hero,0,0,fac_kingdom_1,
   [itm_heavy_crossbow, itm_bolts, itm_sword_medieval_b_small, itm_tab_shield_pavise_c,
    itm_nasal_helmet, itm_padded_leather, itm_leather_gloves, itm_leather_boots],
   str_12|agi_15|int_15|cha_12|level(21),wpex(100,70,70,30,140,80),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_shield_3|knows_weapon_master_5|knows_power_throw_2|knows_power_strike_4|knows_ironflesh_4,0x0000000e1400659226e34dcaa46e36db00000000001e391b0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_8","Gamara","Gamara", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_throwing_spears, itm_throwing_spears, itm_scimitar, itm_leather_covered_round_shield,
    itm_desert_turban, itm_skirmisher_armor, itm_leather_gloves, itm_sarranid_boots_b],
   str_12|agi_15|int_12|cha_12|level(18),wpex(100,40,100,85,15,130),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_shield_2|knows_weapon_master_4|knows_power_draw_2|knows_power_throw_4|knows_power_strike_2|knows_ironflesh_2,0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_9","Aethrod","Aethrod", tf_hero,0,0,fac_kingdom_1,
   [itm_nomad_bow, itm_barbed_arrows, itm_barbed_arrows, itm_scimitar_b,
    itm_splinted_greaves, itm_lamellar_vest],
   str_16|agi_21|int_12|cha_14|level(26),wpex(182,113,112,159,82,115),knows_horse_archery_2|knows_riding_2|knows_athletics_7|knows_shield_2|knows_weapon_master_4|knows_power_draw_7|knows_power_throw_3|knows_power_strike_3|knows_ironflesh_4,0x000000000000210536db6db6db6db6db00000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_10","Zaira","Zaira", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_sarranid_cavalry_sword, itm_strong_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_arabian_horse_b,
    itm_sarranid_felt_head_cloth_b, itm_sarranid_common_dress, itm_sarranid_boots_b],
   str_13|agi_18|int_15|cha_9|level(18),wpex(126,19,23,149,41,26),knows_horse_archery_6|knows_riding_6|knows_weapon_master_2|knows_power_draw_4|knows_power_throw_1|knows_power_strike_4|knows_ironflesh_1,0x0000000502003001471a6a24dc6594cb00000000001da4840000000000000000, swadian_face_old_2],
  ["quick_battle_troop_11","Argo Sendnar","Argo Sendnar", tf_hero,0,0,fac_kingdom_1,
   [itm_morningstar, itm_tab_shield_round_d, itm_war_spear, itm_courser,
    itm_leather_gloves, itm_fur_hat, itm_leather_boots, itm_leather_jacket],
   str_15|agi_12|int_14|cha_20|level(28),wpex(101,35,136,15,17,19),knows_riding_4|knows_athletics_2|knows_shield_4|knows_weapon_master_4|knows_power_strike_5|knows_ironflesh_5,0x0000000e800015125adb702de3459a9c00000000001ea6d00000000000000000, swadian_face_old_2],
  ["quick_battle_troops_end","{!}quick_battle_troops_end","{!}quick_battle_troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  ["tutorial_fighter_1","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088c1073144252b1929a85569300000000000496a50000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_2","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_3","Regular Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(9),wp_melee(50),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_4","Veteran Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(16),wp_melee(110),knows_athletics_1|knows_ironflesh_3|knows_power_strike_2|knows_shield_2,0x000000089910324a495175324949671800000000001cd8ab0000000000000000, vaegir_face_older_2],
  ["tutorial_archer_1","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_leather_jerkin,itm_leather_vest,itm_nomad_boots,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["tutorial_master_archer","Archery Trainer","Archery Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000, vaegir_face_older_2],
  ["tutorial_rider_1","Rider","{!}Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_hunter, itm_saddle_horse,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_riding_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["tutorial_rider_2","Horse archer","{!}Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_tribal_warrior_outfit,itm_nomad_robe,itm_hide_boots,itm_tab_shield_small_round_a,itm_steppe_horse],
   def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,khergit_face_young_1, khergit_face_older_2],
  ["tutorial_master_horseman","Riding Trainer","Riding Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_leather_vest,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000, vaegir_face_older_2],
   
  ["swadian_merchant", "Merchant of Praven", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_4, [itm_sword_two_handed_a, itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["vaegir_merchant", "Merchant of Reyvadin", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_5, [itm_sword_two_handed_a, itm_nobleman_outfit, itm_woolen_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["khergit_merchant", "Merchant of Tulga", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_1, [itm_sword_two_handed_a, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["nord_merchant", "Merchant of Sargoth", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_2, [itm_sword_two_handed_a, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["rhodok_merchant", "Merchant of Jelkala", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_3, [itm_sword_two_handed_a, itm_leather_jerkin, itm_blue_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["sarranid_merchant", "Merchant of Shariz", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_6, [itm_sword_two_handed_a, itm_sarranid_cloth_robe, itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],       
  ["eques_merchant", "Merchant of Sunos", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_7, [itm_sword_two_handed_a, itm_leather_jerkin, itm_blue_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["norse_merchant", "Merchant of coss", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_8, [itm_sword_two_handed_a, itm_leather_jerkin, itm_blue_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["ode_merchant", "Merchant of cosss", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_9, [itm_sword_two_handed_a, itm_leather_jerkin, itm_blue_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
   

 ["startup_merchants_end","startup_merchants_end","startup_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],
 
  ["sea_raider_leader","Sea Raider Captain","Sea Raiders",tf_hero|tf_guarantee_all_wo_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_battle_axe,itm_spear,itm_nordic_shield,itm_nordic_shield,itm_nordic_shield,itm_wooden_shield,itm_long_bow,itm_javelin,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_helmet,itm_nasal_helmet,itm_mail_shirt,itm_byrnie,itm_mail_hauberk,itm_leather_boots, itm_nomad_boots],
   def_attrib|level(24),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],

  ["looter_leader","Robber","Looters",tf_hero,0,0,fac_outlaws,
   [itm_hatchet,itm_club,itm_butchering_knife,itm_falchion,itm_rawhide_coat,itm_stones,itm_nomad_armor,itm_nomad_armor,itm_woolen_cap,itm_woolen_cap,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(20),knows_common,0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2],
   
  ["bandit_leaders_end","bandit_leaders_end","bandit_leaders_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],   
  
  ["relative_of_merchant", "Merchant's Brother", "{!}Prominent",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2, 0x00000000320410022d2595495491afa400000000001d9ae30000000000000000, mercenary_face_2],   
   
  ["relative_of_merchants_end","relative_of_merchants_end","relative_of_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],     

  ["swadian_crossbowman_multiplayer_coop_tier_1","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_hunting_crossbow,itm_bolts,itm_fighting_pick,itm_tab_shield_heater_a,itm_arming_cap,itm_padded_cloth,itm_ankle_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["swadian_infantry_multiplayer_coop_tier_1","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_spiked_club,itm_tab_shield_heater_b,itm_felt_hat,itm_leather_apron,itm_wrapping_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["swadian_man_at_arms_multiplayer_coop_tier_1","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_light_lance,itm_sword_medieval_b_small,itm_tab_shield_heater_a,itm_leather_cap,itm_leather_gloves,itm_padded_cloth,itm_wrapping_boots,itm_warhorse],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_archer_multiplayer_coop_tier_1","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_axe,itm_hunting_bow,itm_linen_tunic,itm_nomad_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_spearman_multiplayer_coop_tier_1","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_tab_shield_kite_a, itm_axe,itm_rawhide_coat,itm_hide_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_horseman_multiplayer_coop_tier_1","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_spear,itm_tab_shield_kite_cav_a,itm_linen_tunic,itm_hide_boots,itm_hunter],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_veteran_horse_archer_multiplayer_coop_tier_1","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_nomad_bow,itm_arrows,itm_steppe_armor,itm_hide_boots,itm_steppe_horse],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_infantry_multiplayer_coop_tier_1","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_tab_shield_small_round_a,itm_steppe_armor,itm_hide_boots,itm_leather_gloves],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_lancer_multiplayer_coop_tier_1","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_spear,itm_tab_shield_small_round_a,itm_steppe_armor,itm_steppe_cap,itm_hide_boots,itm_leather_gloves,itm_courser],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_archer_multiplayer_coop_tier_1","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_2_small,itm_short_bow,itm_blue_tunic,itm_leather_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_veteran_multiplayer_coop_tier_1","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_one_handed_war_axe_a,itm_tab_shield_round_a,itm_blue_tunic,itm_leather_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_scout_multiplayer_coop_tier_1","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_war_spear,itm_tab_shield_small_round_a,itm_blue_tunic,itm_leather_boots,itm_saddle_horse],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_veteran_crossbowman_multiplayer_coop_tier_1","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_crossbow,itm_bolts,itm_fighting_pick,itm_tab_shield_pavise_a,itm_tunic_with_green_cape,itm_ankle_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_sergeant_multiplayer_coop_tier_1","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_military_cleaver_b,itm_tab_shield_pavise_a,itm_darts,itm_green_tunic,itm_ankle_boots,itm_leather_cap],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_horseman_multiplayer_coop_tier_1","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_tab_shield_heater_cav_a, itm_light_lance, itm_green_tunic,itm_ankle_boots,itm_padded_coif,itm_saddle_horse],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_archer_multiplayer_coop_tier_1","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arrows,itm_sarranid_mace_1,itm_short_bow,itm_sarranid_cloth_robe, itm_sarranid_boots_b],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_footman_multiplayer_coop_tier_1","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_tab_shield_kite_a, itm_sarranid_axe_a,itm_sarranid_cloth_robe, itm_sarranid_boots_b],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_mamluke_multiplayer_coop_tier_1","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_lance,itm_tab_shield_small_round_a,itm_sarranid_cloth_robe, itm_sarranid_boots_b,itm_arabian_horse_a],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],

  ["swadian_crossbowman_multiplayer_coop_tier_2","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_spiked_club,itm_crossbow,itm_bolts,itm_tab_shield_heater_b,itm_arming_cap,itm_red_gambeson,itm_ankle_boots],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["swadian_infantry_multiplayer_coop_tier_2","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_b,itm_tab_shield_heater_c,itm_spear,itm_mail_coif,itm_leather_gloves,itm_mail_with_tunic_red,itm_ankle_boots],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["swadian_man_at_arms_multiplayer_coop_tier_2","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_lance,itm_sword_medieval_a,itm_tab_shield_heater_b,itm_helmet_with_neckguard,itm_leather_gloves,itm_haubergeon,itm_leather_boots,itm_warhorse],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_archer_multiplayer_coop_tier_2","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_barbed_arrows,itm_axe,itm_nomad_bow,itm_leather_vest,itm_nomad_boots,itm_vaegir_fur_helmet],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_spearman_multiplayer_coop_tier_2","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_javelin,itm_scimitar,itm_tab_shield_kite_b,itm_leather_jerkin,itm_nomad_boots,itm_vaegir_lamellar_helmet,itm_leather_gloves],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_horseman_multiplayer_coop_tier_2","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_war_spear,itm_tab_shield_kite_cav_b,itm_javelin,itm_studded_leather_coat,itm_leather_gloves,itm_nomad_boots,itm_vaegir_lamellar_helmet,itm_hunter],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_veteran_horse_archer_multiplayer_coop_tier_2","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_2,itm_khergit_bow,itm_barbed_arrows,itm_steppe_armor,itm_leather_steppe_cap_a,itm_nomad_boots,itm_steppe_horse],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_infantry_multiplayer_coop_tier_2","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_2,itm_tab_shield_small_round_b,itm_javelin,itm_tribal_warrior_outfit,itm_nomad_boots,itm_leather_gloves],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_lancer_multiplayer_coop_tier_2","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_war_spear,itm_tab_shield_small_round_b,itm_javelin,itm_tribal_warrior_outfit,itm_leather_steppe_cap_b,itm_nomad_boots,itm_courser],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_archer_multiplayer_coop_tier_2","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_2,itm_long_bow,itm_leather_jerkin,itm_leather_boots,itm_nordic_archer_helmet],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_veteran_multiplayer_coop_tier_2","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_one_handed_war_axe_a,itm_tab_shield_round_b,itm_throwing_axes,itm_leather_jerkin,itm_leather_boots,itm_nordic_footman_helmet,itm_leather_gloves],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_scout_multiplayer_coop_tier_2","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_lance,itm_tab_shield_small_round_a,itm_leather_jerkin,itm_leather_boots,itm_leather_gloves,itm_nordic_footman_helmet,itm_saddle_horse],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_veteran_crossbowman_multiplayer_coop_tier_2","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_heavy_crossbow,itm_bolts,itm_club_with_spike_head,itm_tab_shield_pavise_b,itm_leather_armor,itm_leather_boots,itm_leather_gloves,itm_leather_cap],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_sergeant_multiplayer_coop_tier_2","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_military_cleaver_b,itm_tab_shield_pavise_b,itm_war_darts,itm_padded_cloth,itm_leather_boots,itm_leather_gloves,itm_footman_helmet],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_horseman_multiplayer_coop_tier_2","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_tab_shield_heater_cav_b, itm_heavy_lance,itm_javelin,itm_padded_cloth,itm_leather_boots,itm_leather_gloves,itm_footman_helmet,itm_saddle_horse],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_archer_multiplayer_coop_tier_2","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_barbed_arrows,itm_sarranid_mace_1,itm_nomad_bow,itm_archers_vest,itm_desert_turban,itm_leather_gloves,itm_sarranid_boots_b],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_footman_multiplayer_coop_tier_2","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_tab_shield_kite_b, itm_sarranid_axe_b,itm_javelin,itm_archers_vest,itm_sarranid_warrior_cap,itm_leather_gloves,itm_sarranid_boots_b],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_mamluke_multiplayer_coop_tier_2","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_heavy_lance,itm_tab_shield_small_round_b,itm_javelin,itm_archers_vest, itm_sarranid_warrior_cap,itm_leather_gloves,itm_sarranid_boots_b,itm_arabian_horse_a],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],

  ["swadian_crossbowman_multiplayer_coop_tier_3","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_b,itm_heavy_crossbow,itm_steel_bolts,itm_tab_shield_heater_c,itm_segmented_helmet,itm_leather_jerkin,itm_leather_boots],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["swadian_infantry_multiplayer_coop_tier_3","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bastard_sword_a,itm_awlpike,itm_tab_shield_heater_c,itm_bascinet,itm_mail_mittens,itm_mail_with_surcoat,itm_mail_chausses],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["swadian_man_at_arms_multiplayer_coop_tier_3","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_heavy_lance,itm_bastard_sword_b,itm_tab_shield_heater_cav_a,itm_flat_topped_helmet,itm_mail_mittens,itm_mail_with_surcoat,itm_mail_chausses,itm_warhorse],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_archer_multiplayer_coop_tier_3","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_barbed_arrows,itm_scimitar_b,itm_strong_bow,itm_leather_jerkin,itm_splinted_leather_greaves,itm_vaegir_spiked_helmet,itm_leather_gloves],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_spearman_multiplayer_coop_tier_3","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_scimitar_b, itm_tab_shield_kite_b,itm_javelin,itm_lamellar_armor,itm_splinted_leather_greaves,itm_vaegir_lamellar_helmet,itm_leather_gloves],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_horseman_multiplayer_coop_tier_3","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_heavy_lance,itm_tab_shield_kite_cav_b, itm_javelin,itm_lamellar_armor,itm_splinted_leather_greaves,itm_vaegir_lamellar_helmet,itm_hunter,itm_mail_mittens],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_veteran_horse_archer_multiplayer_coop_tier_3","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_strong_bow,itm_khergit_arrows,itm_tribal_warrior_outfit,itm_leather_steppe_cap_c,itm_khergit_leather_boots,itm_steppe_horse],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_infantry_multiplayer_coop_tier_3","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_hafted_blade_a,itm_javelin,itm_leather_steppe_cap_c,itm_lamellar_armor,itm_splinted_leather_greaves,itm_mail_mittens],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_lancer_multiplayer_coop_tier_3","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_heavy_lance,itm_tab_shield_small_round_a,itm_lamellar_armor,itm_leather_steppe_cap_c,itm_splinted_leather_greaves,itm_courser],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_archer_multiplayer_coop_tier_3","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_barbed_arrows,itm_sword_viking_3,itm_long_bow,itm_leather_jerkin,itm_leather_boots,itm_nordic_veteran_archer_helmet,itm_leather_gloves],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_veteran_multiplayer_coop_tier_3","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_one_handed_war_axe_b,itm_tab_shield_round_d,itm_heavy_throwing_axes,itm_mail_shirt,itm_splinted_leather_greaves,itm_nordic_huscarl_helmet],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_scout_multiplayer_coop_tier_3","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_throwing_spears,itm_heavy_lance,itm_tab_shield_small_round_b,itm_mail_shirt,itm_splinted_leather_greaves,itm_nordic_fighter_helmet,itm_saddle_horse],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_veteran_crossbowman_multiplayer_coop_tier_3","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sniper_crossbow,itm_steel_bolts,itm_military_cleaver_c,itm_tab_shield_pavise_c,itm_padded_cloth,itm_leather_boots,itm_footman_helmet,itm_leather_gloves],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_sergeant_multiplayer_coop_tier_3","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_tab_shield_pavise_c,itm_military_cleaver_c,itm_javelin,itm_ragged_outfit,itm_splinted_greaves,itm_kettle_hat,itm_mail_mittens],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_horseman_multiplayer_coop_tier_3","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_javelin,itm_tab_shield_heater_cav_b, itm_heavy_lance, itm_ragged_outfit,itm_splinted_greaves,itm_bascinet_2,itm_mail_mittens,itm_saddle_horse],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_archer_multiplayer_coop_tier_3","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_khergit_arrows,itm_sarranid_mace_1,itm_nomad_bow,itm_archers_vest,itm_sarranid_mail_coif,itm_leather_gloves,itm_sarranid_boots_c],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_footman_multiplayer_coop_tier_3","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_jarid, itm_tab_shield_kite_c, itm_sarranid_axe_b,itm_sarranid_mail_shirt,itm_sarranid_mail_coif,itm_mail_mittens,itm_sarranid_boots_c],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_mamluke_multiplayer_coop_tier_3","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_heavy_lance,itm_tab_shield_small_round_b,itm_jarid,itm_sarranid_cavalry_robe,itm_sarranid_horseman_helmet,itm_mail_mittens,itm_sarranid_boots_c,itm_arabian_horse_a],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],

  ["swadian_crossbowman_multiplayer_coop_tier_4","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_b,itm_sniper_crossbow,itm_steel_bolts,itm_tab_shield_heater_c,itm_helmet_with_neckguard,itm_leather_gloves,itm_haubergeon,itm_mail_chausses],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["swadian_infantry_multiplayer_coop_tier_4","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bastard_sword_b,itm_awlpike_long,itm_tab_shield_heater_d,itm_guard_helmet,itm_gauntlets,itm_coat_of_plates,itm_iron_greaves],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["swadian_man_at_arms_multiplayer_coop_tier_4","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_great_lance,itm_morningstar,itm_tab_shield_heater_cav_b,itm_great_helmet,itm_gauntlets,itm_coat_of_plates_red,itm_plate_boots,itm_warhorse],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_archer_multiplayer_coop_tier_4","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_barbed_arrows,itm_bardiche,itm_war_bow,itm_lamellar_vest,itm_splinted_leather_greaves,itm_vaegir_lamellar_helmet,itm_leather_gloves],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_spearman_multiplayer_coop_tier_4","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_bardiche,itm_javelin,itm_vaegir_elite_armor,itm_splinted_greaves,itm_vaegir_war_helmet,itm_mail_mittens],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_horseman_multiplayer_coop_tier_4","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_heavy_lance,itm_tab_shield_kite_cav_b,itm_javelin,itm_vaegir_elite_armor,itm_splinted_greaves,itm_hunter,itm_vaegir_war_helmet,itm_scale_gauntlets],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_veteran_horse_archer_multiplayer_coop_tier_4","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_hafted_blade_b,itm_strong_bow,itm_khergit_arrows,itm_lamellar_vest_khergit,itm_khergit_guard_helmet,itm_splinted_leather_greaves,itm_steppe_horse],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_infantry_multiplayer_coop_tier_4","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_hafted_blade_b,itm_tab_shield_small_round_a,itm_jarid,itm_khergit_elite_armor,itm_khergit_guard_boots,itm_khergit_war_helmet,itm_lamellar_gauntlets],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_lancer_multiplayer_coop_tier_4","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_great_lance,itm_tab_shield_small_round_c,itm_khergit_elite_armor,itm_khergit_war_helmet,itm_khergit_guard_boots,itm_lamellar_gauntlets,itm_courser],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_archer_multiplayer_coop_tier_4","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_khergit_arrows,itm_sword_viking_3,itm_long_bow,itm_byrnie,itm_splinted_leather_greaves,itm_nordic_footman_helmet,itm_leather_gloves],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_veteran_multiplayer_coop_tier_4","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_great_axe,itm_tab_shield_round_e,itm_heavy_throwing_axes,itm_banded_armor,itm_mail_boots,itm_nordic_warlord_helmet],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_scout_multiplayer_coop_tier_4","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_throwing_spears,itm_great_lance,itm_tab_shield_small_round_c,itm_mail_hauberk,itm_splinted_leather_greaves,itm_nordic_huscarl_helmet,itm_saddle_horse],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_veteran_crossbowman_multiplayer_coop_tier_4","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sniper_crossbow,itm_steel_bolts,itm_sledgehammer,itm_tab_shield_pavise_d,itm_mail_with_tunic_green,itm_kettle_hat,itm_splinted_greaves,itm_leather_gloves],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_sergeant_multiplayer_coop_tier_4","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_two_handed_cleaver,itm_tab_shield_pavise_d,itm_javelin,itm_surcoat_over_mail,itm_iron_greaves,itm_gauntlets,itm_full_helm,],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_horseman_multiplayer_coop_tier_4","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_javelin,itm_tab_shield_heater_cav_b, itm_great_lance, itm_surcoat_over_mail,itm_iron_greaves,itm_gauntlets,itm_full_helm,itm_saddle_horse],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_archer_multiplayer_coop_tier_4","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_khergit_arrows,itm_sarranid_two_handed_mace_1,itm_strong_bow,itm_sarranid_mail_shirt,itm_sarranid_mail_coif,itm_leather_gloves,itm_sarranid_boots_d],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_footman_multiplayer_coop_tier_4","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_bamboo_spear, itm_tab_shield_kite_c, itm_arabian_sword_a,itm_sarranid_elite_armor,itm_sarranid_veiled_helmet,itm_scale_gauntlets, itm_sarranid_boots_d],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_mamluke_multiplayer_coop_tier_4","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arabian_sword_a,itm_lance,itm_tab_shield_small_round_c,itm_mamluke_mail,itm_sarranid_veiled_helmet,itm_scale_gauntlets, itm_sarranid_boots_d,itm_arabian_horse_a],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],

   ["coop_faction_troop_templates_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   #tier 1
  ["npc1_1","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_armor,itm_nomad_boots,itm_knife, itm_courser],
   str_16|agi_17|int_6|cha_30|level(25),wpex(250,80,140,160,90,250),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_ironflesh_1|knows_power_strike_7|knows_pathfinding_3|knows_athletics_5|knows_tracking_1|knows_riding_6|knows_power_throw_7|knows_power_draw_5, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2_1","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_linen_tunic,itm_hide_boots,itm_club, itm_saddle_horse],
   str_14|agi_17|int_6|cha_30|level(25),wpex(240,130,170,150,170,90),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_5|knows_first_aid_1|knows_leadership_1|knows_riding_4|knows_power_strike_7|knows_power_draw_3|knows_power_throw_3,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3_1","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_dress,itm_woolen_hose,itm_knife, itm_hunter],
   str_24|agi_13|int_6|cha_30|level(25),wpex(190,80,240,180,180,80),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_6|knows_riding_8|knows_power_strike_5|knows_power_draw_3|knows_power_throw_3,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4_1","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_jerkin,itm_nomad_boots, itm_sword_medieval_a, itm_hunter],
   str_20|agi_13|int_6|cha_30|level(25),wpex(210,230,200,90,100,95),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_2|knows_power_strike_9|knows_riding_8|knows_athletics_7|knows_power_throw_3|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2|knows_power_draw_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5_1","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_vest,itm_nomad_boots, itm_sword_khergit_1, itm_steppe_horse],
   str_18|agi_13|int_6|cha_30|level(25),wpex(160,80,130,250,50,230),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_riding_7|knows_horse_archery_9|knows_power_draw_8|knows_leadership_2|knows_weapon_master_1|knows_power_strike_5|knows_power_throw_8|knows_athletics_5,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6_1","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_nomad_boots, itm_sword_medieval_a, itm_sumpter_horse],
   str_20|agi_19|int_6|cha_30|level(25),wpex(240,210,180,90,100,80),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_riding_7|knows_weapon_master_2|knows_athletics_8|knows_trainer_1|knows_leadership_1|knows_power_strike_7|knows_power_draw_2|knows_power_throw_3,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7_1","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_ragged_outfit,itm_wrapping_boots, itm_hunting_bow, itm_arrows, itm_staff, itm_arabian_horse_b],
   str_16|agi_13|int_6|cha_30|level(25),wpex(90,80,230,280,110,130),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_tracking_2|knows_athletics_8|knows_spotting_1|knows_pathfinding_1|knows_power_draw_10|knows_riding_4|knows_power_strike_6|knows_power_throw_5,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8_1","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tribal_warrior_outfit,itm_nomad_boots, itm_sword_viking_1, itm_courser],
   str_18|agi_15|int_6|cha_30|level(25),wpex(190,250,80,120,80,250),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_3|knows_athletics_10|knows_leadership_3|knows_tactics_1|knows_riding_4|knows_power_strike_10|knows_power_draw_2|knows_power_throw_8,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9_1","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_nomad_boots, itm_sword_medieval_b_small, itm_courser],
   str_22|agi_19|int_6|cha_30|level(25),wpex(80,230,130,220,70,160),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_1|knows_riding_4|knows_athletics_6|knows_leadership_1|knows_tactics_1|knows_power_strike_4|knows_power_draw_7|knows_power_throw_5,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10_1","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_padded_leather,itm_nomad_boots, itm_crossbow, itm_bolts, itm_pickaxe, itm_saddle_horse],
   str_24|agi_19|int_6|cha_30|level(25),wpex(170,80,80,160,290,150),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2|knows_riding_4|knows_power_strike_5|knows_power_draw_5|knows_power_throw_5|knows_athletics_7,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11_1","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_apron, itm_falchion, itm_wrapping_boots, itm_sumpter_horse],
   str_16|agi_17|int_6|cha_30|level(25),wpex(140,230,130,80,210,170),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5|knows_riding_4|knows_power_strike_5|knows_power_draw_2|knows_power_throw_7|knows_athletics_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12_1","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_pilgrim_disguise,itm_nomad_boots, itm_staff, itm_sumpter_horse],
   str_16|agi_17|int_6|cha_30|level(25),wpex(120,110,290,80,110,120),   knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_ironflesh_1|knows_power_strike_7|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3|knows_riding_4|knows_power_draw_2|knows_power_throw_3|knows_athletics_7,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13_1","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_robe,itm_nomad_boots, itm_scimitar, itm_courser],
   str_14|agi_17|int_6|cha_30|level(25),wpex(250,80,140,210,110,140),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_riding_9|knows_leadership_2|knows_athletics_5|knows_ironflesh_2|knows_power_strike_6|knows_weapon_master_1|knows_power_draw_7|knows_power_throw_4,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14_1","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nobleman_outfit,itm_nomad_boots, itm_sword_medieval_b_small, itm_courser],
   str_18|agi_19|int_6|cha_30|level(25),wpex(280,170,170,170,170,180),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1|knows_riding_7|knows_power_strike_7|knows_power_draw_6|knows_power_throw_6|knows_athletics_8,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15_1","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_rich_outfit,itm_nomad_boots, itm_sword_medieval_b_small, itm_hunter],
   str_18|agi_13|int_6|cha_30|level(25),wpex(190,290,130,210,90,90),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1|knows_riding_6|knows_power_strike_7|knows_power_draw_7|knows_power_throw_3|knows_athletics_5,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16_1","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_peasant_dress,itm_nomad_boots, itm_dagger, itm_throwing_knives, itm_saddle_horse],
   str_14|agi_17|int_6|cha_30|level(25),wpex(260,10,100,160,30,300),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_power_throw_10|knows_athletics_10|knows_power_strike_8|knows_riding_4|knows_power_draw_5,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],
   
    #tier 2
  ["npc1_2","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_leather_steppe_cap_c,itm_leather_gloves,itm_nomad_robe,itm_hide_boots,itm_sword_medieval_b_small, itm_courser],
   str_16|agi_17|int_12|cha_7|level(14),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2_2","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_nasal_helmet,itm_padded_leather,itm_leather_boots,itm_mace_2,itm_tab_shield_small_round_a, itm_saddle_horse],
   str_14|agi_17|int_11|cha_6|level(14),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3_2","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_head_wrappings,itm_leather_jerkin,itm_wrapping_boots,itm_sword_medieval_b_small, itm_hunter],
   str_24|agi_13|int_11|cha_6|level(14),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4_2","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_kettle_hat,itm_leather_gloves,itm_studded_leather_coat,itm_leather_boots,itm_sword_medieval_c,itm_tab_shield_heater_c, itm_hunter],
   str_20|agi_13|int_13|cha_10|level(27),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5_2","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_khergit_2, itm_tab_shield_small_round_b, itm_leather_steppe_cap_b, itm_tribal_warrior_outfit, itm_khergit_leather_boots, itm_steppe_horse],
   str_18|agi_13|int_12|cha_7|level(23),wp(90),knows_warrior_npc|
   knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6_2","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_bastard_sword_a, itm_mail_coif, itm_mail_with_tunic_red, itm_ankle_boots, itm_sumpter_horse],
   str_20|agi_19|int_10|cha_5|level(25),wp(105),knows_warrior_npc|
   knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7_2","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_voulge, itm_short_bow, itm_barbed_arrows, itm_nordic_fighter_helmet, itm_leather_gloves, itm_studded_leather_coat, itm_leather_boots, itm_arabian_horse_b],
   str_16|agi_13|int_10|cha_6|level(17),wp(80),knows_tracker_npc|
   knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8_2","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_viking_2, itm_nordic_helmet, itm_byrnie, itm_leather_boots, itm_courser],
   str_18|agi_15|int_9|cha_10|level(26),wp(90),knows_warrior_npc|
   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9_2","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_c, itm_vaegir_fur_cap, itm_leather_vest, itm_nomad_boots, itm_courser],
   str_22|agi_19|int_7|cha_8|level(17),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10_2","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_military_sickle_a, itm_heavy_crossbow, itm_bolts, itm_mail_coif, itm_leather_gloves, itm_aketon_green, itm_leather_boots, itm_saddle_horse],
   str_24|agi_19|int_9|cha_11|level(27),wp(105),knows_warrior_npc|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11_2","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sarranid_axe_a, itm_arming_cap, itm_leather_gloves, itm_padded_cloth, itm_ankle_boots, itm_sumpter_horse],
   str_16|agi_17|int_10|cha_10|level(26),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12_2","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_staff, itm_padded_coif, itm_leather_gloves, itm_pilgrim_disguise, itm_leather_boots, itm_sumpter_horse],
   str_16|agi_17|int_13|cha_7|level(20),wp(30),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13_2","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar, itm_tab_shield_small_round_b, itm_sarranid_warrior_cap, itm_sarranid_leather_armor, itm_sarranid_boots_b, itm_courser],
   str_14|agi_17|int_12|cha_8|level(19),wp(80),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14_2","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_b, itm_tab_shield_heater_c, itm_mail_coif, itm_studded_leather_coat, itm_leather_boots, itm_courser],
   str_18|agi_19|int_11|cha_8|level(23),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15_2","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_axe, itm_helmet_with_neckguard, itm_leather_gloves, itm_red_gambeson, itm_leather_boots, itm_hunter],
   str_18|agi_13|int_12|cha_8|level(25),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16_2","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_viking_2_small, itm_light_throwing_axes, itm_helmet_with_neckguard, itm_leather_gloves, itm_leather_jerkin, itm_ankle_boots, itm_saddle_horse],
   str_14|agi_17|int_8|cha_7|level(17),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],

  #tier 3
  ["npc1_3","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_war_helmet,itm_lamellar_gauntlets,itm_lamellar_vest_khergit,itm_khergit_leather_boots,itm_sword_medieval_c_small, itm_courser],
   str_16|agi_17|int_12|cha_7|level(14),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2_3","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_nordic_veteran_archer_helmet,itm_leather_gloves,itm_byrnie,itm_leather_boots,itm_mace_3,itm_tab_shield_small_round_b, itm_saddle_horse],
   str_14|agi_17|int_11|cha_6|level(14),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3_3","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_skullcap,itm_leather_gloves,itm_mail_shirt,itm_wrapping_boots,itm_sword_medieval_c_small, itm_hunter],
   str_24|agi_13|int_11|cha_6|level(14),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4_3","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_bascinet_2,itm_leather_gloves,itm_surcoat_over_mail,itm_mail_chausses,itm_sword_medieval_c_long,itm_tab_shield_heater_c, itm_hunter],
   str_20|agi_13|int_13|cha_10|level(27),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5_3","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar, itm_tab_shield_small_round_c, itm_khergit_cavalry_helmet, itm_leather_gloves, itm_lamellar_vest, itm_khergit_leather_boots, itm_steppe_horse],
   str_18|agi_13|int_12|cha_7|level(23),wp(90),knows_warrior_npc|
   knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6_3","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_bastard_sword_b, itm_flat_topped_helmet, itm_mail_mittens, itm_haubergeon, itm_mail_chausses, itm_sumpter_horse],
   str_20|agi_19|int_10|cha_5|level(25),wp(105),knows_warrior_npc|
   knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7_3","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_bardiche, itm_strong_bow, itm_barbed_arrows, itm_nordic_helmet, itm_leather_gloves, itm_mail_hauberk, itm_splinted_leather_greaves, itm_arabian_horse_b],
   str_16|agi_13|int_10|cha_6|level(17),wp(80),knows_tracker_npc|
   knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8_3","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_battle_axe, itm_nordic_huscarl_helmet, itm_leather_gloves, itm_mail_hauberk, itm_mail_chausses, itm_courser],
   str_18|agi_15|int_9|cha_10|level(26),wp(90),knows_warrior_npc|
   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9_3","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_c_long, itm_vaegir_lamellar_helmet, itm_leather_gloves, itm_lamellar_vest, itm_leather_boots, itm_courser],
   str_22|agi_19|int_7|cha_8|level(17),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10_3","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_military_pick, itm_heavy_crossbow, itm_steel_bolts, itm_kettle_hat, itm_leather_gloves, itm_mail_with_tunic_green, itm_leather_boots, itm_saddle_horse],
   str_24|agi_19|int_9|cha_11|level(27),wp(105),knows_warrior_npc|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11_3","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sarranid_axe_b, itm_arming_cap, itm_leather_gloves, itm_mail_with_surcoat, itm_mail_chausses, itm_sumpter_horse],
   str_16|agi_17|int_10|cha_10|level(26),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12_3","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_staff, itm_mail_coif, itm_mail_mittens, itm_pilgrim_disguise, itm_mail_chausses, itm_sumpter_horse],
   str_16|agi_17|int_13|cha_7|level(20),wp(30),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13_3","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar, itm_tab_shield_small_round_c, itm_sarranid_mail_coif, itm_arabian_armor_b, itm_sarranid_boots_c, itm_courser],
   str_14|agi_17|int_12|cha_8|level(19),wp(80),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14_3","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_c, itm_tab_shield_heater_c, itm_bascinet_2, itm_leather_gloves, itm_surcoat_over_mail, itm_mail_chausses, itm_courser],
   str_18|agi_19|int_11|cha_8|level(23),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15_3","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_axe_b, itm_guard_helmet, itm_mail_mittens, itm_haubergeon, itm_mail_chausses, itm_hunter],
   str_18|agi_13|int_12|cha_8|level(25),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16_3","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_viking_2_small, itm_throwing_axes, itm_vaegir_fur_helmet, itm_leather_gloves, itm_lamellar_vest, itm_leather_boots, itm_saddle_horse],
   str_14|agi_17|int_8|cha_7|level(17),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],

   #tier 4
  ["npc1_4","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_guard_helmet,itm_lamellar_gauntlets,itm_khergit_guard_armor,itm_khergit_guard_boots,itm_sword_viking_3_small, itm_courser],
   str_16|agi_17|int_12|cha_7|level(14),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2_4","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_nordic_helmet,itm_mail_mittens,itm_mail_hauberk,itm_mail_chausses,itm_mace_4,itm_tab_shield_small_round_c, itm_saddle_horse],
   str_14|agi_17|int_11|cha_6|level(14),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3_4","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_guard_helmet,itm_gauntlets,itm_plate_armor,itm_plate_boots,itm_sword_viking_3_small, itm_hunter],
   str_24|agi_13|int_11|cha_6|level(14),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4_4","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_full_helm,itm_scale_gauntlets,itm_heraldic_mail_with_tabard,itm_iron_greaves,itm_sword_medieval_d_long,itm_tab_shield_heater_d, itm_hunter],
   str_20|agi_13|int_13|cha_10|level(27),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5_4","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar_b, itm_tab_shield_small_round_c, itm_khergit_guard_helmet, itm_scale_gauntlets, itm_lamellar_armor, itm_iron_greaves, itm_steppe_horse],
   str_18|agi_13|int_12|cha_7|level(23),wp(90),knows_warrior_npc|
   knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6_4","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_two_handed_b, itm_bascinet, itm_gauntlets, itm_cuir_bouilli, itm_plate_boots, itm_sumpter_horse],
   str_20|agi_19|int_10|cha_5|level(25),wp(105),knows_warrior_npc|
   knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7_4","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_great_long_bardiche, itm_war_bow, itm_khergit_arrows, itm_nordic_huscarl_helmet, itm_scale_gauntlets, itm_heraldic_mail_with_tabard, itm_iron_greaves, itm_arabian_horse_b],
   str_16|agi_13|int_10|cha_6|level(17),wp(80),knows_tracker_npc|
   knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8_4","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_great_axe, itm_nordic_warlord_helmet, itm_mail_mittens, itm_banded_armor, itm_mail_chausses, itm_courser],
   str_18|agi_15|int_9|cha_10|level(26),wp(90),knows_warrior_npc|
   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9_4","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_bastard_sword_b, itm_vaegir_war_helmet, itm_lamellar_gauntlets, itm_banded_armor, itm_iron_greaves, itm_courser],
   str_22|agi_19|int_7|cha_8|level(17),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10_4","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_military_pick, itm_sniper_crossbow, itm_steel_bolts, itm_full_helm, itm_mail_mittens, itm_surcoat_over_mail, itm_splinted_leather_greaves, itm_saddle_horse],
   str_24|agi_19|int_9|cha_11|level(27),wp(105),knows_warrior_npc|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11_4","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sarranid_two_handed_axe_a, itm_great_helmet, itm_gauntlets, itm_brigandine_red, itm_plate_boots, itm_sumpter_horse],
   str_16|agi_17|int_10|cha_10|level(26),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12_4","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_staff, itm_kettle_hat, itm_gauntlets, itm_surcoat_over_mail, itm_plate_boots, itm_sumpter_horse],
   str_16|agi_17|int_13|cha_7|level(20),wp(30),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13_4","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar_b, itm_tab_shield_small_round_c, itm_sarranid_veiled_helmet, itm_scale_gauntlets, itm_mamluke_mail, itm_sarranid_boots_d, itm_courser],
   str_14|agi_17|int_12|cha_8|level(19),wp(80),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14_4","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_d_long, itm_tab_shield_heater_d, itm_great_helmet, itm_gauntlets, itm_heraldic_mail_with_surcoat, itm_plate_boots, itm_courser],
   str_18|agi_19|int_11|cha_8|level(23),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15_4","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_axe_c, itm_full_helm, itm_scale_gauntlets, itm_heraldic_mail_with_surcoat, itm_iron_greaves, itm_hunter],
   str_18|agi_13|int_12|cha_8|level(25),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16_4","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_viking_3_small, itm_heavy_throwing_axes, itm_vaegir_lamellar_helmet, itm_lamellar_gauntlets, itm_lamellar_armor, itm_khergit_guard_boots, itm_saddle_horse],
   str_14|agi_17|int_8|cha_7|level(17),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],

   ["coop_companion_equipment_ui_0","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["coop_companion_equipment_ui_0_f","{!}multiplayer_end","{!}multiplayer_end", tf_female, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["coop_companion_equipment_ui_1","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["coop_companion_equipment_ui_1_f","{!}multiplayer_end","{!}multiplayer_end", tf_female, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["coop_companion_equipment_sets_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

   ["kingdom_neutral_lord",  "King Neutral",  "Neutral",  tf_hero, 0,reserved,  fac_neutrals,[ itm_saddle_horse,  itm_nord_nobleman_outfit,    itm_leather_boots,              itm_iron_greaves,                 itm_french_plate,   itm_hourglass_gauntlets_b,    itm_french_longsword,   itm_heavy_lance,        itm_tab_shield_heater_cav_b,    itm_visored_sallet_coif],            knight_attrib_5,wp(360),knight_skills_5, 0x0000000189080005549c575aea691962000000000011dd270000000000000000, nord_face_older_2],


  ["player_temp_recruit","Player Temp Recruit","Player Temp ",tf_hero|tf_randomize_face, 0, reserved,  fac_commoners,
   [itm_club,itm_spiked_club,itm_cleaver,itm_tab_shield_round_a,
	itm_felt_hat,itm_straw_hat,itm_shirt,itm_linen_shirt_a,itm_wrapping_boots,itm_hide_boots],
   str_7 | agi_5 | int_4 | cha_4|level(4),wp(60),knows_common|knows_inventory_management_10, man_face_old_1, man_face_older_2],
  
  ["player_temp_footman","Player Temp Footman","Player Temp ",tf_hero|tf_randomize_face, 0, reserved,  fac_commoners,
   [itm_sword_medieval_a,itm_spiked_club,itm_one_handed_war_axe_a,itm_shortened_spear,itm_spear,itm_tab_shield_round_b,
    itm_nordic_archer_helmet,itm_leather_warrior_cap,itm_leather_jerkin,itm_red_gambeson,itm_nomad_boots,itm_leather_boots,itm_leather_gloves,itm_black_leather_gloves],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(80)|wp_two_handed(80)|wp_polearm(80)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_2|knows_ironflesh_1|knows_shield_1|knows_athletics_1|knows_power_throw_2,swadian_face_younger_1, swadian_face_middle_2],
   
  ["player_temp_trained_footman","Player Temp Trained Footman","Player Temp ",tf_hero|tf_randomize_face, 0, reserved,  fac_commoners,
   [itm_one_handed_war_axe_b,itm_sword_medieval_b,itm_sword_medieval_c,itm_fighting_pick,itm_war_spear,itm_spear,itm_long_hafted_knobbed_mace,itm_javelin,itm_tab_shield_round_c,itm_tab_shield_round_b,
	itm_helmet_with_neckguard,itm_segmented_helmet,itm_mail_shirt_with_fur,itm_byrnie,itm_nomad_boots,itm_leather_boots,itm_leather_gloves],
   str_12 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(110)|wp_two_handed(110)|wp_polearm(110)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_4|knows_ironflesh_2|knows_shield_2|knows_athletics_3|knows_power_throw_2,swadian_face_younger_1, swadian_face_middle_2],
   
  ["player_temp_infantry","Player Temp Infantry","Player Temp ",tf_hero|tf_randomize_face, 0, reserved,  fac_commoners,
   [itm_one_handed_battle_axe_b,itm_steel_pick,itm_military_hammer,itm_bardiche,itm_war_spear,itm_long_bardiche,itm_longsword_b,itm_long_hafted_spiked_mace,itm_ashwood_pike,itm_tab_shield_round_c,itm_tab_shield_round_d,itm_javelin,itm_throwing_spears,
	itm_guard_helmet,itm_bascinet_3,itm_heraldic_mail_with_surcoat,itm_heraldic_mail_with_tabard,itm_mail_chausses,itm_mail_mittens,itm_hourglass_gloves,itm_gilded_hourglass_gloves],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5|knows_power_throw_3,swadian_face_younger_1, swadian_face_middle_2],
  
  ["player_temp_elite_footman","Player Temp Elite Footman","Player Temp ",tf_hero|tf_randomize_face, 0, reserved,  fac_commoners,
   [itm_one_handed_battle_axe_b,itm_steel_pick,itm_military_hammer,itm_bardiche,itm_war_spear,itm_long_bardiche,itm_longsword_b,itm_long_hafted_spiked_mace,itm_ashwood_pike,itm_tab_shield_round_c,itm_tab_shield_round_d,itm_javelin,itm_throwing_spears,
	itm_guard_helmet,itm_bascinet_3,itm_heraldic_mail_with_surcoat,itm_heraldic_mail_with_tabard,itm_mail_chausses,itm_mail_mittens,itm_hourglass_gloves,itm_gilded_hourglass_gloves],
   str_15 | agi_12 | int_4 | cha_4|level(20),wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_6|knows_ironflesh_3|knows_shield_4|knows_athletics_5|knows_power_throw_4,swadian_face_younger_1, swadian_face_middle_2],
  
  ["player_temp_sergeant","Player Temp Sergeant","Player Temp ",tf_hero|tf_randomize_face, 0, reserved,  fac_commoners,
   [itm_one_handed_warhammer,itm_one_handed_battle_axe_c,itm_steel_pick,itm_sword_two_handed_a,itm_great_bardiche,itm_warhammer,itm_great_long_bardiche,itm_ashwood_pike,itm_tab_shield_round_d,itm_tab_shield_round_e,itm_throwing_spears,
	itm_great_helmet_f,itm_great_helmet_g,itm_gotland_helmet_b,itm_great_helmet_h,itm_great_helmet_i,itm_transitional_blue,itm_churburg_a,itm_transitional_heraldic,itm_steel_greaves_a,itm_iron_greaves,itm_gilded_hourglass_gloves,itm_hourglass_gloves,itm_hourglass_gauntlets_a,itm_hourglass_gauntlets_b],
   str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_8|knows_ironflesh_5|knows_shield_5|knows_athletics_7|knows_power_throw_5,swadian_face_younger_1, swadian_face_middle_2],
  
  ["player_temp_skirmisher","Player Temp Skirmisher","Player Temp ",tf_hero|tf_randomize_face, 0, reserved,  fac_commoners,
   [itm_fighting_pick,itm_one_handed_war_axe_a,itm_hunting_bow,itm_arrows,itm_short_bow,itm_barbed_arrows,
   	itm_nordic_archer_helmet,itm_leather_warrior_cap,itm_leather_jerkin,itm_red_gambeson,itm_nomad_boots,itm_leather_boots,itm_leather_gloves,itm_black_leather_gloves],
   str_9 | agi_7 | int_4 | cha_4|level(9),wp_one_handed(65)|wp_two_handed(20)|wp_polearm(50)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100),knows_common|knows_power_strike_1|knows_ironflesh_1|knows_athletics_3|knows_power_draw_1,swadian_face_younger_1, swadian_face_middle_2],
  
  ["player_temp_archer","Player Temp Archer","Player Temp Archers",tf_hero|tf_randomize_face, 0, reserved,  fac_commoners,
   [itm_one_handed_war_axe_b,itm_sword_medieval_a,itm_long_bow,itm_barbed_arrows,itm_short_bow,itm_bodkin_arrows,
    itm_nordic_archer_helmet,itm_leather_warrior_cap,itm_leather_jerkin,itm_red_gambeson,itm_nomad_boots,itm_leather_boots,itm_leather_gloves,itm_black_leather_gloves],
   str_11 | agi_9 | int_4 | cha_4|level(14),wp_one_handed(70)|wp_two_handed(30)|wp_polearm(60)|wp_archery(115)|wp_crossbow(115)|wp_throwing(115),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_5|knows_power_draw_3,swadian_face_younger_1, swadian_face_middle_2],
  
  ["player_temp_master_archer","Player Temp Master Archer","Player Temp ",tf_hero|tf_randomize_face, 0, reserved,  fac_commoners,
   [itm_one_handed_war_axe_b,itm_military_hammer,itm_long_bow,itm_barbed_arrows,itm_bodkin_arrows,
	itm_helmet_with_neckguard,itm_segmented_helmet,itm_mail_shirt_with_fur,itm_byrnie,itm_nomad_boots,itm_leather_boots,itm_leather_gloves],
   str_13 | agi_12 | int_4 | cha_4|level(19),wp_one_handed(80)|wp_two_handed(40)|wp_polearm(70)|wp_archery(140)|wp_crossbow(140)|wp_throwing(140),knows_common|knows_power_strike_2|knows_ironflesh_3|knows_athletics_6|knows_power_draw_4,swadian_face_younger_1, swadian_face_middle_2],
  
  ["player_temp_horseman","Player Temp Horseman","Player Temp ",tf_hero|tf_randomize_face, 0, reserved,  fac_commoners,
   [itm_sword_medieval_a,itm_sword_medieval_b,itm_light_lance,itm_lance,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_javelin,
	itm_helmet_with_neckguard,itm_segmented_helmet,itm_mail_shirt_with_fur,itm_byrnie,itm_nomad_boots,itm_leather_boots,itm_leather_gloves,itm_saddle_horse,itm_courser],
   str_12 | agi_9 | int_4 | cha_4|level(17),wp_one_handed(120)|wp_two_handed(120)|wp_polearm(120)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_3|knows_ironflesh_3|knows_shield_2|knows_athletics_3|knows_riding_3,swadian_face_younger_1, swadian_face_middle_2],
  
  ["player_temp_nobleman","Player Temp Nobleman","Player Temp ",tf_hero|tf_randomize_face, 0, reserved,  fac_commoners,
   [itm_one_handed_battle_axe_b,itm_steel_pick,itm_military_hammer,itm_bardiche,itm_longsword_b,itm_lance,itm_heavy_lance,itm_tab_shield_round_c,itm_tab_shield_small_round_b,
	itm_guard_helmet,itm_bascinet_3,itm_heraldic_mail_with_surcoat,itm_heraldic_mail_with_tabard,itm_mail_chausses,itm_mail_mittens,itm_hourglass_gloves,itm_gilded_hourglass_gloves,itm_courser,itm_hunter],
   str_15 | agi_12 | int_4 | cha_4|level(21),wp_one_handed(150)|wp_two_handed(150)|wp_polearm(150)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_5|knows_ironflesh_4|knows_shield_4|knows_athletics_5|knows_riding_5,swadian_face_younger_1, swadian_face_middle_2],
  
  ["player_temp_knight","Player Temp Knight","Player Temp ",tf_hero|tf_randomize_face, 0, reserved,  fac_commoners,
   [itm_one_handed_warhammer,itm_one_handed_battle_axe_c,itm_steel_pick,itm_sword_two_handed_a,itm_heavy_lance,itm_great_lance,itm_tab_shield_small_round_c,
	itm_great_helmet_f,itm_great_helmet_g,itm_gotland_helmet_b,itm_great_helmet_h,itm_great_helmet_i,itm_transitional_blue,itm_churburg_a,itm_transitional_heraldic,itm_steel_greaves_a,itm_iron_greaves,itm_gilded_hourglass_gloves,itm_hourglass_gloves,itm_hourglass_gauntlets_a,itm_hourglass_gauntlets_b,itm_warhorse,itm_warhorse_b],
    str_18 | agi_15 | int_4 | cha_4|level(25),wp_one_handed(180)|wp_two_handed(180)|wp_polearm(180)|wp_archery(10)|wp_crossbow(10)|wp_throwing(10),knows_common|knows_power_strike_7|knows_ironflesh_6|knows_shield_5|knows_athletics_6|knows_riding_7,swadian_face_younger_1, swadian_face_middle_2],
   
  ["player_temp_kingsguard","Player Temp Kings Guard","Player Temp Kings Guards",tf_hero|tf_randomize_face, 0, reserved,  fac_commoners,
   [itm_one_handed_battle_axe_b,itm_tab_shield_small_round_c,itm_great_helmet_f,itm_great_helmet_g,itm_gotland_helmet_b,itm_great_helmet_h,itm_great_helmet_i,itm_transitional_blue,itm_churburg_a,itm_transitional_heraldic,itm_steel_greaves_a,itm_iron_greaves,itm_gilded_hourglass_gloves,itm_hourglass_gloves,itm_hourglass_gauntlets_a,itm_hourglass_gauntlets_b,itm_warhorse,itm_warhorse_b],
   str_25|agi_18|int_10|cha_5|level(20),wp(200),knows_warrior_npc|knows_inventory_management_10, man_face_old_1, man_face_older_2],
  
  ["player_test_troop","Player Test Troop 1","Player Test Troop 1",tf_hero|tf_randomize_face, 0, reserved,  fac_commoners,
  [itm_padded_leather,itm_nomad_boots, itm_crossbow, itm_bolts, itm_pickaxe],
   def_attrib|level(1),wp(20),knows_warrior_npc|knows_inventory_management_10, man_face_old_1, man_face_older_2],
  
   
]


#Troop upgrade declarations

upgrade(troops,"farmer", "watchman")
upgrade(troops,"townsman","watchman")
upgrade2(troops,"watchman","caravan_guard","mercenary_crossbowman")
upgrade2(troops,"caravan_guard","mercenary_swordsman","mercenary_horseman")
upgrade(troops,"mercenary_swordsman","hired_blade")
upgrade2(troops,"mercenary_horseman","mercenary_cavalry","mercenary_horse_crossbowman")

upgrade(troops,"mercenary_horse_crossbowman","mercenary_veteran_horse_crossbowman")	
upgrade(troops,"mercenary_veteran_horse_crossbowman","mercenary_elite_horse_crossbowman")	

upgrade(troops,"mercenary_horse_thrower","mercenary_veteran_horse_thrower")	
upgrade(troops,"mercenary_veteran_horse_thrower","mercenary_elite_horse_thrower")	
 
### swadian mercenaries begin

upgrade2(troops,"swadian_militia_merc","swadian_footman_merc","swadian_skirmisher_merc")
upgrade2(troops,"swadian_footman_merc","swadian_infantry_merc","swadian_man_at_arms_merc")		

upgrade(troops,"swadian_skirmisher_merc","swadian_crossbowman_merc")		
upgrade(troops,"swadian_crossbowman_merc","swadian_sharpshooter_merc")		

upgrade(troops,"swadian_man_at_arms_merc","swadian_cavalryman_merc")		
upgrade(troops,"swadian_infantry_merc","swadian_sergeant_merc")		


### swadian mercenaries end
### vaegir mercenaries begin
upgrade2(troops,"vaegir_footman_merc","vaegir_skirmisher_merc","vaegir_veteran_merc")		
upgrade2(troops,"vaegir_veteran_merc","vaegir_infantry_merc","vaegir_horseman_merc")		
	
upgrade(troops,"vaegir_skirmisher_merc","vaegir_archer_merc")	
upgrade(troops,"vaegir_archer_merc","vaegir_marksman_merc")	

upgrade(troops,"vaegir_infantry_merc","vaegir_guard_merc")	

upgrade(troops,"vaegir_horseman_merc","vaegir_cavalryman_merc")	

### vaegir mercenaries end
### khergit mercenaries begin

upgrade2(troops,"khergit_skirmisher_merc","khergit_horseman_merc","khergit_horse_archer_merc")		
	
upgrade(troops,"khergit_horseman_merc","khergit_lancer_merc")	
upgrade(troops,"khergit_horse_archer_merc","khergit_veteran_horse_archer_merc")	
	
### khergit mercenaries end

### Nord mercenaries begin
upgrade2(troops,"nord_footman_merc","nord_trained_footman_merc","nord_huntsman_merc")		
	
upgrade(troops,"nord_trained_footman_merc","nord_warrior_merc")		
upgrade(troops,"nord_warrior_merc","nord_veteran_merc")		
upgrade(troops,"nord_veteran_merc","nord_champion_merc")		
	
upgrade(troops,"nord_huntsman_merc","nord_archer_merc")		
upgrade(troops,"nord_archer_merc","nord_veteran_archer_merc")		
	
### Nord mercenaries end
### Rhodok mercenaries begin
upgrade2(troops,"rhodok_spearman_merc","rhodok_trained_spearman_merc","rhodok_crossbowman_merc")		
	
upgrade(troops,"rhodok_trained_spearman_merc","rhodok_veteran_spearman_merc")	
upgrade(troops,"rhodok_veteran_spearman_merc","rhodok_sergeant_merc")	

upgrade(troops,"rhodok_crossbowman_merc","rhodok_trained_crossbowman_merc")	
upgrade(troops,"rhodok_trained_crossbowman_merc","rhodok_veteran_crossbowman_merc")	
upgrade(troops,"rhodok_veteran_crossbowman_merc","rhodok_sharpshooter_merc")	

### Rhodok mercenaries end
### Sarranid mercenaries begin

upgrade2(troops,"sarranid_footman_merc","sarranid_skirmisher_merc","sarranid_veteran_footman_merc")		
upgrade2(troops,"sarranid_veteran_footman_merc","sarranid_horseman_merc","sarranid_infantry_merc")		
	
upgrade(troops,"sarranid_skirmisher_merc","sarranid_archer_merc")		
upgrade(troops,"sarranid_archer_merc","sarranid_master_archer_merc")	
	
upgrade(troops,"sarranid_horseman_merc","sarranid_mamluke_merc")		
upgrade(troops,"sarranid_infantry_merc","sarranid_guard_merc")	

### Sarranid mercenaries end
upgrade(troops,"swadian_recruit","swadian_militia")
upgrade2(troops,"swadian_militia","swadian_footman","swadian_skirmisher")
upgrade2(troops,"swadian_footman","swadian_man_at_arms","swadian_infantry")
upgrade2(troops,"swadian_infantry","swadian_sergeant","swadian_pikeman")
upgrade(troops,"swadian_skirmisher","swadian_crossbowman")

upgrade(troops,"swadian_crossbowman","swadian_sharpshooter")

upgrade(troops,"swadian_man_at_arms","swadian_knight")
upgrade(troops,"swadian_knight","swadian_heavy_knight")

upgrade(troops,"vaegir_recruit","vaegir_footman")
upgrade2(troops,"vaegir_footman","vaegir_veteran","vaegir_skirmisher")

upgrade2(troops,"vaegir_skirmisher","vaegir_archer","vaegir_crossbowman")

upgrade(troops,"vaegir_archer","vaegir_marksman")

upgrade2(troops,"vaegir_veteran","vaegir_horseman","vaegir_infantry")

upgrade2(troops,"vaegir_infantry","vaegir_guard","vaegir_pikeman")
upgrade(troops,"vaegir_horseman","vaegir_knight")


upgrade2(troops,"khergit_tribesman","khergit_footman","khergit_skirmisher")
upgrade2(troops,"khergit_footman","khergit_warrior","khergit_horseman")
upgrade(troops,"khergit_skirmisher","khergit_archer")
upgrade(troops,"khergit_veteran_warrior","khergit_veteran_horse_archer")
upgrade(troops,"khergit_archer","khergit_veteran_archer")
upgrade(troops,"khergit_veteran_archer","khergit_horse_archer")
	
upgrade(troops,"khergit_warrior","khergit_veteran_warrior")
upgrade(troops,"khergit_horseman","khergit_lancer") 
upgrade(troops,"khergit_lancer","khergit_heavy_lancer")    
	
upgrade2(troops,"nord_recruit","nord_footman","nord_huntsman")
upgrade2(troops,"nord_footman","nord_trained_footman","nord_horseman")
upgrade2(troops,"nord_trained_footman","nord_warrior","nord_veteran")
upgrade(troops,"nord_veteran","nord_champion")
upgrade2(troops,"nord_huntsman","nord_archer","nord_crossboman")
upgrade(troops,"nord_archer","nord_veteran_archer")

upgrade(troops,"nord_horseman","nord_knight")



upgrade2(troops,"rhodok_tribesman","rhodok_spearman","rhodok_crossbowman")
upgrade(troops,"rhodok_spearman","rhodok_trained_spearman")
upgrade2(troops,"rhodok_trained_spearman","rhodok_veteran_spearman","rhodok_horseman")
upgrade(troops,"rhodok_veteran_spearman","rhodok_sergeant")

upgrade(troops,"rhodok_horseman","rhodok_veteran_horseman")
upgrade(troops,"rhodok_veteran_horseman","rhodok_knight")


upgrade(troops,"rhodok_crossbowman","rhodok_trained_crossbowman")
upgrade(troops,"rhodok_trained_crossbowman","rhodok_veteran_crossbowman") #new 1.126
upgrade(troops,"rhodok_veteran_crossbowman","rhodok_sharpshooter")




upgrade2(troops,"sarranid_recruit","sarranid_footman","sarranid_skirmisher")

upgrade2(troops,"sarranid_footman","sarranid_veteran_footman","sarranid_horseman")
upgrade(troops,"sarranid_veteran_footman","sarranid_infantry")
upgrade(troops,"sarranid_infantry","sarranid_guard")
upgrade(troops,"sarranid_skirmisher","sarranid_archer")

upgrade(troops,"sarranid_archer","sarranid_master_archer")

upgrade(troops,"sarranid_horseman","sarranid_mamluke")
upgrade(troops,"sarranid_mamluke","sarranid_man_at_arms")
upgrade(troops,"sarranid_man_at_arms","sarranid_knight")


upgrade2(troops,"eques_tribesman","eques_spearman","eques_crossbowman")
upgrade(troops,"eques_spearman","eques_trained_spearman")
upgrade2(troops,"eques_trained_spearman","eques_veteran_spearman","eques_horseman")
upgrade(troops,"eques_veteran_spearman","eques_sergeant")

upgrade(troops,"eques_horseman","eques_veteran_horseman")
upgrade(troops,"eques_veteran_horseman","eques_knight")


upgrade(troops,"eques_crossbowman","eques_trained_crossbowman")
upgrade2(troops,"eques_trained_crossbowman","eques_veteran_crossbowman","eques_sharpshooter") #new 1.126


upgrade2(troops,"norse_recruit","norse_footman","norse_huntsman")
upgrade(troops,"norse_huntsman","norse_archer")			
upgrade(troops,"norse_archer","norse_veteran_archer")	
	
upgrade2(troops,"norse_footman","norse_trained_footman","norse_horseman")
upgrade(troops,"norse_horseman","norse_cavalryman")	
	
upgrade2(troops,"norse_trained_footman","norse_warrior","norse_axeman")	
upgrade(troops,"norse_warrior","norse_veteran_warrior")	
upgrade(troops,"norse_axeman","norse_vetera_axeman")	


upgrade2(troops,"order_recruit","order_footman","order_nobleman")
upgrade2(troops,"order_footman","order_trained_footman","order_crossbowman")		
upgrade2(troops,"order_trained_footman","order_veteran_footman","order_spearman")			
upgrade(troops,"order_veteran_footman","order_elite_footman")
upgrade(troops,"order_crossbowman","order_veteran_crossbowman")
upgrade(troops,"order_veteran_crossbowman","order_elite_crossbowman")
upgrade(troops,"order_nobleman","order_knight")
upgrade(troops,"order_knight","order_heavy_knight")
upgrade(troops,"sarranid_horseman","sarranid_mamluke")


upgrade2(troops,"looter","mountain_bandit", "forest_bandit")

#new tree connections
upgrade2(troops,"mountain_bandit","mountain_archer","mountain_warrior")
upgrade2(troops,"forest_bandit","forest_archer","forest_fighters")
upgrade2(troops,"steppe_bandit","steppe_bandit_archer","steppe_bandit_lancer")
#upgrade(troops,"taiga_bandit","vaegir_recruit")		# 21.09.2018

upgrade(troops,"sea_raider_light","sea_raider")
upgrade2(troops,"desert_bandit","desert_horse_archer","desert_horse_warrior")
#new tree connections ended

upgrade2(troops,"bandit","brigand","mercenary_swordsman")
upgrade(troops,"manhunter","slave_driver")

upgrade2(troops,"swamp_bandit","swamp_archer","swamp_warrior")

#upgrade(troops,"forest_bandit","mercenary_crossbowman")

upgrade(troops,"slave_driver","slave_hunter")
upgrade(troops,"slave_hunter","slave_crusher")
upgrade(troops,"slave_crusher","slaver_chief")

upgrade(troops,"follower_woman","hunter_woman")
upgrade(troops,"hunter_woman","fighter_woman")

upgrade(troops,"fighter_woman","sword_sister")
upgrade(troops,"refugee","follower_woman")
upgrade(troops,"peasant_woman","follower_woman")


#### Player troops upgrade 
#upgrade2(troops,"player_recruit","player_footman","player_skirmisher"),
upgrade3(troops,"player_recruit","player_footman","player_skirmisher","player_horseman"),
upgrade2(troops,"player_footman","player_trained_footman","player_horseman"),
upgrade2(troops,"player_trained_footman","player_infantry","player_elite_footman"),
upgrade(troops,"player_skirmisher","player_archer"),
upgrade(troops,"player_archer","player_master_archer"),
upgrade(troops,"player_infantry","player_sergeant"),
upgrade(troops,"player_horseman","player_nobleman"),
upgrade(troops,"player_nobleman","player_knight"),

