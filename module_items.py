from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn|imodbit_champion     ### +1,+2,+3 (spirited=, heavy= , champion=,                    1
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened                     ### +1,+2,+3 (sturdy=, thick= , hardened=,                      2 
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly     ### +1,+2,+3 (thick=, reinforced= , lordly=,                    3
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly   ### +1,+2,+3 (thick=, reinforced= , lordly=,    3
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_fine |imodbit_balanced | imodbit_masterwork             ### +1,+2,+3 (fine=, balanced= , masterwork=,                           4
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_heavy |imodbit_thick | imodbit_reinforced            ### +1,+2,+3 (heavy=35c, thick=36c , reinforced=37c,                    5
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork          ### +1,+2,+3 (Balanced=35c, tempered=36c , masterwork=37c,              6
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork     ### +1,+2,+3 (Heavy=38c ,Balanced=39c, masterwork=41c,                  7
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy |imodbit_balanced| imodbit_masterwork            ### +1,+2,+3 (fine=38c ,Balanced=39c, masterwork=41c,                    7  
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_fine|imodbit_heavy|imodbit_masterwork                 ### +1,+2,+3 (fine=33b ,Balanced=34b, masterwork=37b                         8
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_fine | imodbit_heavy|imodbit_masterwork               ### +1,+2,+3 (fine=32k ,Balanced=34p, masterwork=36k,                        8
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_fine |imodbit_strong|imodbit_masterwork                     ### +1,+2,+3 (fine= ,strong=, masterwork=,                              9
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_fine | imodbit_heavy|imodbit_masterwork                 ### +1,+2,+3 (heavy= ,strong=, masterwork=,                            10
imodbits_missile   = imodbit_bent | imodbit_large_bag|imodbit_fine|imodbit_heavy                                       ### +1,+2,+3 (large_bag= ,fine=, heavy=,                             11
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag |imodbit_masterwork              ### +1,+2,+3 (heavy= ,balanced=, masterwork=,                        12
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag|imodbit_masterwork                 ### +1,+2,+3 (large_bag= ,balanced=, masterwork=,                       13

itc_warclub = itc_cut_two_handed |  itcf_thrust_polearm | itc_parry_two_handed |itc_dagger
itc_greatsword = itc_cut_two_handed |  itcf_thrust_twohanded | itc_parry_two_handed |itcf_thrust_onehanded_lance
itc_flamberge =   itcf_thrust_polearm | itc_parry_two_handed | itcf_slashright_twohanded |itcf_slashleft_polearm   |itcf_overswing_polearm  

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent
# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive) 
items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
 ["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

 ["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar|itcf_carry_mace_left_hip, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(55)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile],
 ["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crossbow",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Kite Shield", [("shield_kite_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],
 ["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
 ["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

 ["tutorial_dagger","Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],


 ["horse_meat","Horse Meat", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 12,weight(40)|food_quality(30)|max_ammo(40),imodbits_none],
# Items before this point are hardwired and their order should not be changed!
 ["practice_sword","Practice Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(22,blunt)|thrust_damage(20,blunt),imodbits_none],
 ["heavy_practice_sword","Heavy Practice Sword", [("heavy_practicesword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_greatsword,
    21, weight(6.25)|spd_rtng(94)|weapon_length(128)|swing_damage(30,blunt)|thrust_damage(24,blunt),imodbits_none],
 ["practice_dagger","Practice Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_dagger|itcf_carry_dagger_front_left, 2,weight(0.5)|spd_rtng(110)|weapon_length(47)|swing_damage(16,blunt)|thrust_damage(14,blunt),imodbits_none],
 ["practice_axe", "Practice Axe", [("hatchet",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 24 , weight(2) | spd_rtng(95) | weapon_length(75) | swing_damage(24, blunt) | thrust_damage(0, pierce), imodbits_axe],
 ["arena_axe", "Axe", [("arena_axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 137 , weight(1.5)|spd_rtng(100) | weapon_length(69)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["arena_sword", "Sword", [("arena_sword_one_handed",0),("sword_medieval_b_scabbard", ixmesh_carry),], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1.5)|spd_rtng(99) | weapon_length(95)|swing_damage(22 , blunt) | thrust_damage(20 ,  blunt),imodbits_sword_high ],
 ["arena_sword_two_handed",  "Two Handed Sword", [("arena_sword_two_handed",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 670 , weight(2.75)|spd_rtng(93) | weapon_length(110)|swing_damage(30 , blunt) | thrust_damage(24 ,  blunt),imodbits_sword_high ],
 ["arena_lance",         "Lance", [("arena_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
 90 , weight(2.5)|spd_rtng(96) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(25 ,  blunt),imodbits_polearm ],
 ["practice_staff","Practice Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(2.5)|spd_rtng(103) | weapon_length(118)|swing_damage(18,blunt) | thrust_damage(18,blunt),imodbits_none],
 ["practice_lance","Practice Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_greatlance, 18,weight(4.25)|spd_rtng(58)|weapon_length(240)|swing_damage(0,blunt)|thrust_damage(15,blunt),imodbits_none],
 ["practice_shield","Practice Shield", [("shield_round_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 20,weight(3.5)|body_armor(1)|hit_points(200)|spd_rtng(100)|shield_width(50),imodbits_none],
 ["practice_bow","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
##                                                     ("hunting_bow",0)],                  itp_type_bow|itp_two_handed|itp_primary|itp_attach_left_hand, itcf_shoot_bow, 4,weight(1.5)|spd_rtng(90)|shoot_speed(40)|thrust_damage(19,blunt),imodbits_none],
 ["practice_crossbow", "Practice Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(95)| shoot_speed(68) | thrust_damage(23,blunt)|max_ammo(1),imodbits_crossbow],
 ["practice_javelin", "Practice Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5) | spd_rtng(91) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(50) | weapon_length(75), imodbits_thrown],
 ["practice_javelin_melee", "practice_javelin_melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff, 0, weight(1)|difficulty(0)|spd_rtng(91) |swing_damage(12, blunt)| thrust_damage(14,  blunt)|weapon_length(75),imodbits_polearm ],
 ["practice_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(10)|weapon_length(0),imodbits_thrown ],
 ["practice_throwing_daggers_100_amount", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(100)|weapon_length(0),imodbits_thrown ],
# ["cheap_shirt","Cheap Shirt", [("shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 4,weight(1.25)|body_armor(3),imodbits_none],
 ["practice_horse","Practice Horse", [("saddle_horse",0)], itp_type_horse, 0, 37,body_armor(10)|horse_speed(40)|horse_maneuver(37)|horse_charge(14),imodbits_none],
 ["practice_arrows","Practice Arrows", [("arena_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|thrust_damage(1,blunt)|weapon_length(95)|max_ammo(80),imodbits_missile],
## ["practice_arrows","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo)], itp_type_arrows, 0, 31,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_none],
 ["practice_bolts","Practice Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|thrust_damage(1,blunt)|weapon_length(55)|max_ammo(49),imodbits_missile],
 ["practice_arrows_10_amount","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|thrust_damage(1,blunt)|weapon_length(95)|max_ammo(10),imodbits_missile],
 ["practice_arrows_100_amount","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|thrust_damage(1,blunt)|weapon_length(95)|max_ammo(100),imodbits_missile],
 ["practice_bolts_9_amount","Practice Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|thrust_damage(1,blunt)|weapon_length(55)|max_ammo(9),imodbits_missile],
 ["practice_boots", "Practice Boots", [("boot_nomad_a",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10), imodbits_cloth ],
 ["red_tourney_armor","Red Tourney Armor", [("tourn_armor_a",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["blue_tourney_armor","Blue Tourney Armor", [("mail_shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["green_tourney_armor","Green Tourney Armor", [("leather_vest",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["gold_tourney_armor","Gold Tourney Armor", [("padded_armor",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["red_tourney_helmet","Red Tourney Helmet",[("flattop_helmet",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["blue_tourney_helmet","Blue Tourney Helmet",[("segmented_helm",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["green_tourney_helmet","Green Tourney Helmet",[("hood_c",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["gold_tourney_helmet","Gold Tourney Helmet",[("hood_a",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],

["arena_shield_red", "Shield", [("arena_shield_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_blue", "Shield", [("arena_shield_blue",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_green", "Shield", [("arena_shield_green",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_yellow", "Shield", [("arena_shield_yellow",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],

["arena_armor_white", "Arena Armor White", [("arena_armorW_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_red", "Arena Armor Red", [("arena_armorR_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_blue", "Arena Armor Blue", [("arena_armorB_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_green", "Arena Armor Green", [("arena_armorG_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_yellow", "Arena Armor Yellow", [("arena_armorY_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_tunic_white", "Arena Tunic White ", [("arena_tunicW_new",0)], itp_type_body_armor |itp_covers_legs ,0, 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_red", "Arena Tunic Red", [("arena_tunicR_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ], 
["arena_tunic_blue", "Arena Tunic Blue", [("arena_tunicB_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ], 
["arena_tunic_green", "Arena Tunic Green", [("arena_tunicG_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_yellow", "Arena Tunic Yellow", [("arena_tunicY_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
#headwear
["arena_helmet_red", "Arena Helmet Red", [("arena_helmetR",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_blue", "Arena Helmet Blue", [("arena_helmetB",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_green", "Arena Helmet Green", [("arena_helmetG",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_yellow", "Arena Helmet Yellow", [("arena_helmetY",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_white", "Steppe Helmet White", [("steppe_helmetW",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_red", "Steppe Helmet Red", [("steppe_helmetR",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_blue", "Steppe Helmet Blue", [("steppe_helmetB",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_green", "Steppe Helmet Green", [("steppe_helmetG",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_yellow", "Steppe Helmet Yellow", [("steppe_helmetY",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["tourney_helm_white", "Tourney Helm White", [("tourney_helmR",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_red", "Tourney Helm Red", [("tourney_helmR",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_blue", "Tourney Helm Blue", [("tourney_helmB",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_green", "Tourney Helm Green", [("tourney_helmG",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_yellow", "Tourney Helm Yellow", [("tourney_helmY",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_red", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_blue", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_green", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_yellow", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],

# A treatise on The Method of Mechanical Theorems Archimedes
 
#This book must be at the beginning of readable books
 ["book_tactics","De Re Militari", [("book_a",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],
 ["book_persuasion","Rhetorica ad Herennium", [("book_b",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
 ["book_leadership","The Life of Alixenus the Great", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_intelligence","Essays on Logic", [("book_e",0)], itp_type_book, 0, 2900,weight(2)|abundance(100),imodbits_none],
 ["book_trade","A Treatise on the Value of Things", [("book_f",0)], itp_type_book, 0, 3100,weight(2)|abundance(100),imodbits_none],
 ["book_weapon_mastery", "On the Art of Fighting with Swords", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_engineering","Method of Mechanical Theorems", [("book_open",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],

#Reference books
#This book must be at the beginning of reference books
 ["book_wound_treatment_reference","The Book of Healing", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_training_reference","Manual of Arms", [("book_open",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_surgery_reference","The Great Book of Surgery", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],

 #other trade goods (first one is Oil)	#mod edited 20.09.2018


 #["flour","Flour", [("salt_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 40,weight(50)|abundance(100)|food_quality(45)|max_ammo(50),imodbits_none],
 #other trade goods (first one is spice)

 ["pottery","Pottery", [("jug",0)], itp_merchandise|itp_type_goods, 0, 100,weight(50)|abundance(90),imodbits_none],

 ["raw_flax","Flax Bundle", [("raw_flax",0)], itp_merchandise|itp_type_goods, 0, 150,weight(40)|abundance(90),imodbits_none],
 ["linen","Linen", [("linen",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],

 ["wool","Wool", [("wool_sack",0)], itp_merchandise|itp_type_goods, 0, 130,weight(40)|abundance(90),imodbits_none],
 ["wool_cloth","Wool Cloth", [("wool_cloth",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],

 ["raw_silk","Raw Silk", [("raw_silk_bundle",0)], itp_merchandise|itp_type_goods, 0, 600,weight(30)|abundance(90),imodbits_none],
 ["raw_dyes","Dyes", [("dyes",0)], itp_merchandise|itp_type_goods, 0, 200,weight(10)|abundance(90),imodbits_none],
 ["velvet","Velvet", [("velvet",0)], itp_merchandise|itp_type_goods, 0, 1025,weight(40)|abundance(30),imodbits_none],

 ["iron","Iron", [("iron",0)], itp_merchandise|itp_type_goods, 0,264,weight(60)|abundance(60),imodbits_none],
 ["tools","Tools", [("iron_hammer",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbits_none],

 ["raw_leather","Hides", [("leatherwork_inventory",0)], itp_merchandise|itp_type_goods, 0, 120,weight(40)|abundance(90),imodbits_none],
 ["leatherwork","Leatherwork", [("leatherwork_frame",0)], itp_merchandise|itp_type_goods, 0, 220,weight(40)|abundance(90),imodbits_none],
 
 ["furs","Furs", [("fur_pack",0)], itp_merchandise|itp_type_goods, 0, 391,weight(40)|abundance(90),imodbits_none],


# ["dry_bread", "wheat_sack", itp_type_goods|itp_consumable, 0, slt_none,view_goods,95,weight(2),max_ammo(50),imodbits_none],
#foods (first one is smoked_fish)
 ["smoked_fish","Smoked Fish", [("smoked_fish",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 65,weight(15)|abundance(110)|food_quality(50)|max_ammo(50),imodbits_none],
 ["cheese","Cheese", [("cheese_b",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(6)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],
 ["honey","Honey", [("honey_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 220,weight(5)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],
 ["sausages","Sausages", [("sausages",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(10)|abundance(110)|food_quality(40)|max_ammo(40),imodbits_none],
 ["cabbages","Cabbages", [("cabbage",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 30,weight(15)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["dried_meat","Dried Meat", [("smoked_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(15)|abundance(100)|food_quality(70)|max_ammo(50),imodbits_none],
 ["apples","Fruit", [("apple_basket",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 44,weight(20)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["raw_grapes","Grapes", [("grapes_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 75,weight(40)|abundance(90)|food_quality(10)|max_ammo(10),imodbits_none], #x2 for wine
 ["grain","Grain", [("wheat_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 30,weight(30)|abundance(110)|food_quality(1)|max_ammo(50),imodbits_none],
 ["raw_olives","Olives", [("olive_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 100,weight(40)|abundance(90)|food_quality(10)|max_ammo(10),imodbits_none], #x3 for oil

 ["spice","Spice", [("spice_sack",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 880,weight(40)|food_quality(70)|abundance(25)|max_ammo(50),imodbits_none],
 ["salt","Salt", [("salt_sack",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 255,weight(50)|food_quality(10)|max_ammo(40)|abundance(120),imodbits_none],
 ["oil","Oil", [("oil",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 450,weight(50)|food_quality(20)|abundance(60)|max_ammo(50),imodbits_none],

 
 ["wine","Wine", [("amphora_slim",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 220,weight(30)|food_quality(30)|abundance(60)|max_ammo(50),imodbits_none],## 30.04.2018	wasnt between food.
 ["ale","Ale", [("ale_barrel",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 120,weight(30)|food_quality(30)|abundance(70)|max_ammo(50),imodbits_none],## 30.04.2018
 
 ["raw_date_fruit","Date Fruit", [("date_inventory",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 120,weight(40)|food_quality(10)|max_ammo(10),imodbits_none],

 
 ["cattle_meat","Beef", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 80,weight(20)|abundance(100)|food_quality(80)|max_ammo(50),imodbits_none],
 ["bread","Bread", [("bread_a",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 50,weight(30)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["chicken","Chicken", [("chicken",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 95,weight(10)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["pork","Pork", [("pork",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(15)|abundance(100)|food_quality(70)|max_ammo(50),imodbits_none],
 ["butter","Butter", [("butter_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(6)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],
 

 #Would like to remove flour altogether and reduce chicken, pork and butter (perishables) to non-trade items. Apples could perhaps become a generic "fruit", also representing dried fruit and grapes
 # Armagan: changed order so that it'll be easier to remove them from trade goods if necessary.
#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************

# Quest Items

 ["siege_supply","Supplies", [("ale_barrel",0)], itp_type_goods, 0, 96,weight(40)|abundance(70),imodbits_none],
 ["quest_wine","Wine", [("amphora_slim",0)], itp_type_goods, 0, 46,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
 ["quest_ale","Ale", [("ale_barrel",0)], itp_type_goods, 0, 31,weight(40)|abundance(70)|max_ammo(50),imodbits_none],

 
# Tutorial Items

 ["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
 ["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar|itcf_carry_mace_left_hip, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile],
 ["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Kite Shield", [("shield_kite_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],

# Horses: sumpter horse/ pack horse, saddle horse, steppe horse, warm blood, geldling, stallion,   war mount, charger, 
# Carthorse, hunter, heavy hunter, hackney, palfrey, courser, destrier.
 ["sumpter_horse","Sumpter Horse", [("sumpter_horse",0)], itp_merchandise|itp_type_horse, 0, 
267,abundance(90)|hit_points(100)|body_armor(14)|difficulty(1)|horse_speed(37)|horse_maneuver(39)|horse_charge(9)|horse_scale(100),imodbits_horse_basic],
 
 ##################           NEW
 ["donkey","Donkey", [("donkey_mount",0)], itp_merchandise|itp_type_horse, 0, 
117,abundance(90)|hit_points(110)|body_armor(5)|difficulty(0)|horse_speed(32)|horse_maneuver(37)|horse_charge(8)|horse_scale(100),imodbits_horse_basic],
 ["rus_horse","Slav Horse", [("rus_horse",0)], itp_merchandise|itp_type_horse, 0, 
578,abundance(90)|hit_points(122)|body_armor(15)|difficulty(2)|horse_speed(42)|horse_maneuver(43)|horse_charge(15)|horse_scale(100),imodbits_horse_basic],

 ["padded_warhorse","Padded Warhorse", [("romeian_barded_warhorse",0)], itp_merchandise|itp_type_horse, 0, 
2105,abundance(50)|hit_points(131)|body_armor(28)|difficulty(4)|horse_speed(42)|horse_maneuver(40)|horse_charge(26)|horse_scale(110),imodbits_horse_basic|imodbit_champion],

 ["barded_warhorse","Barded Warhorse", [("barded_warhorse_a",0)], itp_merchandise|itp_type_horse, 0, 
2017,abundance(50)|hit_points(128)|body_armor(23)|difficulty(4)|horse_speed(41)|horse_maneuver(42)|horse_charge(22)|horse_scale(110),imodbits_horse_basic|imodbit_champion],

# ["heraldic_barded_warhorse","Heraldic Barded Warhorse", [("barded_warhorse_a",0)], itp_merchandise|itp_type_horse, 0, 
# 4034,abundance(50)|hit_points(128)|body_armor(23)|difficulty(4)|horse_speed(41)|horse_maneuver(42)|horse_charge(22)|horse_scale(110),imodbits_horse_basic|imodbit_champion,
# [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_barded_warhorse", ":agent_no", ":troop_no")])]],


 
 
 
 
###################
 ["steppe_horse","Steppe Horse", [("steppe_horse",0)], itp_merchandise|itp_type_horse, 0, 
467,abundance(80)|hit_points(120)|body_armor(10)|difficulty(2)|horse_speed(40)|horse_maneuver(51)|horse_charge(8)|horse_scale(98),imodbits_horse_basic, [], [fac_kingdom_2, fac_kingdom_3]],
 ["saddle_horse","Saddle Horse", [("saddle_horse",0),("horse_c",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 
632,abundance(90)|difficulty(1)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104),imodbits_horse_basic],
 ["saddle_horse_b","Saddle Horse B", [("horse_c",0)], itp_merchandise|itp_type_horse, 0, 
632,abundance(90)|difficulty(1)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104),imodbits_horse_basic],
 ["arabian_horse_a","Desert Horse", [("arabian_horse_a",0)], itp_merchandise|itp_type_horse, 0, 
774,abundance(80)|hit_points(110)|body_armor(10)|difficulty(2)|horse_speed(42)|horse_maneuver(50)|horse_charge(12)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3, fac_kingdom_6]],
 ["courser","Courser", [("courser",0)], itp_merchandise|itp_type_horse, 0, 
1874,abundance(70)|body_armor(12)|hit_points(110)|difficulty(3)|horse_speed(50)|horse_maneuver(44)|horse_charge(12)|horse_scale(106),imodbits_horse_basic|imodbit_champion],
 ["hunter","Hunter", [("hunting_horse",0),("hunting_horse",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 
2087,abundance(60)|hit_points(160)|body_armor(18)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(108),imodbits_horse_basic|imodbit_champion],
 ["arabian_horse_b","Arabian Warhorse", [("arabian_horse_b",0)], itp_merchandise|itp_type_horse, 0, 
2342,abundance(80)|hit_points(120)|body_armor(10)|difficulty(3)|horse_speed(43)|horse_maneuver(54)|horse_charge(16)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6]],
 ["warhorse","War Horse", [("warhorse_chain",0)], itp_merchandise|itp_type_horse, 0,
3244,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
 ["warhorse_b","War Horse", [("warhorse_zagibu",0)], itp_merchandise|itp_type_horse, 0, 
3484,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
 ["warhorse_steppe","Steppe Charger", [("warhorse_steppe",0)], itp_merchandise|itp_type_horse, 0, 
2061,abundance(45)|hit_points(150)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(50)|horse_charge(28)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3,fac_kingdom_2]],
 ["charger","Charger", [("charger_new",0)], itp_merchandise|itp_type_horse, 0, 
3595,abundance(40)|hit_points(165)|body_armor(58)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
 ["warhorse_sarranid","Sarranian War Horse", [("warhorse_sarranid",0)], itp_merchandise|itp_type_horse, 0, 
3595,abundance(40)|hit_points(165)|body_armor(58)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6]],
 ["plated_charger","Plated Charger", [("charger_plate_1",0)], itp_merchandise|itp_type_horse, 0, 
4467,abundance(40)|hit_points(180)|body_armor(75)|difficulty(5)|horse_speed(39)|horse_maneuver(32)|horse_charge(62)|horse_scale(116),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_2]],



#whalebone crossbow, yew bow, war bow, arming sword 
 ["arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back, 
84,weight(6)|abundance(160)|weapon_length(95)|thrust_damage(6,cut)|max_ammo(24),imodbits_missile],
 ["khergit_arrows","Tatar Arrows", [("arrow_b",0),("flying_missile",ixmesh_flying_ammo),("quiver_b", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
347,weight(6)|abundance(30)|weapon_length(95)|thrust_damage(15,cut)|max_ammo(22),imodbits_missile],
 ["barbed_arrows","Barbed Arrows", [("barbed_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_d", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
267,weight(6)|abundance(70)|weapon_length(95)|thrust_damage(10,cut)|max_ammo(20),imodbits_missile],
 ["bodkin_arrows","Bodkin Arrows", [("piercing_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_c", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
376,weight(6)|abundance(50)|weapon_length(91)|thrust_damage(6,pierce)|max_ammo(20),imodbits_missile],
 ["bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 
218,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(8,pierce)|max_ammo(24),imodbits_missile],
 ["steel_bolts","Steel Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag_c", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 
367,weight(2.5)|abundance(20)|weapon_length(63)|thrust_damage(15,pierce)|max_ammo(18),imodbits_missile],
 ["cartridges","Cartridges", [("cartridge_a",0)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo, 0, 
433,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(10,pierce)|max_ammo(50),imodbits_missile],

["pilgrim_disguise", "Pilgrim Disguise", [("pilgrim_outfit",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0, 
51, weight(3)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["pilgrim_hood", "Pilgrim Hood", [("pilgrim_hood",0)], 0| itp_type_head_armor |itp_civilian  ,0, 
17, weight(0.3)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# ARMOR
#handwear
["leather_gloves","Leather Gloves", [("leather_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0, 
45, weight(0.3)|abundance(120)|body_armor(2)|difficulty(0),imodbits_cloth],
["black_leather_gloves","Black Leather Gloves", [("black_leather_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0, 
45, weight(0.3)|abundance(120)|body_armor(2)|difficulty(0),imodbits_cloth],

["leather_gloves_b","Colored Leather Gloves", [("leather_gloves_b_L",0)], itp_merchandise|itp_type_hand_armor,0, 
45, weight(0.3)|abundance(120)|body_armor(2)|difficulty(0),imodbits_cloth,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_colored_gloves", ":agent_no", ":troop_no")])]],


["mail_mittens","Mail Mittens", [("mail_mittens_L",0)], itp_merchandise|itp_type_hand_armor,0, 
210, weight(0.5)|abundance(100)|body_armor(3)|difficulty(0),imodbits_armor],
["mail_gloves","Mail Gloves", [("mail_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0, 
210, weight(0.5)|difficulty(0)|abundance(100)|body_armor(3),imodbits_armor],
["wisby_gloves_black","Wisby Gloves", [("wisby_gloves_black_L",0)], itp_merchandise|itp_type_hand_armor,0, 
260, weight(0.7)|difficulty(0)|abundance(90)|body_armor(4),imodbits_armor],
["wisby_gloves_red","Red Wisby Gloves", [("wisby_gloves_red_L",0)], itp_merchandise|itp_type_hand_armor,0, 
260, weight(0.7)|difficulty(0)|abundance(90)|body_armor(4),imodbits_armor],
["mail_gauntlets","Mail Gauntlets", [("mail_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 
260, weight(0.7)|difficulty(0)|abundance(100)|body_armor(4),imodbits_armor],
["scale_gloves_a","Lamellar Gloves", [("scale_gloves_a_L",0)], itp_merchandise|itp_type_hand_armor,0, 
426, weight(0.9)|difficulty(0)|abundance(70)|body_armor(5),imodbits_armor],
["scale_gloves_b","Scale Gloves", [("scale_gloves_b_L",0)], itp_merchandise|itp_type_hand_armor,0, 
426, weight(0.9)|difficulty(0)|abundance(70)|body_armor(5),imodbits_armor],
["wisby_gauntlets_black","Wisby Gauntlets", [("wisby_gauntlets_black_L",0)], itp_merchandise|itp_type_hand_armor,0, 
426, weight(0.9)|difficulty(0)|abundance(90)|body_armor(5),imodbits_armor],
["wisby_gauntlets_red","Red Wisby Gauntlets", [("wisby_gauntlets_red_L",0)], itp_merchandise|itp_type_hand_armor,0, 
426, weight(0.9)|difficulty(0)|abundance(90)|body_armor(5),imodbits_armor],
["scale_gauntlets","Scale Gauntlets", [("scale_gauntlets_b_L",0)], itp_merchandise|itp_type_hand_armor,0, 
562, weight(1.1)|abundance(100)|body_armor(6)|difficulty(7),imodbits_armor],
["lamellar_gauntlets","Lamellar Gauntlets", [("scale_gauntlets_a_L",0)], itp_merchandise|itp_type_hand_armor,0, 
562, weight(1.1)|abundance(100)|body_armor(6)|difficulty(7),imodbits_armor],
["hourglass_gloves","Hourglass Gloves", [("hourglass_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0, 
562, weight(1.1)|difficulty(7)|abundance(50)|body_armor(6),imodbits_armor],
["gilded_hourglass_gloves","Gilded Hourglass Gloves", [("hourglass_gloves_ornate_L",0)], itp_merchandise|itp_type_hand_armor,0, 
612, weight(1.1)|difficulty(7)|abundance(50)|body_armor(6),imodbits_armor],
["short_plate_mittens","Short Plate Mittens", [("short_plate_mittens_L",0)], itp_merchandise|itp_type_hand_armor,0, 
670, weight(1.3)|difficulty(7)|abundance(40)|body_armor(7),imodbits_armor],
["hourglass_gauntlets_a","Hourglass Gauntlets", [("hourglass_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 
670, weight(1.3)|difficulty(7)|abundance(50)|body_armor(7),imodbits_armor],
["hourglass_gauntlets_b","Gilded Hourglass Gauntlets", [("hourglass_gauntlets_ornate_L",0)], itp_merchandise|itp_type_hand_armor,0, 
705, weight(1.3)|difficulty(7)|abundance(50)|body_armor(7),imodbits_armor],
["plate_mittens","Plate Mittens", [("plate_mittens_L",0)], itp_merchandise|itp_type_hand_armor,0, 
751, weight(1.5)|difficulty(8)|abundance(90)|body_armor(8),imodbits_armor],
["hourglass_gauntlets_c","Ornamented Hourglass Gauntlets", [("new_hourglass_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 
751, weight(1.5)|difficulty(8)|abundance(50)|body_armor(8),imodbits_armor],
["wisby_gloves","Black and White Plate Gloves", [("bnw_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0, 
751, weight(1.5)|difficulty(8)|abundance(30)|body_armor(8),imodbits_armor],
["heavy_plate_gloves","Heavy Plate Gloves", [("heavy_plate_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0, 
1028, weight(1.7)|difficulty(8)|abundance(20)|body_armor(9),imodbits_armor],
["gloves_a","Plated Gloves", [("glove1_L",0)], itp_merchandise|itp_type_hand_armor,0, 
1028, weight(1.7)|difficulty(8)|abundance(50)|body_armor(9),imodbits_armor],
["bnw_gauntlets","Black Gauntlets", [("bnw_gauntlet_L",0)], itp_merchandise|itp_type_hand_armor,0, 
1028, weight(1.7)|difficulty(8)|abundance(90)|body_armor(9),imodbits_armor],
["gauntlets","Heavy Gauntlets", [("gauntlets_L",0),("gauntlets_L",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0, 
1057, weight(2)|abundance(100)|body_armor(10)|difficulty(9),imodbits_armor],
################################             Gloves


#footwear
["wrapping_boots", "Wrapping Boots", [("wrapping_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
1, weight(0.1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["woolen_hose", "Woolen Hose", [("woolen_hose_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
3, weight(0.1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["blue_hose", "Blue Hose", [("blue_hose_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
5, weight(0.1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["narf_hose", "Brown Hose", [("narf_hose",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature,0,
5, weight(0.1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["turkish_shoes", "Turkish Shoes", [("luxurious_hose",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature,0,
5, weight(0.1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["serbian_ankle_boots", "Serbian Ankle Boots", [("serbian_ankle_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
5, weight(0.1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],

["sarranid_boots_a", "Saracen Shoes", [("sarranid_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
15, weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["hunter_boots", "Hunter Boots", [("hunter_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature,0,
22, weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(11)|difficulty(0) ,imodbits_cloth ],
["hide_boots", "Hide Boots", [("hide_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
33, weight(0.3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["rus_shoes", "Rus Shoes", [("rus_shoes",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature,0,
39, weight(0.3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth ],
["sarranid_boots_b", "Saracen Leather Boots", [("sarranid_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
55, weight(0.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
["ankle_boots", "Ankle Boots", [("ankle_boots_a_new",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
55, weight(0.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
["khergit_leather_boots", "Mongolian Leather Boots", [("khergit_leather_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
55, weight(0.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(7) ,imodbits_cloth ],

["kazakh_boots", "Kazakh Boots", [("new_kazakh.1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature,0,
65, weight(0.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],

 
["nomad_boots", "Nomad Boots", [("nomad_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
83, weight(0.6)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(6) ,imodbits_cloth ],
["light_leather_boots",  "Light Leather Boots", [("light_leather_boots",0)], itp_type_foot_armor |itp_merchandise| itp_attach_armature,0, 
83, weight(0.7)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(6) ,imodbits_cloth ],

["leather_boots", "Leather Boots", [("leather_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
161, weight(0.8)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(19)|difficulty(6) ,imodbits_cloth ],
["rus_cav_boots", "Rus Cavalry Boots", [("rus_cav_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
255, weight(0.8)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(6) ,imodbits_cloth ],

["hose_kneecops_red", "Red Hose with Kneecops", [("hose_kneecops_red",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
349, weight(0.9)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(6) ,imodbits_cloth ],

["hose_kneecops_green", "Green Hose with Kneecops", [("hose_kneecops_green",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
349, weight(0.9)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(6) ,imodbits_cloth ],

["mail_chausses", "Mail Chausses", [("mail_chausses_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
587, weight(1.7)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(8) ,imodbits_armor ],
["sarranid_boots_d", "Saracen Mail Boots", [("sarranid_mail_chausses",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
626, weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(9) ,imodbits_armor ],
["norman_shoes", "Norman Mail Chausses", [("norman_shoes",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
626, weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(9) ,imodbits_armor ],

["splinted_leather_greaves", "Splinted Leather Greaves", [("leather_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
649, weight(2.1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(31)|difficulty(9) ,imodbits_armor ],

["splinted_greaves", "Splinted Greaves", [("splinted_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
710, weight(2.4)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],

["sarranid_boots_c", "Plated Boots", [("sarranid_camel_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
770, weight(2.6)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(34)|difficulty(10) ,imodbits_plate ],
["rus_splint_greaves", "Rus Splinted Greaves", [("rus_splint_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
770, weight(2.6)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(34)|difficulty(10) ,imodbits_armor ],

["mail_boots", "Mail Boots", [("mail_boots_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
833, weight(2.9)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(36)|difficulty(10) ,imodbits_armor ],
["mail_and_plate_boots_b", "Light Mail and Plate Boots", [("plate_mail_boot",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
833, weight(2.9)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(36)|difficulty(11) ,imodbits_armor ],

["iron_greaves", "Iron Greaves", [("iron_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
885, weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(37)|difficulty(11) ,imodbits_armor ],
["splinted_greaves_spurs", "Splinted Greaves with Spurs", [("splinted_greaves_spurs",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
885, weight(2.7)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(37)|difficulty(10) ,imodbits_armor ],
["khergit_guard_boots",  "Mongolian Guard Boots", [("lamellar_boots_a",0)], itp_type_foot_armor|itp_merchandise | itp_attach_armature,0,
885, weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(37)|difficulty(11) ,imodbits_cloth ],

["shynbaulds", "Shynbaulds", [("shynbaulds",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
922, weight(3.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(38)|difficulty(11) ,imodbits_armor ],
["mail_and_plate_boots_a", "Mail and Plate Boots", [("plate_boot",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
982, weight(3.4)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(39)|difficulty(12) ,imodbits_armor ],
["plate_boots", "Plate Boots", [("plate_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
982, weight(3.4)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(39)|difficulty(13) ,imodbits_plate ], 

["steel_greaves_a", "Cased Greaves", [("steel_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
1070, weight(3.6)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(12) ,imodbits_armor ],
["steel_greaves_b", "Ornamented Steel Greaves", [("new_steel_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
1070, weight(3.6)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(12) ,imodbits_armor ],

["black_greaves", "Black Greaves", [("black_greaves",0)], itp_type_foot_armor  | itp_attach_armature,0,
1180, weight(3.8)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(41)|difficulty(12) ,imodbits_armor ],





 
 
["sarranid_head_cloth", "Lady Head Cloth", [("tulbent",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_head_cloth_b", "Lady Head Cloth", [("tulbent_b",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_head_cloth", "Head Cloth", [("common_tulbent",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_head_cloth_b", "Head Cloth", [("common_tulbent_b",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],




#bodywear
["lady_dress_ruby", "Lady Dress", [("lady_dress_r",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth],
["lady_dress_green", "Lady Dress", [("lady_dress_g",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth],
["lady_dress_blue", "Lady Dress", [("lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth],
["red_dress", "Red Dress", [("red_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth],
["brown_dress", "Brown Dress", [("brown_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth],
["green_dress", "Green Dress", [("green_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth],
["khergit_lady_dress", "Mongolian Lady Dress", [("khergit_lady_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth],
["khergit_lady_dress_b", "Mongolian Leather Lady Dress", [("khergit_lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth],
["sarranid_lady_dress", "Sarranid Lady Dress", [("sarranid_lady_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth],
["sarranid_lady_dress_b", "Sarranid Lady Dress", [("sarranid_lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth],
["sarranid_common_dress", "Sarranid Dress", [("sarranid_common_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth],
["sarranid_common_dress_b", "Sarranid Dress", [("sarranid_common_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth],
["courtly_outfit", "Courtly Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["nobleman_outfit", "Nobleman Outfit", [("nobleman_outfit_b_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth ], 
["nomad_armor", "Nomad Armor", [("nomad_armor_new",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs   ,0, 75 , weight(2.1)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["khergit_armor", "Mongolian Skirmisher Armor", [("khergit_armor_new",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs ,0, 55 , weight(1.3)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_jacket", "Leather Jacket", [("leather_jacket_new",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs  |itp_civilian ,0, 50 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

#NEW:
["rawhide_coat", "Rawhide Coat", [("coat_of_plates_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 12 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(11)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
#NEW: was lthr_armor_a
["leather_armor", "Leather Armor", [("tattered_leather_armor_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs  ,0, 65 , weight(2.1)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["fur_coat", "Fur Coat", [("fur_coat",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 117 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(7)|difficulty(0) ,imodbits_armor ],



#for future:
["coat", "Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["leather_coat", "Leather Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["mail_coat", "Coat of Mail", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_mail_coat", "Long Coat of Mail", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["mail_with_tunic_red", "Mail with Tunic", [("arena_armorR_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(8), imodbits_armor ],
["mail_with_tunic_green", "Mail with Tunic", [("arena_armorG_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(8), imodbits_armor ],
["hide_coat", "Hide Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["merchant_outfit", "Merchant Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["homespun_dress", "Homespun Dress", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["thick_coat", "Thick Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["coat_with_cape", "Coat with Cape", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["steppe_outfit", "Steppe Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nordic_outfit", "Nordic Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nordic_armor", "Nordic Armor", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["hide_armor", "Hide Armor", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["cloaked_tunic", "Cloaked Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sleeveless_tunic", "Sleeveless Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sleeveless_leather_tunic", "Sleeveless Leather Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["linen_shirt", "Linen Shirt", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["wool_coat", "Wool Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#end

 


["dress", "Dress", [("dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(0.3)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
["blue_dress", "Blue Dress", [("blue_dress_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(0.3)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
["peasant_dress", "Peasant Dress", [("peasant_dress_b_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(0.3)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(3)|difficulty(0) ,imodbits_cloth ], 
["woolen_dress", "Woolen Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor|itp_civilian  |itp_covers_legs ,0,
 10 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
["sarranid_dress_a", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 55 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["sarranid_dress_b", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 55 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],

#Quest-specific - perhaps can be used for prisoners, 
["burlap_tunic", "Burlap Tunic", [("shirt",0)], itp_type_body_armor  |itp_covers_legs ,0,
 5 , weight(0.3)|abundance(100)|head_armor(0)|body_armor(3)|leg_armor(1)|difficulty(0) ,imodbits_armor ],

 
 
######## LIGHT ARMORS 1-30 body armor

["shirt", "Shirt", [("shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
1, weight(0.2)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_a", "Shirt", [("fattiglinenskjortir",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
1, weight(0.2)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],

["linen_shirt_b", "Red Shirt", [("redvikingshirt",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
1, weight(0.2)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_c", "Blue Shirt", [("bluevikingshirt",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
1, weight(0.2)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["linen_shirt_d", "Green Shirt", [("greenvikingshirt",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
1, weight(0.2)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],

 #NEW: was "linen_tunic"
["linen_tunic", "Linen Tunic", [("shirt_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
3, weight(0.3)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["tunic_with_green_cape", "Tunic with Green Cape", [("peasant_man_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 
4, weight(0.3)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(3)|difficulty(0) ,imodbits_cloth ], 
 #NEW was cvl_costume_a
["short_tunic", "Red Tunic", [("rich_tunic_a",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
5, weight(0.4)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
#TODO:
["red_shirt", "Red Shirt", [("rich_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
5, weight(0.4)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["red_tunic", "Red Tunic", [("arena_tunicR_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
5,  weight(0.4)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],

["green_tunic", "Green Tunic", [("arena_tunicG_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
5,  weight(0.4)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["blue_tunic", "Blue Tunic", [("arena_tunicB_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
5, weight(0.4)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["robe", "Robe", [("robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
15, weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["nord_nobleman_outfit", "Nord Nobleman Outfit", [("noblemanshirt",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
348, weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],

 ##armors_d
["pelt_coat", "Pelt Coat", [("thick_coat_a",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
22, weight(0.6)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["saracen_shirt_a", "Saracen Shirt", [("saracen_shirt_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
22, weight(0.8)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["sarranid_cloth_robe", "Worn Robe", [("sar_robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
24, weight(0.8)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["sarranid_cloth_robe_b", "Worn Robe", [("sar_robe_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
24, weight(0.8)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],

["deli_robe_b", "Turkish Robe", [("bashibazouk_robe_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs  ,0, 
25, weight(0.8)|abundance(100)|head_armor(0)|body_armor(11)|leg_armor(3)|difficulty(0) ,imodbits_cloth ], 
["saracen_shirt_b", "Saracen Patterned Shirt", [("saracen_shirt_c",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
27, weight(0.9)|abundance(100)|head_armor(0)|body_armor(11)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["saracen_shirt_c", "Saracen Padded Shirt", [("saracen_padded_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
27, weight(0.9)|abundance(100)|head_armor(0)|body_armor(11)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

 
#NEW: was coarse_tunic
["lithuanian_shirt", "Lithuanian Shirt", [("armor_21",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
28, weight(2.1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["coarse_tunic", "Tunic with vest", [("coarse_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
29, weight(1.1)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],

["leather_apron", "Leather Apron", [("leather_apron",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
30, weight(1.3)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
#NEW: was tabard_a
["tabard", "Tabard", [("tabard_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
53, weight(1.7)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["black_kaftan", "Black Kaftan", [("raylin_black_kaftan",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
53, weight(1.7)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["blue_kaftan", "Blue Kaftan", [("raylin_blue_kaftan",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
53, weight(1.7)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["red_kaftan", "Red Kaftan", [("raylin_red_kaftan",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
53, weight(1.7)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["white_kaftan", "White Kaftan", [("raylin_white_kaftan",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
53, weight(1.7)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],

 
 #NEW: was leather_vest
["leather_vest", "Leather Vest", [("leather_vest_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
73, weight(1.9)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["skirmisher_armor", "Skirmisher Armor", [("skirmisher_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
73, weight(2.1)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

["blue_kaftan", "Blue Kaftan", [("blue_kaftan",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
91, weight(1.7)|abundance(100)|head_armor(0)|body_armor(17)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["drz_kaftan", "Red Kaftan", [("drz_kaftan",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
91, weight(1.7)|abundance(100)|head_armor(0)|body_armor(17)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["steppe_armor", "Steppe Armor", [("lamellar_leather",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
97, weight(2.2)|abundance(100)|head_armor(0)|body_armor(17)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],

["kazakh_outfit", "Kazakh Outfit", [("new_kazakh",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,  
105, weight(2)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],

["white_gambeson_a", "White Gambeson", [("white_gambeson_kovas",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
170, weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(5) ,imodbits_cloth ],
["blue_gambeson_a", "Blue Gambeson", [("blue_gambeson_kovas",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
170, weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(5) ,imodbits_cloth ],
 
 
["gambeson", "White Gambeson", [("white_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
251, weight(3.1)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["blue_gambeson", "Blue Gambeson*", [("blue_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
251, weight(3.1)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW: was red_gambeson
["red_gambeson", "Red Gambeson", [("red_gambeson_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
251, weight(3.1)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW: was aketon_a
["padded_cloth", "Aketon", [("padded_cloth_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
293, weight(3.5)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
#NEW:
["aketon_green", "Padded Cloth", [("padded_cloth_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
284, weight(3.5)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["nomad_vest", "Nomad Vest", [("nomad_vest_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
277, weight(3.8)|abundance(50)|head_armor(0)|body_armor(23)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],

 #NEW: was "leather_jerkin"
["leather_jerkin", "Leather Jerkin", [("ragged_leather_jerkin",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
306, weight(3.9)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["ragged_outfit", "Ragged Outfit", [("ragged_outfit_a_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
319, weight(4.1)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["archers_vest", "Saracen Padded Vest", [("archers_vest",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
321, weight(4.4)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(13)|difficulty(0) ,imodbits_cloth ],


["deli_robe", "Deli Robe", [("deli_robe",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs  ,0, 
372, weight(3.9)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
["leather_scale_armor", "Leather Scale Armor", [("archer_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
397, weight(4.5)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(9)|difficulty(4) ,imodbits_armor ],    
 
 
["gambeson_b", "Padded Jack", [("gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
412, weight(4.4)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(8)|difficulty(4) ,imodbits_cloth ],
["light_leather", "Light Leather", [("light_leather",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 
427, weight(4.9)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(8)|difficulty(5) ,imodbits_armor ],
["ranger_leather_armor", "Ranger Leather Armor", [("ranger_leather_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs  ,0, 
442, weight(5)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(4) ,imodbits_cloth ],

 
 #NEW: was padded_leather
["padded_leather", "Padded Leather", [("leather_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
478, weight(5.5)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(11)|difficulty(0) ,imodbits_cloth ],
["tribal_warrior_outfit", "Tribal Warrior Outfit", [("tribal_warrior_outfit_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
478, weight(5.6)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(11)|difficulty(0) ,imodbits_cloth ],
["sarranid_leather_armor", "Saracen Leather Armor", [("sarranid_leather_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
502, weight(6.1)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(13)|difficulty(6) ,imodbits_armor ],

["nomad_robe", "Nomad Robe", [("nomad_robe_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0,
515, weight(6)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(0) ,imodbits_cloth ],
#["heraldric_armor", "Heraldric Armor", [("tourn_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 442 , weight(17)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#NEW: was "std_lthr_coat"
["peltastos_armor", "Peltastos Armor", [("peltastos_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
570, weight(6.6)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(11)|difficulty(6) ,imodbits_plate ],

 
 ##############################################
###### Medium Armors  31 - 50
#######################################
###################### 
["padded_cloth_b", "Gilded Heavy Aketon", [("luxurious_aketon",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
600, weight(6.6)|abundance(100)|head_armor(0)|body_armor(31)|leg_armor(11)|difficulty(6) ,imodbits_cloth ],
["padded_cloth_c", "Heavy Aketon", [("new_aketon",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
600, weight(6.6)|abundance(100)|head_armor(0)|body_armor(31)|leg_armor(11)|difficulty(6) ,imodbits_cloth ],


["byrnie", "Byrnie", [("byrnie_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
735, weight(8.6)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(4)|difficulty(6) ,imodbits_armor ],
["mail_shirt_with_fur", "Mail Shirt with Fur", [("mail_shirt_with_fur",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
735, weight(8.6)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(4)|difficulty(8) ,imodbits_armor ],
["lamellar_vest", "Lamellar Vest", [("lamellar_vest_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
755, weight(9.1)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(7)|difficulty(8) ,imodbits_cloth ],
["lamellar_vest_khergit", "Mongolian Lamellar Vest", [("lamellar_vest_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
755, weight(9.1)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(7)|difficulty(8) ,imodbits_cloth ],
["sarranid_cavalry_robe", "Cavalry Robe", [("arabian_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
780, weight(9.4)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(9)|difficulty(9) ,imodbits_armor ],
["arabian_armor_a2", "Dark Cavalry Robe", [("arabian_armor_a2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
780, weight(9.4)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(9)|difficulty(9) ,imodbits_armor ],

 
["byrnja", "Byrnja", [("dejawolf_vikingbyrnie",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
805, weight(9.4)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(6)|difficulty(9) ,imodbits_armor ],
["byrnja_b", "Brown Byrnja", [("dejawolf_vikingbyrnie_h1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
805, weight(9.4)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(6)|difficulty(9) ,imodbits_armor ],
["byrnja_c", "Grey Byrnja", [("dejawolf_vikingbyrnie_h2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
805, weight(9.4)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(6)|difficulty(9) ,imodbits_armor ],
["byrnja_d", "Black Byrnja", [("dejawolf_vikingbyrnie_h3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
805, weight(9.4)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(6)|difficulty(9) ,imodbits_armor ],
["mail_shirt", "Mail Shirt", [("mail_shirt_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
832, weight(9.6)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(7)|difficulty(8) ,imodbits_armor ],
["drz_mail_shirt", "Druzhina Mail Shirt", [("drz_mail_shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
832, weight(9.6)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(7)|difficulty(9) ,imodbits_armor ],
["skutatos_armor", "Skutatos Armor", [("skutatos_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
832, weight(9.6)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(7)|difficulty(9) ,imodbits_plate ],
["saracen_mail_b", "Saracen Collared Mail Shirt", [("saracen_mail_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
847, weight(9.8)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(8)|difficulty(9) ,imodbits_armor ],
["swordsman_armor", "Swordsman Armor", [("swordsman_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs  ,0, 
857, weight(10.6)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(9)|difficulty(9) ,imodbits_cloth ],
["saracen_mail_c", "Saracen Shirt over Mail", [("saracen_shirt_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
875, weight(10.1)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(10)|difficulty(10) ,imodbits_armor ],
["mail_hauberk", "Mail Hauberk", [("hauberk_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
893, weight(10.3)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(11)|difficulty(9) ,imodbits_armor ],
["dark_hauberk", "Dark Hauberk", [("Dark_Hauberk",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
893, weight(10.3)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(11)|difficulty(10) ,imodbits_armor ],
["norman_mail", "Norman Mail", [("norman_hauberk_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
998, weight(11.3)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(20)|difficulty(10) ,imodbits_armor ],

 
 
["saracen_mail_a", "Saracen Mail over Padded Shirt", [("saracen_mail_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1007, weight(10.2)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(9)|difficulty(10) ,imodbits_armor ],
["scale_armor", "Scale Armor", [("lamellar_armor_e",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1032, weight(10.6)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(10)|difficulty(9) ,imodbits_armor ],
["brigandine_green", "Green Brigandine over Aketon", [("brigandine_over_aketon_new_green",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
1032, weight(10.6)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(10)|difficulty(9) ,imodbits_armor ],
["brigandine_blue", "Blue Brigandine over Aketon", [("new_brigandine_blue",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
1032, weight(10.6)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(10)|difficulty(9) ,imodbits_armor ],
["brigandine_red_c", "Red Brigandine over Aketon", [("new_brigandine_red",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
1032, weight(10.6)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(10)|difficulty(9) ,imodbits_armor ],
["brigandine_black", "Black Brigandine over Aketon", [("brigandine_over_aketon_black",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
1032, weight(10.6)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(10)|difficulty(9) ,imodbits_armor ],
["brigandine_brown", "Brown Brigandine over Aketon", [("brigandine_over_aketon_brown",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
1032, weight(10.6)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(10)|difficulty(9) ,imodbits_armor ],
["brigandine_purple", "Purple Brigandine over Aketon", [("brigandine_over_aketon_purple",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
1032, weight(10.6)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(10)|difficulty(9) ,imodbits_armor ],
["brigandine_white", "White Brigandine over Aketon", [("brigandine_over_aketon_white",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
1032, weight(10.6)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(10)|difficulty(9) ,imodbits_armor ],
["brigandine_yellow", "Yellow Brigandine over Aketon", [("brigandine_over_aketon_yellow",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
1032, weight(10.6)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(10)|difficulty(9) ,imodbits_armor ],
["palace_guard", "Palace Guard Armor", [("palace_guard",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1059, weight(10.8)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(11)|difficulty(9) ,imodbits_plate ],
["palace_guard_red", "Red Palace Guard Armor", [("palace_guard_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1059, weight(10.8)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(11)|difficulty(9) ,imodbits_plate ],
["heraldic_mail_with_tunic", "Heraldic Mail", [("heraldic_armor_new_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1089, weight(11.1)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(13)|difficulty(10) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_b", ":agent_no", ":troop_no")])]],

 
["saracen_lamellar_a", "Saracen Lamellar Cuirass", [("saracen_lamellar_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1124, weight(10.3)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(7)|difficulty(10) ,imodbits_armor ],
["haubergeon", "Haubergeon", [("haubergeon_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1169, weight(11.5)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(10) ,imodbits_armor ],
["sarranid_mail_shirt", "Saracen Mail Shirt", [("sarranian_mail_shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
1189, weight(12)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(15)|difficulty(10) ,imodbits_armor ],
["mail_with_surcoat", "Red Surcoat over Mail", [("mail_long_surcoat_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1219, weight(12.8)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(19)|difficulty(10) ,imodbits_armor ],
["surcoat_over_mail", "Green Surcoat over Mail", [("surcoat_over_mail_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1219, weight(12.8)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(19)|difficulty(10) ,imodbits_armor ],
["heraldic_mail_with_surcoat", "Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1219, weight(12.8)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(19)|difficulty(10) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],
["surcoat_over_mail_black", "Black Surcoat over Mail", [("new_som_black",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1219, weight(12.8)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(19)|difficulty(11) ,imodbits_armor ],
["surcoat_over_mail_blue", "Blue Surcoat over Mail", [("new_som_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1219, weight(12.8)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(19)|difficulty(11) ,imodbits_armor ],
["surcoat_over_mail_brown", "Brown Surcoat over Mail", [("new_som_brown",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1219, weight(12.8)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(19)|difficulty(11) ,imodbits_armor ],
["surcoat_over_mail_green", "Green Surcoat over Mail", [("new_som_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1219, weight(12.8)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(19)|difficulty(11) ,imodbits_armor ],
["surcoat_over_mail_purple", "Purple Surcoat over Mail", [("new_som_purple",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1219, weight(12.8)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(19)|difficulty(11) ,imodbits_armor ],
["surcoat_over_mail_red", "Red Surcoat over Mail", [("new_som_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1219, weight(12.8)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(19)|difficulty(11) ,imodbits_armor ],
["surcoat_over_mail_white", "White Surcoat over Mail", [("new_som_white",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1219, weight(12.8)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(19)|difficulty(11) ,imodbits_armor ],
["surcoat_over_mail_yellow", "Yellow Surcoat over Mail", [("new_som_yellow",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1219, weight(12.8)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(19)|difficulty(11) ,imodbits_armor ],
["surcoat_over_mail_heraldic", "Heraldic Surcoat over Mail", [("new_som_heraldic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1219, weight(12.8)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(19)|difficulty(11) ,imodbits_armor ,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_f", ":agent_no", ":troop_no")])]],

 
 
["archons_armor", "Archon's Armor", [("archons_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1261, weight(11.1)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(7)|difficulty(10) ,imodbits_plate ],
["heraldic_mail_with_tabard", "Heraldic Mail with Tabard", [("heraldic_armor_new_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1319, weight(12.2)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(13)|difficulty(10) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_d", ":agent_no", ":troop_no")])]],

["scale_mail", "Scale Mail", [("lamellar_armor_f",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1354, weight(12.2)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(10)|difficulty(11) ,imodbits_armor ],
["lithuanian_lamellar", "Lithuanian Lamellar", [("armor_18",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1380, weight(12.5)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(12)|difficulty(10) ,imodbits_armor ],
["kaftan_over_mail_a", "Black Kaftan over Mail", [("kaftan_black_over_mail",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1380, weight(12.6)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(12)|difficulty(10) ,imodbits_armor ],
["kaftan_over_mail_b", "Blue Kaftan over Mail", [("kaftan_blue_over_mail",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1380, weight(12.6)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(12)|difficulty(10) ,imodbits_armor ],
["kaftan_over_mail_c", "Red Kaftan over Mail", [("kaftan_red_over_mail",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1380, weight(12.6)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(12)|difficulty(10) ,imodbits_armor ],
["kaftan_over_mail_d", "White Kaftan over Mail", [("kaftan_white_over_mail",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1380, weight(12.6)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(12)|difficulty(10) ,imodbits_armor ],

["heraldic_mail_with_tunic_b", "Heraldic Mail", [("heraldic_armor_new_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1412, weight(12.6)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(9)|difficulty(10) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_c", ":agent_no", ":troop_no")])]],
["kuyak_a", "Light Kuyak", [("kuyak_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1447, weight(12.9)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(11)|difficulty(10) ,imodbits_armor ],

["studded_leather_coat", "Studded Leather over Mail", [("leather_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1462, weight(13.5)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(11)|difficulty(11) ,imodbits_armor ],
["black_studded_leather_mail", "Black Studded Leather over Mail", [("blackpadded3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1462, weight(13.5)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(11)|difficulty(11) ,imodbits_armor ],
["mongol_armor", "Mongolian Lamellar Robe", [("mongol_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1488, weight(13.9)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(13)|difficulty(11) ,imodbits_plate ],

["kuyak_b", "Heavy Kuyak", [("kuyak_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1523, weight(14.1)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(11)|difficulty(11) ,imodbits_armor ],
["lithuanian_ducal_armor", "Lithuanian Ducal Armor", [("armor_23",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1553, weight(14.3)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(13)|difficulty(11) ,imodbits_armor ],
["mamluke_mail", "Mamluke Mail", [("sarranid_elite_cavalary",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
1573, weight(15.9)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(12) ,imodbits_armor ],


["banded_armor_b", "Black Banded Armor", [("new_banded_armor_black",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1588, weight(15.5)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(13)|difficulty(12) ,imodbits_armor ],
["banded_armor", "Banded Armor", [("banded_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1599, weight(15.5)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["ritterbruder_armor", "Ritterbruder Armor", [("armor_35",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1608, weight(16.2)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(12) ,imodbits_armor ],
#NEW: was hard_lthr_a
["cuir_bouilli", "Cuir Bouilli", [("cuir_bouilli_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1608, weight(15.7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(12) ,imodbits_armor ],
["surcoa_over_mail_and_plate_black", "Black Surcoat over Mail and Plate", [("new_plated_som_black",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1608, weight(15.7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(12) ,imodbits_armor ],
["surcoa_over_mail_and_plate_blue", "Blue Surcoat over Mail and Plate", [("new_plated_som_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1608, weight(15.7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(12) ,imodbits_armor ],
["surcoa_over_mail_and_plate_brown", "Brown Surcoat over Mail and Plate", [("new_plated_som_brown",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1608, weight(15.7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(12) ,imodbits_armor ],
["surcoa_over_mail_and_plate_green", "Green Surcoat over Mail and Plate", [("new_plated_som_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1608, weight(15.7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(12) ,imodbits_armor ],
["surcoa_over_mail_and_plate_purple", "Purple Surcoat over Mail and Plate", [("new_plated_som_purple",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1608, weight(15.7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(12) ,imodbits_armor ],
["surcoa_over_mail_and_plate_red", "Red Surcoat over Mail and Plate", [("new_plated_som_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1608, weight(15.7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(12) ,imodbits_armor ],
["surcoa_over_mail_and_plate_white", "White Surcoat over Mail and Plate", [("new_plated_som_white",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1608, weight(15.7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(12) ,imodbits_armor ],
["surcoa_over_mail_and_plate_yellow", "Yellow Surcoat over Mail and Plate", [("new_plated_som_yellow",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1608, weight(15.7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(12) ,imodbits_armor ],
["surcoa_over_mail_and_plate_heraldic", "Heraldic Surcoat over Mail and Plate", [("new_plated_som_heraldic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1608, weight(15.7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(12) ,imodbits_armor ,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_g", ":agent_no", ":troop_no")])]],
["norman_armor_a", "Norman Double Mail", [("norman_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1633, weight(16.6)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(20)|difficulty(12) ,imodbits_plate ],
 
["arabian_armor_b", "Saracen Guard Armor", [("arabian_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1648, weight(14.5)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(7)|difficulty(12) ,imodbits_armor],
["brigandine_green_b", "Green Brigandine over Mail", [("brigandine_over_mail_new_green",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
1653, weight(15.7)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(13)|difficulty(12) ,imodbits_armor ],
["brigandine_red_b", "Red Brigandine over Mail", [("brigandine_red_mail",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
1653, weight(15.7)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(13)|difficulty(12) ,imodbits_armor ],
["brigandine_blue_a", "Blue Brigandine over Mail", [("brigandine_blue_mail",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
1653, weight(15.7)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(13)|difficulty(12) ,imodbits_armor ],
["brigandine_black_a", "Black Brigandine over Mail", [("brigandine_over_mail_black",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
1653, weight(15.7)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(13)|difficulty(12) ,imodbits_armor ],
["brigandine_brown_a", "Brown Brigandine over Mail", [("brigandine_over_mail_brown",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
1653, weight(15.7)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(13)|difficulty(12) ,imodbits_armor ],
["brigandine_purple_a", "Purple Brigandine over Mail", [("brigandine_over_mail_purple",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
1653, weight(15.7)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(13)|difficulty(12) ,imodbits_armor ],
["brigandine_white_a", "White Brigandine over Mail", [("brigandine_over_mail_white",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
1653, weight(15.7)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(13)|difficulty(12) ,imodbits_armor ],
["brigandine_yellow_a", "Yellow Brigandine over Mail", [("brigandine_over_mail_yellow",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
1653, weight(15.7)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(13)|difficulty(12) ,imodbits_armor ],
["brown_tabard_over_mail_and_plate", "Brown Tabard over Mail and Plate", [("dull_brown",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1678, weight(16.6)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(17)|difficulty(12) ,imodbits_plate ],
["grey_tabard_over_mail_and_plate", "Grey Tabard over Mail and Plate", [("grey_plate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1678, weight(16.6)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(17)|difficulty(12) ,imodbits_plate ],
["light_mail_and_plate", "Light Mail and Plate", [("light_mail_and_plate",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 
1678, weight(16.6)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(17)|difficulty(12) ,imodbits_armor ],

 
["brigandine_red", "Brigandine", [("brigandine_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
1688, weight(16.4)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(13)|difficulty(12) ,imodbits_armor ],
["heavy_gotland_armor", "Heavy Gotland Armor", [("heavy_gotland_merchant",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1688, weight(17.4)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(18)|difficulty(13) ,imodbits_plate ],

["serbian_lamellar_a", "Serbian Lamellar", [("serbian_lamellar",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1707, weight(16.4)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(10)|difficulty(12) ,imodbits_plate ],
["drz_lamellar_armor_a", "Brown Rus Lamellar Cuirass", [("rus_lamellar_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1715, weight(17)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(13)|difficulty(13) ,imodbits_armor ],
["drz_lamellar_armor_b", "Green Rus Lamellar Cuirass", [("rus_lamellar_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1715, weight(17)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(13)|difficulty(13) ,imodbits_armor ],
["lamellar_armor", "Lamellar Armor", [("lamellar_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1719, weight(17.2)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(14)|difficulty(13) ,imodbits_armor ],
["drz_lamellar_armor", "Druzhina Lamellar Armor", [("drz_lamellar_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1719, weight(17.2)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(14)|difficulty(13) ,imodbits_armor ],
["serbian_lamellar_b", "Serbian Lamellar with Knee Cops", [("serbian_lamellar_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1724, weight(17.7)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(13) ,imodbits_plate ],
["pronoia_armor", "Pronoia Armor", [("pronoia_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
1749, weight(18.8)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(21)|difficulty(14) ,imodbits_plate ],

 
 
 
#["blackwhite_surcoat", "Black and White Surcoat", [("surcoat_blackwhite",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 348 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["green_surcoat", "Green Surcoat", [("surcoat_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 348 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["blue_surcoat", "Blue Surcoat", [("surcoat_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 350 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["red_surcoat", "Red Surcoat", [("surcoat_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 350 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],


#["lamellar_cuirass", "Lamellar Cuirass", [("lamellar_armor",0)], itp_type_body_armor  |itp_covers_legs,0, 1020 , weight(25)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(15)|difficulty(9) ,imodbits_armor ],

#["black_armor", "Black Armor", [("black_armor",0)], itp_type_body_armor  |itp_covers_legs ,0,
# 9496 , weight(25)|abundance(100)|head_armor(0)|body_armor(57)|leg_armor(18)|difficulty(10) ,imodbits_plate ],



 
 




#################################### ARMORS

###### Heavy Armors  > 50

["rus_scale", "Rus Scale Armor", [("rus_scale",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2001, weight(18.1)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(15)|difficulty(13) ,imodbits_armor ],
["rus_scale_b", "Green Rus Scale Armor", [("rus_scale_h1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2001, weight(18.1)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(15)|difficulty(13) ,imodbits_armor ],
["rus_scale_c", "Blue Rus Scale Armor", [("rus_scale_h2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2001, weight(18.1)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(15)|difficulty(13) ,imodbits_armor ],
["rus_scale_d", "Red Rus Scale Armor", [("rus_scale_h3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2001, weight(18.1)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(15)|difficulty(13) ,imodbits_armor ],
["katafraktoi_armor", "Katafraktoi Armor", [("katafraktoi_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2021, weight(18.3)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(13) ,imodbits_plate ],
["coat_of_plates", "Black Coat of Plates", [("coat_of_plates_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2021, weight(19.3)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(19)|difficulty(14) ,imodbits_armor ],
["coat_of_plates_red", "Red Coat of Plates", [("coat_of_plates_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2021, weight(19.3)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(19)|difficulty(14) ,imodbits_armor ],
["coat_of_plates_blue", "Blue Coat of Plates", [("coat_of_plates_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2021, weight(19.3)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(19)|difficulty(14) ,imodbits_armor ],
["coat_of_plates_green", "Green Coat of Plates", [("coat_of_plates_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2021, weight(19.3)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(19)|difficulty(14) ,imodbits_armor ],
["sipahi_jawshan", "Sipahi Yawshan", [("sipahi_jawshan",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2021, weight(19)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(19)|difficulty(14) ,imodbits_plate ],
["plated_light_brigandine", "Plated Light Brigandine", [("merc_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2041, weight(19)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(14) ,imodbits_plate ],

 
["mail_and_plate", "Mail and Plate", [("mail_and_plate",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0,
2186, weight(19.7)|abundance(100)|head_armor(0)|body_armor(51)|leg_armor(19)|difficulty(14) ,imodbits_armor ],
["black_armor_b", "Black Armor", [("bnw_armour_slashed",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2256, weight(20.2)|abundance(100)|head_armor(0)|body_armor(51)|leg_armor(21)|difficulty(14) ,imodbits_plate ],
["black_armor_c", "Black Armor with Stripes", [("bnw_armour_stripes",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2256, weight(20.2)|abundance(100)|head_armor(0)|body_armor(51)|leg_armor(21)|difficulty(14) ,imodbits_plate ],
  
["khergit_guard_armor", "Mongolian Guard Armor", [("lamellar_armor_a",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 
2286, weight(20.9)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(21)|difficulty(15) ,imodbits_armor ],

##armors_e
["khergit_elite_armor", "Mongolian Elite Armor", [("lamellar_armor_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2323, weight(20.7)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(17)|difficulty(14) ,imodbits_armor ],
["vaegir_elite_armor", "Mongolian Elite Cavalry Armor", [("lamellar_armor_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2323, weight(20.7)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(17)|difficulty(14) ,imodbits_armor ],
["sarranid_elite_armor", "Saracen Elite Armor", [("tunic_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian ,0,
2323, weight(20.7)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(17)|difficulty(14) ,imodbits_armor ],
["corrazina_red", "Red Corrazina Armor", [("corrazina_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2348, weight(21.1)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(19)|difficulty(15) ,imodbits_plate ],
["corrazina_grey", "Grey Corrazina Armor", [("corrazina_grey",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2348, weight(21.1)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(19)|difficulty(15) ,imodbits_plate ],
["corrazina_green", "Green Corrazina Armor", [("corrazina_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2348, weight(21.1)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(19)|difficulty(15) ,imodbits_plate ],
["french_plate", "Fleur-de-lis Tunic over Plate", [("frenchplate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2348, weight(21.1)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(19)|difficulty(15) ,imodbits_plate ],

["drz_elite_lamellar_armor", "Druzhina Elite Lamellar Armor", [("drz_elite_lamellar_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2408, weight(21.4)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(17)|difficulty(15) ,imodbits_armor ],
["transitional_white", "White Transitional Armor with Surcoat", [("early_transitional_white",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2443, weight(21.9)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(19)|difficulty(15) ,imodbits_plate ],
["transitional_heraldic", "Heraldic Transitional Armor", [("early_transitional_heraldic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2443, weight(21.9)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(19)|difficulty(15) ,imodbits_plate, 
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_e", ":agent_no", ":troop_no")])]],
["transitional_blue", "Blue Transitional Armor with Surcoat", [("early_transitional_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2443, weight(21.9)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(19)|difficulty(15) ,imodbits_plate ],
["transitional_orange", "Orange Transitional Armor with Surcoat", [("early_transitional_orange",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2443, weight(21.9)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(19)|difficulty(15) ,imodbits_plate ],
["transitional_black", "Black Transistional Armour", [("platedtransditionalarmor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2443, weight(21.9)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(19)|difficulty(15) ,imodbits_plate ],
["polish_transitional_armor", "Polish Transistional Armour", [("polishplate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2443, weight(21.9)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(19)|difficulty(15) ,imodbits_plate, [], [fac_kingdom_1, fac_kingdom_2]],

["varangopoulos_armor", "Varangopoulos Armor", [("varangopoulos_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2493, weight(22.9)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(20)|difficulty(16) ,imodbits_plate ],
["heavy_yawshan", "Heavy Yawshan", [("heavy_yawshan",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2503, weight(23.1)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(21)|difficulty(16) ,imodbits_plate ],

 
["plate_armor", "Plate Armor", [("full_plate_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2618, weight(23.6)|abundance(100)|head_armor(0)|body_armor(56)|leg_armor(20)|difficulty(16) ,imodbits_plate ],
["churburg_a", "Blue Churburg Cuirass", [("churburg_13",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2618, weight(23.6)|abundance(100)|head_armor(0)|body_armor(56)|leg_armor(20)|difficulty(16) ,imodbits_plate ],
["churburg_b", "Red Churburg Cuirass", [("churburg_13_brass",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2618, weight(23.6)|abundance(100)|head_armor(0)|body_armor(56)|leg_armor(20)|difficulty(16) ,imodbits_plate ],
["churburg_c", "Churburg Cuirass", [("churburg_13_mail",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2618, weight(23.6)|abundance(100)|head_armor(0)|body_armor(56)|leg_armor(20)|difficulty(16) ,imodbits_plate ],
["churburg_d", "Ornamented Churburg Cuirass", [("new_churburg",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2643, weight(23.6)|abundance(100)|head_armor(0)|body_armor(56)|leg_armor(21)|difficulty(16) ,imodbits_plate ],

["gothic_armour_a", "Gothic Plate with Bevor", [("gothic_armour",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_covers_beard ,0,
3193, weight(27.9)|abundance(100)|head_armor(8)|body_armor(57)|leg_armor(21)|difficulty(18) ,imodbits_plate ],
["gothic_knightly_plate_a", "Gothic Knightly Plate", [("elite_gothic_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2843, weight(24.7)|abundance(100)|head_armor(0)|body_armor(57)|leg_armor(21)|difficulty(16) ,imodbits_plate ],
["gothic_knightly_plate_b", "Black Gothic Knightly_Plate", [("blacken_plate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2843, weight(24.7)|abundance(100)|head_armor(0)|body_armor(57)|leg_armor(21)|difficulty(16) ,imodbits_plate ],
["gothic_knightly_plate_c", "Bronze Gothic Knightly_Plate", [("bronzeknight",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2843, weight(24.7)|abundance(100)|head_armor(0)|body_armor(57)|leg_armor(21)|difficulty(16) ,imodbits_plate ],
["gothic_armour_b", "Gothic Plate", [("gothic_armour_nobevor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2843, weight(24.7)|abundance(100)|head_armor(0)|body_armor(57)|leg_armor(21)|difficulty(17) ,imodbits_plate ],
 
 
["plate_armor_b", "Plate Armor", [("plate_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
2993, weight(27)|abundance(100)|head_armor(0)|body_armor(58)|leg_armor(21)|difficulty(18) ,imodbits_plate ],
["plate_armor_c", "Heavy Plate Armor", [("new_horde_plate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
3002, weight(26)|abundance(100)|head_armor(0)|body_armor(58)|leg_armor(23)|difficulty(17) ,imodbits_plate ],

["heavy_gothic_armor_a", "Heavy Gothic Armor", [("variantarmor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
3102, weight(26.3)|abundance(100)|head_armor(0)|body_armor(59)|leg_armor(21)|difficulty(17) ,imodbits_plate ],
["heavy_gothic_armor_b", "Black Heavy Gothic Armor", [("variantarmorblack",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
3102, weight(26.3)|abundance(100)|head_armor(0)|body_armor(59)|leg_armor(21)|difficulty(17) ,imodbits_plate ],
["heavy_gothic_armor_c", "Bronze Heavy Gothic Armor", [("variantarmorbronze",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
3102, weight(26.3)|abundance(100)|head_armor(0)|body_armor(59)|leg_armor(21)|difficulty(17) ,imodbits_plate ],

["milanese_armour", "Milanese Plate", [("milanese_armour",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
3502, weight(27.9)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(24)|difficulty(18) ,imodbits_plate ],
 



#["tunic_over_mail_a", "Blue Tunic over Mail", [("tunic_over_mail_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 2758 , weight(11.1)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(13)|difficulty(10) ,imodbits_armor ],

#["tunic_over_mail_b", "Green Tunic over Mail", [("tunic_over_mail_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 2758 , weight(11.1)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(13)|difficulty(10) ,imodbits_armor ],

#["tunic_over_mail_c", "Red Tunic over Mail", [("tunic_over_mail_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 2758 , weight(11.1)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(13)|difficulty(10) ,imodbits_armor ],

#["tunic_over_mail_d", "White Tunic over Mail", [("tunic_over_mail_white",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 2758 , weight(11.1)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(13)|difficulty(10) ,imodbits_armor ],
 
#["tunic_over_mail_e", "Yellow Tunic over Mail", [("tunic_over_mail_yellow",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 2758 , weight(11.1)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(13)|difficulty(10) ,imodbits_armor ],
 
#["tunic_over_mail_f", "Heraldic Tunic over Mail", [("tunic_over_mail_heraldic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 1320 , weight(11.1)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(13)|difficulty(10) ,imodbits_armor,
#[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_f", ":agent_no", ":troop_no")])]],

 




 
 
 
 
 

 
["turret_hat_ruby", "Turret Hat", [("turret_hat_r",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 70 , weight(0.1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 
["turret_hat_blue", "Turret Hat", [("turret_hat_b",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 
["turret_hat_green", "Barbette", [("barbette_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,70, weight(0.1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["court_hat", "Turret Hat", [("court_hat",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 
["wimple_a", "Wimple", [("wimple_a_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.1)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["wimple_with_veil", "Wimple with Veil", [("wimple_b_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.1)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["woolen_hood", "Woolen Hood", [("woolen_hood",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["female_hood", "Lady's Hood", [("ladys_hood_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 9 , weight(0.2)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_lady_hat", "Mongolian Lady Hat", [("khergit_lady_hat",0)],  itp_type_head_armor   |itp_civilian |itp_doesnt_cover_hair | itp_fit_to_head,0, 1 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_lady_hat_b", "Mongolian Lady Leather Hat", [("khergit_lady_hat_b",0)], itp_type_head_armor  | itp_doesnt_cover_hair | itp_fit_to_head  |itp_civilian ,0, 1 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["crown", "Crown", [("crown",0)],  itp_type_head_armor  |itp_fit_to_head|itp_doesnt_cover_hair ,0, 
 4000 , weight(0.9)|abundance(100)|head_armor(1)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["crowned_helmet", "Crowned Helmet", [("crownedhelm",0)], itp_type_head_armor|itp_covers_beard ,0, 
 7000 , weight(3.1)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],


 
############################## 
###### LIGHT HELMETS 0 - 30
 ##############################

["ranger_hood", "Brown Hood", [("ranger_hood_brown",0),("ranger_hood_brown_inv",ixmesh_inventory)], 0| itp_type_head_armor |itp_civilian|itp_attach_armature  ,0, 
12, weight(0.2)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["straw_hat", "Straw Hat", [("straw_hat_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,
4, weight(0.1)|abundance(100)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["head_wrappings","Head Wrapping",[("head_wrapping",0)],itp_type_head_armor|itp_fit_to_head,0,
8, weight(0.1)|head_armor(4),imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick],
["headcloth", "Headcloth", [("headcloth_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
0, weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_hat", "Saracen Felt Hat", [("sar_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0,
8, weight(0.1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap", "Woolen Cap", [("woolen_cap_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
1, weight(0.1)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["arming_cap", "Arming Cap", [("arming_cap_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
2, weight(0.1)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["kazakh_hat", "Kazakht Hat", [("kazakh_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 
3, weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["felt_hat", "Felt Hat", [("felt_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0,
2, weight(0.1)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat_b", "Felt Hat", [("felt_hat_b_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0,
3, weight(0.1)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["fur_hat", "Fur Hat", [("fur_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0,
2, weight(0.1)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["common_hood", "Hood", [("hood_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,
4, weight(0.2)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_b", "Green Hood", [("hood_b",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,
4, weight(0.2)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_c", "Purple Hood", [("hood_c",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,
4, weight(0.2)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_d", "Blue Hood", [("hood_d",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,
4, weight(0.2)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["deli_cap", "Deli Cap", [("deli_cap",0)], itp_merchandise| itp_type_head_armor  |itp_fit_to_head ,0, 
4, weight(0.1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

 
["nomad_cap_b", "Nomad Cap", [("nomad_cap_b_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0,
3, weight(0.2)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["steppe_cap", "Steppe Cap", [("steppe_cap_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
7, weight(0.4)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["padded_coif", "Padded Coif", [("padded_coif_a_new",0)], itp_merchandise| itp_type_head_armor   ,0,
3, weight(0.2)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_cap", "Leather Cap", [("leather_cap_a_new",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0,
11, weight(0.2)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["pelt_hood", "Pelt Hood", [("pelt_hood",0)], 0| itp_type_head_armor |itp_civilian  ,0, 
12, weight(0.2)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["black_hood", "Black Hood", [("hood_black",0)], itp_type_head_armor|itp_merchandise   ,0, 
12, weight(0.2)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["turban", "Turban", [("tuareg_open",0)], itp_merchandise| itp_type_head_armor   ,0,
15, weight(0.2)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["turban_b", "Turban Hat", [("rw_turban",0)], 0| itp_type_head_armor |itp_civilian  ,0, 
21, weight(0.2)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_steppe_cap_a", "Steppe Cap", [("leather_steppe_cap_a_new",0)], itp_merchandise|itp_type_head_armor   ,0, 
21, weight(0.2)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["nordic_archer_helmet", "Nordic Leather Helmet", [("Helmet_A_vs2",0)], itp_merchandise| itp_type_head_armor    ,0,
28, weight(0.3)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
["desert_turban", "Desert Turban", [("tuareg",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard ,0,
28, weight(0.3)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_steppe_cap_b", "Steppe Cap ", [("tattered_steppe_cap_b_new",0)], itp_merchandise|itp_type_head_armor   ,0, 
28, weight(0.3)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["vaegir_fur_cap", "Cap with Fur", [("vaeg_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0,
32, weight(0.4)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
 
["leather_steppe_cap_c", "Steppe Cap", [("steppe_cap_a_new",0)], itp_merchandise|itp_type_head_armor   ,0,
38, weight(0.4)|abundance(100)|head_armor(17)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["leather_warrior_cap", "Leather Warrior Cap", [("skull_cap_new_b",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
42, weight(0.5)|abundance(100)|head_armor(19)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["shahi", "Saracen Turban Helm with Coif", [("shahi",0)], itp_type_head_armor|itp_merchandise   ,0, 
51, weight(1.6)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["sarranid_warrior_cap", "Saracen Warrior Cap", [("tuareg_helmet",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0,
51, weight(0.5)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ],
["nomad_cap", "Nomad Cap", [("nomad_cap_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0,
51, weight(0.5)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["skullcap", "Skullcap", [("skull_cap_new_a",0)], itp_merchandise| itp_type_head_armor   ,0,
51, weight(0.6)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
["nordic_veteran_archer_helmet", "Nordic Leather Helmet", [("Helmet_A",0)], itp_merchandise| itp_type_head_armor,0,
51, weight(0.6)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ],
["vaegir_fur_helmet", "Rus Fur Helmet", [("vaeg_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0,
51, weight(0.6)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

["mail_coif", "Mail Coif", [("mail_coif_new",0)], itp_merchandise| itp_type_head_armor   ,0,
66, weight(0.7)|abundance(100)|head_armor(23)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor ],
["mail_coif_b", "Dark Mail Coif", [("coif",0)], itp_merchandise| itp_type_head_armor|itp_covers_beard   ,0, 
66, weight(0.7)|abundance(100)|head_armor(23)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_armor ],
["mail_coif_c", "Dark Mail Coif", [("balaclavacoif",0)], itp_merchandise| itp_type_head_armor|itp_covers_beard  ,0, 
66, weight(0.7)|abundance(100)|head_armor(23)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_armor ],

["footman_helmet", "Footman's Helmet", [("skull_cap_new",0)], itp_merchandise| itp_type_head_armor   ,0,
83, weight(0.8)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

["sarranid_horseman_helmet", "Horseman Helmet", [("sar_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0,
100, weight(0.9)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["saracen_helmet_a", "Saracen Helmet", [("saracen_helmet_a",0)], itp_merchandise| itp_type_head_armor   ,0, 
100, weight(1.3)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 
 #missing...
["nasal_helmet", "Nasal Helmet", [("nasal_helmet_b",0)], itp_merchandise| itp_type_head_armor   ,0,
134, weight(0.9)|abundance(100)|head_armor(27)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["solak_helmet_a", "Solak Helmet", [("solak_helmet_A",0)], itp_merchandise| itp_type_head_armor  |itp_fit_to_head ,0, 
134, weight(0.9)|abundance(100)|head_armor(27)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["solak_helmet_b", "Crested Solak Helmet", [("solak_helmet_B",0)], itp_merchandise| itp_type_head_armor  |itp_fit_to_head ,0, 
147, weight(1)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(3) ,imodbits_cloth ],
["solak_helmet_c", "Crested Solak Helmet with Plume", [("solak_helmet_C",0)], itp_merchandise| itp_type_head_armor  |itp_fit_to_head ,0, 
147, weight(1)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(3) ,imodbits_cloth ],

 
["norman_helmet", "Helmet with Cap", [("norman_helmet_a",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
157, weight(1.1)|abundance(100)|head_armor(29)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["janissary_boerk_a", "Boerk", [("janissary_boerk_A",0)], itp_merchandise| itp_type_head_armor  |itp_fit_to_head ,0, 
157, weight(1.1)|abundance(100)|head_armor(29)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ],

["janissary_boerk_b", "Crested Boerk", [("janissary_boerk_B",0)], itp_merchandise| itp_type_head_armor  |itp_fit_to_head ,0, 
180, weight(1.1)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ],
["janissary_boerk_c", "Crested Boerk with Plume", [("janissary_boerk_C",0)], itp_merchandise| itp_type_head_armor  |itp_fit_to_head ,0, 
180, weight(1.1)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ],


############################## 
###### MEDIUM HELMETS 31 - 50
############################## 
 
["nordic_footman_helmet", "Nordic Footman Helmet", [("Helmet_B_vs2",0)], itp_merchandise| itp_type_head_armor |itp_fit_to_head ,0,
251, weight(1.2)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["segmented_helmet_b", "Segmented Helmet With Padded Coif", [("new_segmented_helm_new",0),("new_segmented_helm_new_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 
251, weight(1.25)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["magyar_helmet_a", "Magyar Helmet", [("magyar_helmet_a",0)], itp_type_head_armor|itp_merchandise   ,0, 
251, weight(1.2)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["rabati", "Rabati", [("rabati",0)], itp_type_head_armor|itp_merchandise   ,0, 
251, weight(1.2)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["mail_coif_d", "Dark Full Face Mail Coif", [("fullfacecoif",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard   ,0, 
275, weight(1.3)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor ],
["segmented_helmet", "Segmented Helmet", [("segmented_helm_new",0)], itp_merchandise| itp_type_head_armor   ,0,
275, weight(1.3)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],

["helmet_with_neckguard", "Helmet with Neckguard", [("neckguard_helm_new",0)], itp_merchandise| itp_type_head_armor   ,0, 
301, weight(1.3)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["vaegir_spiked_helmet", "Spiked Cap", [("vaeg_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0,
301, weight(1.3)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["chapel_de_fer_e", "Kettle Hat with Padded Coif", [("chapel-de-fer_cloth2",0),("inv_chapel-de-fer_cloth2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
301, weight(1.3)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["chapel_de_fer_f", "Chapel de Fer with Padded Coif", [("chapel-de-fer_cloth3",0),("inv_chapel-de-fer_cloth3",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
301, weight(1.3)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["kettle_hat_i", "Black Kettle Hat with Padded Coif", [("luxurious_chapel-de-fer_cloth2",0),("luxurious_chapel-de-fer_cloth2_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
301, weight(1.3)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["flat_topped_helmet_b", "Flat Topped Helmet", [("new_flattop_helmet_new",0),("new_flattop_helmet_new_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature|itp_fit_to_head   ,0, 
301, weight(1.75)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["khergit_helmet", "Mongolian Helmet", [("khergit_guard_helmet",0)], itp_type_head_armor|itp_merchandise   ,0, 
329, weight(1.4)|difficulty(7)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["flat_topped_helmet", "Flat Topped Helmet", [("flattop_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0, 
329, weight(1.4)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["chapel_de_fer_d", "Iron Hat with Padded Coif", [("chapel-de-fer_cloth1",0),("inv_chapel-de-fer_cloth1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
329, weight(1.4)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["kettle_hat_h", "Black Iron Hat with Padded Coif", [("luxurious_chapel-de-fer_cloth1",0),("luxurious_chapel-de-fer_cloth1_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
329, weight(1.4)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["kettle_hat_j", "Black Chapel de Fer with Padded Coif", [("luxurious_chapel-de-fer_cloth3",0),("luxurious_chapel-de-fer_cloth3_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
329, weight(1.4)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["neckguard_helm_new_b", "Helmet With Padded Coif", [("new_neckguard_helm_new",0),("new_neckguard_helm_new_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature|itp_fit_to_head,0,
329, weight(1.4)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],

["khergit_war_helmet", "Mongolian War Helmet", [("tattered_steppe_cap_a_new",0)], itp_type_head_armor | itp_merchandise   ,0, 
389, weight(1.5)|difficulty(8)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["nordic_fighter_helmet", "Nordic Fighter Helmet", [("Helmet_B",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
389, weight(1.5)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["kettle_hat_e", "Blue Kettle Helmet", [("col1_kettlehat2",0)], itp_merchandise| itp_type_head_armor|itp_covers_beard,0, 
389, weight(1.7)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["skullcap_c", "Iron Skull Cap", [("new_skull_cap_metal",0),("new_skull_cap_metal_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 
389, weight(1.5)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["skullcap_d", "Black Iron Skull Cap", [("new_skull_cap_blk",0),("new_skull_cap_blk_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 
389, weight(1.5)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["skullcap_e", "White Iron Skull Cap", [("new_skull_cap_wit",0),("new_skull_cap_wit_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 
389, weight(1.5)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["skullcap_g", "Blue Iron Skull Cap", [("new_skull_cap_blu",0),("new_skull_cap_blue_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 
389, weight(1.5)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["sarranid_helmet1", "Saracen Keffiyeh Helmet", [("sar_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0,
434, weight(1.6)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["kettle_hat", "Kettle Hat", [("kettle_hat_new",0)], itp_merchandise| itp_type_head_armor,0, 
434, weight(1.6)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["sipahi_helmet_a", "Sipahi Helmet", [("sipahi_helmet_a",0)], itp_type_head_armor|itp_merchandise   ,0, 
434, weight(1.6)|difficulty(9)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["conichelm", "Conic Helmet", [("conichelm",0)], itp_merchandise| itp_type_head_armor|itp_covers_beard   ,0, 
460, weight(1.9)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_armor ],
["kettle_hat_g", "Kettle Helmet", [("prato_chapel-de-fer",0)], itp_merchandise| itp_type_head_armor|itp_covers_beard,0,
460, weight(1.6)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["khergit_cavalry_helmet", "Mongolian Cavalry Helmet", [("lamellar_helmet_b",0)], itp_type_head_armor | itp_merchandise   ,0, 
460, weight(1.6)|difficulty(8)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["kettle_hat_b", "Kettle Hat", [("kettlehat1",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard,0, 
490, weight(1.7)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["kettle_hat_c", "Kettle Hat", [("kettlehat2",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard,0, 
490, weight(1.7)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["kettle_hat_d", "Broad Brimmed Kettle Helmet", [("col1_kettlehat1",0)], itp_merchandise| itp_type_head_armor|itp_covers_beard,0, 
490, weight(1.7)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["kettle_hat_f", "Blue Kettle Hat", [("kettlehatfacebyrnie",0)], itp_merchandise| itp_type_head_armor| itp_covers_beard,0, 
490, weight(1.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["pepperpot_helmet_f", "Blue Flat Topped Helmet", [("flattophelmet",0)], itp_merchandise| itp_type_head_armor|itp_covers_beard,0,
490, weight(1.7)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["saracen_helmet_c", "Saracen Helmet with Long Turban", [("saracen_helmet_c",0)], itp_merchandise| itp_type_head_armor,0, 
490, weight(1.7)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

 
["spiked_helmet", "Spiked Helmet", [("spiked_helmet_new",0)], itp_merchandise| itp_type_head_armor,0,
525, weight(1.8)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["nordic_helmet", "Nordic Helmet", [("helmet_w_eyeguard_new",0)], itp_merchandise| itp_type_head_armor   ,0,
525, weight(1.8)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["vaegir_lamellar_helmet", "Helmet with Lamellar Guard", [("vaeg_helmet4",0)], itp_merchandise| itp_type_head_armor,0,
525, weight(1.8)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["nasal_helmet_c", "Nasal Helmet With Aventail", [("nasal_helmet_with_aventail",0),("nasal_helmet_with_aventail_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature,0, 
525, weight(2.1)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["byzantion_helmet_d", "Roman Helmet", [("byzantine_helmet_a_inv",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_beard,0, 
525, weight(1.8)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["byzantion_helmet_e", "Red Roman Helmet", [("byzantine_helmet_a_red_inv",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_beard,0, 
525, weight(1.8)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["ghulam_helmet_a", "Ghulam Helmet with Coif", [("ghulam_helmet_a",0)], itp_merchandise| itp_type_head_armor,0, 
556, weight(1.9)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["phrygian_helmet", "Phrygian Helmet", [("phirgian_helmet_a_inv",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_beard,0, 
556, weight(1.8)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["nordic_huscarl_helmet", "Nordic Huscarl's Helmet", [("Helmet_C_vs2",0)], itp_merchandise| itp_type_head_armor,0,
591, weight(2)|abundance(100)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["rus_helmet_b", "Rus Helmet", [("rus_helm",0),("inv_rus_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature,0,
591, weight(2)|abundance(100)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["helmet_a", " Helmet With Aventail", [("new_reinf_helmet",0),("new_reinf_helmet_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature,0,
591, weight(1.9)|abundance(100)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["khergit_guard_helmet", "Mongolian Guard Helmet", [("lamellar_helmet_a",0)], itp_type_head_armor |itp_merchandise,0,
591, weight(2)|difficulty(9)|abundance(100)|head_armor(41)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["sarranid_mail_coif", "Saracen Mail Coif", [("tuareg_helmet2",0)], itp_merchandise| itp_type_head_armor ,0,
628, weight(2.1)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["chapel_de_fer_c", "Chapel de Fer with Aventail", [("chapel-de-fer_mail3",0),("inv_chapel-de-fer_mail3",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
628, weight(2.1)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["golden_horde_helmet", "Golden Horde Helmet", [("mongolian_helmet_inv",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head,0, 
628, weight(2.1)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],

["chapel_de_fer_b", "Kettle Hat with Aventail", [("chapel-de-fer_mail2",0),("inv_chapel-de-fer_mail2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_fit_to_head|itp_attach_armature,0,
688, weight(2.1)|abundance(100)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["byzantion_helmet_f", "Roman Helmet with Veil", [("byzantine_helmet_b_inv",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_beard,0, 
688, weight(2.1)|abundance(100)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["byzantion_helmet_g", "Red Roman Helmet with Veil", [("byzantine_helmet_b_red_inv",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_beard,0, 
688, weight(2.1)|abundance(100)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["saracen_helmet_b", "Saracen Helmet with Coif", [("turban_helmet_b",0),("turban_helmet_b_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_attach_armature,0, 
688, weight(2.1)|abundance(100)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
  
["norman_helmet_b", "Nordic Pot Helmet", [("normanhelmbalaclavacoif",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_beard ,0, 
718, weight(2.2)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["norman_helmet_c", "Nordic Pot Helmet", [("normanhelmcoif",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_beard ,0, 
718, weight(2.2)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["chapel_de_fer_a", "Iron Hat with Aventail", [("chapel-de-fer_mail1",0),("inv_chapel-de-fer_mail1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_fit_to_head|itp_attach_armature,0,
718, weight(2.2)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["varangian_helmet", "Fluted Varangian Helmet", [("eng_varangian_helmet_inv",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_beard,0, 
718, weight(2.2)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["skutatos_helmet", "Skutatos Helmet", [("skutatos_helmet_inv",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_beard,0, 
718, weight(1.9)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["lithuanian_helmet", "Lithuanian Helmet", [("helmet_4",0)], itp_merchandise| itp_type_head_armor,0,
753, weight(2.3)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["norman_helmet_d", "Nordic Conical Helmet", [("normanhelmfullcoif",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_beard ,0, 
753, weight(2.3)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["bascinet", "Bascinet", [("bascinet_avt_new",0)], itp_merchandise|itp_type_head_armor,0, 
753, weight(2.3)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["bascinet_4", "Onion Top Bascinet", [("onion-top_bascinet",0)], itp_merchandise| itp_type_head_armor|itp_covers_beard,0,
753, weight(2.3)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["clibanarius_helmet", "Clibanarius Helmet", [("clibanarius_helmet_inv",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_beard,0, 
753, weight(2.3)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],

["bascinet_2", "Bascinet with Aventail", [("bascinet_new_a",0)], itp_merchandise|itp_type_head_armor,0, 
799, weight(2.4)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["vaegir_noble_helmet", "Rus Nobleman Helmet", [("vaeg_helmet7",0)], itp_merchandise| itp_type_head_armor,0,
799, weight(2.4)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["tagancha_helmet_a", "Tagancha Helm", [("tagancha_helm_a",0),("inv_tagancha_helm_a",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature,0,
799, weight(2.4)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["pronoia_helmet", "Pronoia Helmet", [("pronoia_helmet_inv",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_beard,0, 
799, weight(2.4)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],

["bascinet_3", "Bascinet with Nose Guard", [("bascinet_new_b",0)], itp_merchandise|itp_type_head_armor,0,
837, weight(2.5)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["ottoman_chichak", "Chichak", [("ottoman_chichak",0)], itp_merchandise|itp_type_head_armor,0, 
837, weight(2.5)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["morion_b", "Blue Morion", [("combed_morion_blued",0)], itp_merchandise| itp_type_head_armor,0,
837, weight(2.5)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["gnezdovo_helmet", "Gnezdovo Helmet", [("gnezdovo_helm_a",0),("inv_gnezdovo_helm_a",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
837, weight(2.5)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
 
["guard_helmet", "Guard Helmet", [("reinf_helmet_new",0)], itp_merchandise| itp_type_head_armor,0,
891, weight(2.6)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["ottoman_elite_cavalry_chichak", "Elite Cavalry Chichak", [("ottoman_elite_cavalry_chichak",0)], itp_merchandise| itp_type_head_armor,0, 
891, weight(2.6)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["zitta_bascinet_b", "Zitta Bascinet", [("zitta_bascinet_novisor",0),("inv_zitta_bascinet_novisor",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_fit_to_head|itp_attach_armature,0,
891, weight(2.6)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["chapel_de_fer_g", "Chapel de Fer", [("chapel_de_fer",0)], itp_merchandise| itp_type_head_armor,0,
891, weight(2.6)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["novogrod_helmet", "Novgorod Helm", [("novogrod_helm",0),("inv_novogrod_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
891, weight(2.6)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["saracen_helmet_d", "Saracen Helmet with Veil", [("turban_helmet_new",0),("turban_helmet_new_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_beard|itp_attach_armature,0, 
891, weight(2.6)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],

["tagancha_helmet_b", "Tagancha Helm with Veil", [("tagancha_helm_b",0),("inv_tagancha_helm_b",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
891, weight(2.6)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["vaegir_war_helmet", "Rus War Helmet", [("vaeg_helmet6",0)], itp_merchandise| itp_type_head_armor   ,0,
891, weight(2.6)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["sarranid_veiled_helmet", "Saracen Veiled Helmet", [("sar_helmet4",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0,
891, weight(2.6)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],

["nordic_warlord_helmet", "Nordic Warlord Helmet", [("Helmet_C",0)], itp_merchandise| itp_type_head_armor ,0,
935, weight(2.7)|abundance(100)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["byzantion_helmet", "Byzantion Helmet", [("brimmed_helmet_a",0),("brimmed_helmet_a_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor |itp_covers_beard|itp_attach_armature ,0, 
935, weight(2.7)|abundance(100)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["byzantion_helmet_b", "Byzantion Helmet", [("byzantion",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0, 
935, weight(2.7)|abundance(100)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["byzantion_helmet_c", "Veiled Byzantion Helmet", [("col1_byzantion",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0, 
935, weight(2.7)|abundance(100)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["gjermundbu_helmet", "Gjermundbu Helmet", [("chieftainhelm",0)], itp_merchandise| itp_type_head_armor ,0, 
935, weight(2.7)|abundance(100)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["open_sallet", "Open Sallet", [("open_sallet",0)], itp_merchandise| itp_type_head_armor,0,
935, weight(2.7)|abundance(100)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["nikolskoe_helmet", "Nikolskoe Helm", [("nikolskoe_helm",0),("inv_nikolskoe_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
935, weight(2.7)|abundance(100)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["byzantion_helmet_h", "Byzantion Helmet", [("brimmed_helmet_b",0),("brimmed_helmet_b_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_beard|itp_attach_armature,0, 
935, weight(2.7)|abundance(100)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
 

 
############################## 
###### HEAVY HELMETS >= 50
############################## 
 
["pepperpot_helmet_e", "French Pepperpot", [("new_frenchpepperpot",0),("frenchpepperpot",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
1022, weight(2.8)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["morion_a", "Morion", [("combed_morion",0)], itp_merchandise| itp_type_head_armor,0,
1022, weight(2.8)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],

["vaegir_mask", "Rus War Mask", [("vaeg_helmet9",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
1057, weight(3.1)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["barbuta_1", "Barbuta", [("barbuta1",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head,0, 
1057, weight(2.9)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["barbuta_2", "Barbutte", [("barbuta2",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head,0, 
1057, weight(2.9)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["munitions_pot_helmet", "Munitions Pot Helmet", [("new_munitionshelm2",0),("munitionshelm2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
1057, weight(2.9)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["pepperpot_helmet_b", "Pepperpot Helm", [("new_pepperpothelm1",0),("pepperpothelm1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
1057, weight(2.9)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["pepperpot_helmet_c", "Phrygian Helmet with Faceplate", [("mediterranean_helmet",0),("mediterranean_helmet_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
1057, weight(2.8)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["pepperpot_helmet_d", "Munitions Pot Helmet", [("new_munitionshelm1",0),("munitionshelm1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
1057, weight(2.9)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["black_helmet", "Black Helmet", [("black_helm",0)], itp_type_head_armor,0,
1057, weight(2.9)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["open_sallet_coif", "Open Sallet with Coif", [("open_sallet_coif",0)], itp_merchandise| itp_type_head_armor|itp_covers_beard,0,
1057, weight(2.9)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["open_sallet_b", "Open Sallet With Aventail", [("new_open_sallet",0),("new_open_sallet_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature,0,
1057, weight(3.2)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],

["zitta_bascinet", "Zitta Bascinet with Faceplate",  [("zitta_bascinet",0),("inv_zitta_bascinet_closedvisor",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_attach_armature,0,
1120, weight(3)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["full_helm", "Full Helm", [("great_helmet_new_b",0)], itp_merchandise| itp_type_head_armor |itp_covers_head ,0,
1120, weight(3)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["varangopoulos_bascinet", "Varangopoulos Bascinet", [("varangopoulos_bascinet_inv",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_beard,0, 
1120, weight(3)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["norman_pot_helmet", "Norman Pot Helmet with Faceplate", [("pot_helm_a_inv",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head|itp_covers_beard,0, 
1120, weight(3)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],

["klappvisier", "Klappvisier", [("klappvisier",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1187, weight(3.1)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["black_helmet_b", "Black Helmet", [("sturmhaube_5BW",0)], itp_merchandise| itp_type_head_armor|itp_covers_beard,0,
1187, weight(3.1)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["pigface_klappvisier", "Pigface Klappvisier", [("pigface_klappvisor",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0,
1187, weight(3.1)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["crusader_face_plate_a", "Crusader Face Plate", [("crusader_face_plate",0),("crusader_face_plate_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_attach_armature ,0, 
1187, weight(3.1)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["crusader_face_plate_b", "Black Crusader Face Plate", [("crusader_face_plate_blk",0),("crusader_face_plate_blk_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_attach_armature ,0, 
1187, weight(3.1)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["crusader_face_plate_c", "White Crusader Face Plate", [("crusader_face_plate_wit",0),("crusader_face_plate_wit_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_attach_armature ,0, 
1187, weight(3.1)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["crusader_face_plate_e", "Blue Crusader Face Plate", [("crusader_face_plate_blu",0),("crusader_face_plate_blu_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_attach_armature ,0, 
1187, weight(3.1)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],

["great_helmet", "Great Helmet", [("great_helmet_new",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0,
1218, weight(3.2)|abundance(100)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["french_pepperpot_helmet", "French Pepperpot Helm", [("new_frenchpepperpot2",0),("frenchpepperpot2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
1218, weight(3.2)|abundance(100)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["french_pepperpot_helmet_b", "French Pepperpot Helm", [("new_frenchpepperpot3",0),("frenchpepperpot3",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
1218, weight(3.2)|abundance(100)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["litchina_helmet", "Litchina Helm", [("litchina_helm",0),("inv_litchina_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_beard|itp_attach_armature,0,
1218, weight(3.2)|abundance(100)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],

["great_helmet_b", "Great Helmet with Hat", [("greathelmwhat",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285,weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["great_helmet_c", "Great Helmet", [("bolzanobucket",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["great_helmet_d", "Orange Great Helmet", [("col1_bolzanobucket",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["great_helmet_e", "Red Great Helmet", [("col2_bolzanobucket",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["crusader_helmet_a", "Crusader Helmet", [("crusaderbucket1",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["crusader_helmet_b", "Crusader Helmet", [("crusaderbucket2",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["gotland_helmet", "Gotland Helmet", [("gotlandbucket",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["topfhelm", "Topfhelm", [("madelnbucket1",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["topfhelm_b", "Rounded Topfhelm", [("madelnbucket2",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["great_helmet_f", "Red Great Helmet", [("col2_crusaderbucket1",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["great_helmet_g", "Red Great Helmet", [("col2_crusaderbucket2",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["gotland_helmet_b", "Red Gotland Helmet", [("col2_gotlandbucket",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["topfhelm_c", "Red Topfhelm Helmet", [("col2_madelnbucket1",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["topfhelm_d", "Rounded Topfhelm Helmet", [("col2_madelnbucket2",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["great_helmet_h", "Blue Great Helmet", [("col1_crusaderbucket1",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["great_helmet_i", "Blue Great Helmet", [("col1_crusaderbucket2",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["gotland_helmet_c", "Red Gotland Helmet", [("col1_gotlandbucket",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["topfhelm_e", "Red Topfhelm Helmet", [("col1_madelnbucket1",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0,
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["topfhelm_f", "Orange Rounded Topfhelm Helmet", [("col1_madelnbucket2",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1285, weight(3.3)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
 
["sugarloaf_a", "Sugarloaf Helmet", [("sugarloaf",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0,
1330, weight(3.4)|abundance(100)|head_armor(56)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["winged_great_helmet", "Winged Great Helmet", [("maciejowski_helmet_new",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0,
1330, weight(3.4)|abundance(100)|head_armor(56)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],
["sugarloaf_c", "Ornamented Sugarloaf Helmet", [("inv_new_sugarloaf",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0,
1330, weight(3.4)|abundance(100)|head_armor(56)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],

["great_helmet_k", "Great Helmet With Coif", [("great_helm_new_jarold",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1375, weight(3.5)|abundance(100)|head_armor(57)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_plate ],
["hounskull", "Houndskull Bascinet", [("hounskull",0)], itp_merchandise| itp_type_head_armor|itp_covers_beard,0,
1375, weight(3.5)|abundance(100)|head_armor(57)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_plate ],
["sugarloaf_b", "Sugarloaf Helmet with Coif", [("sugarloaf_coif",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0,
1375, weight(3.5)|abundance(100)|head_armor(57)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_plate ],

["great_bascinet_a", "Great Bascinet", [("greatbascinet1",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1402, weight(3.7)|abundance(100)|head_armor(58)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_plate ],
["great_helmet_j", "Great Helmet", [("greathelm1",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0,
1402, weight(3.7)|abundance(100)|head_armor(58)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_plate ],
["horned_great_elmet", "Horned Great Helmet", [("maciejowski_helmet_new_jarold",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1402, weight(3.7)|abundance(100)|head_armor(58)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_plate ],
["visored_sallet", "Sallet with Visor", [("visored_sallet",0)], itp_merchandise| itp_type_head_armor,0,
1402, weight(3.7)|abundance(100)|head_armor(58)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_plate ],

 
["milanese_sallet", "Milanese Sallet", [("milanese_sallet",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1449, weight(3.8)|abundance(100)|head_armor(59)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_plate ],
["visored_sallet_coif", "Sallet with Visor And Coif", [("visored_sallet_coif",0)], itp_merchandise| itp_type_head_armor|itp_covers_beard,0,
1449, weight(3.8)|abundance(100)|head_armor(59)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_plate ],
["visored_sallet_with_coif_a", "Visored Sallet with Coif", [("gothicknighthelm",0)], itp_merchandise| itp_type_head_armor|itp_covers_beard ,0, 
1449, weight(3.8)|abundance(100)|head_armor(59)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_plate ],
["visored_sallet_with_coif_b", "Black Visored Sallet with Coif", [("blacken_helm",0)], itp_merchandise| itp_type_head_armor|itp_covers_beard ,0, 
1449, weight(3.8)|abundance(100)|head_armor(59)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_plate ],
["visored_sallet_with_coif_c", "Bronze Visored Sallet with Coif", [("bronzekngihthelm",0)], itp_merchandise| itp_type_head_armor|itp_covers_beard ,0, 
1449, weight(3.8)|abundance(100)|head_armor(59)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_plate ],

["armet", "Armet", [("flemish_armet",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 
1506, weight(3.9)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_plate ],
["heavy_gothic_helmet_a", "Heavy Gothic Helm", [("variantknighthelm",0)], itp_merchandise| itp_type_head_armor|itp_covers_head ,0, 
1510, weight(3.9)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_plate ],
["heavy_gothic_helmet_b", "Black Heavy Gothic Helm", [("varianthelmblack",0)], itp_merchandise| itp_type_head_armor|itp_covers_head ,0, 
1510, weight(3.9)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_plate ],
["heavy_gothic_helmet_c", "Bronze Heavy Gothic Helm", [("varianthelmbronze",0)], itp_merchandise| itp_type_head_armor|itp_covers_head ,0, 
1510, weight(3.9)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_plate ],
["weimar_helmet", "Weimar Helmet", [("weimarhelm",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0,
1525, weight(4)|abundance(100)|head_armor(61)|body_armor(0)|leg_armor(0)|difficulty(14) ,imodbits_plate ],

#TODO:
#["skullcap_b", "Skullcap_b", [("skull_cap_new_b",0)], itp_merchandise| itp_type_head_armor   ,0, 71 , weight(1.5)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],

#["plainhelm", "Plainhelm", [("plainhelm",0)], itp_merchandise| itp_type_head_armor  ,0, 
#1723 , weight(1.3)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ],

#["pointyhelm", "Pointyhelm", [("pointyhelm",0)], itp_merchandise| itp_type_head_armor  ,0, 
#1723 , weight(1.3)|abundance(100)|head_armor(34)|body_armor(0)|difficulty(7) ,imodbits_plate ],

##["green_felt_hat", "Green Felt Hat", [("green_felt_hat",0)],  itp_type_head_armor |itp_civilian,0, 
##123 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],


#["skullcap_f", "Gold Iron Skull Cap", [("new_skull_cap_gold",0),("new_skull_cap_gold_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 
#1742 , weight(1.5)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],


#["skullcap_h", "Red Iron Skull Cap", [("new_skull_cap_red",0),("new_skull_cap_red_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 
#1742 , weight(1.5)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],



#["crusader_face_plate_d", "Gold Crusader Face Plate", [("crusader_face_plate_gold",0),("crusader_face_plate_gold_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_attach_armature ,0, 
# 2641 , weight(3.1)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],


#["crusader_face_plate_f", "Red Crusader Face Plate", [("crusader_face_plate_red",0),("crusader_face_plate_red_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_attach_armature ,0, 
# 2641 , weight(3.1)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],


#["barbuta_3", "Hooded Barbuta", [("hooded_barbuta_inv",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head,0, 
# 2754 , weight(3.1)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],

#["nasal_helmet_d", "Hooded Nasal Helmet", [("hooded_nasal_helmet_inv",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head,0, 
# 1576 , weight(3.1)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],


#["pelt_hood_cz", "Donkey Hood", [("pelt_hood_cz",0)], 0| itp_type_head_armor |itp_civilian|itp_covers_head  ,0, 
# 532 , weight(0.2)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],


#WEAPONS

######################### ######################### ######################### 
######################### 1H SWORDS					######################### 
######################### ######################### ######################### 
["sword_medieval_a", "Sword", [("sword_medieval_a",0),("sword_medieval_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
160, weight(1.4)|difficulty(7)|spd_rtng(101) | weapon_length(95)|swing_damage(27 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],
#["sword_medieval_a_long", "Sword", [("sword_medieval_a_long",0),("sword_medieval_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 156 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(105)|swing_damage(25 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
["sword_medieval_b", "Sword", [("sword_medieval_b",0),("sword_medieval_b_scabbard", ixmesh_carry),("sword_rusty_a",imodbit_rusty),("sword_rusty_a_scabbard", ixmesh_carry|imodbit_rusty)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
277, weight(1.4)|difficulty(7)|spd_rtng(100) | weapon_length(95)|swing_damage(28 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["sword_medieval_b_small", "Short Sword", [("sword_medieval_b_small",0),("sword_medieval_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
171, weight(1)|difficulty(6)|spd_rtng(103) | weapon_length(81)|swing_damage(26, cut) | thrust_damage(25, pierce),imodbits_sword_high ],
["sword_medieval_c", "Arming Sword", [("sword_medieval_c",0),("sword_medieval_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
489, weight(1.4)|difficulty(7)|spd_rtng(99) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
["sword_medieval_c_small", "Short Arming Sword", [("sword_medieval_c_small",0),("sword_medieval_c_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
378, weight(1)|difficulty(6)|spd_rtng(102) | weapon_length(81)|swing_damage(28, cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
["sword_medieval_c_long", "Long Arming Sword", [("sword_medieval_c_long",0),("sword_medieval_c_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
606, weight(1.7)|difficulty(8)|spd_rtng(98) | weapon_length(102)|swing_damage(30 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],
["sword_medieval_d_long", "Knightly Arming Sword", [("sword_medieval_d_long",0),("sword_medieval_d_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
747, weight(1.7)|difficulty(8)|spd_rtng(97) | weapon_length(102)|swing_damage(31 , cut) | thrust_damage(25 ,  pierce),imodbits_sword ],

["sword_viking_1", "Nordic Sword", [("sword_viking_c",0),("sword_viking_c_scabbard ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
170, weight(1.5)|difficulty(8)|spd_rtng(101) | weapon_length(94)|swing_damage(28 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ] ,
["sword_viking_2", "Nordic Sword", [("sword_viking_b",0),("sword_viking_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
376, weight(1.5)|difficulty(8)|spd_rtng(100) | weapon_length(94)|swing_damage(29 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],
["sword_viking_2_small", "Nordic Short Sword", [("sword_viking_b_small",0),("sword_viking_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
271, weight(1.1)|difficulty(7)|spd_rtng(103) | weapon_length(81)|swing_damage(28 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["sword_viking_3", "Nordic War Sword", [("sword_viking_a",0),("sword_viking_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
506, weight(1.5)|difficulty(8)|spd_rtng(99) | weapon_length(95)|swing_damage(31 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],
["sword_viking_a_long", "Nordic Champion's Sword", [("sword_viking_a_long",0),("sword_viking_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
626, weight(1.8)|difficulty(9)|spd_rtng(97) | weapon_length(102)|swing_damage(32 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["sword_viking_3_small", "Nordic Short War Sword", [("sword_viking_a_small",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
393, weight(1.1)|difficulty(7)|spd_rtng(102) | weapon_length(81)|swing_damage(30 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["sword_viking_c_long", "Nordic Champion's Sword", [("sword_viking_c_long",0),("sword_viking_c_long_scabbard ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
626, weight(1.8)|difficulty(9)|spd_rtng(97) | weapon_length(102)|swing_damage(32 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ] ,

["arabian_sword_a",         "Arabian Sword", [("arabian_sword_a",0),("scab_arabian_sword_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
117, weight(1.8)|difficulty(9)|spd_rtng(99) | weapon_length(100)|swing_damage(30 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
["arabian_sword_b",         "Arabian Arming Sword", [("arabian_sword_b",0),("scab_arabian_sword_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
271, weight(1.8)|difficulty(9)|spd_rtng(98) | weapon_length(100)|swing_damage(32 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
["sarranid_cavalry_sword",         "Arabian Cavalry Sword", [("arabian_sword_c",0),("scab_arabian_sword_c", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
578, weight(2.3)|difficulty(10)|spd_rtng(96) | weapon_length(105)|swing_damage(33 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
["arabian_sword_d",         "Arabian Guard Sword", [("arabian_sword_d",0),("scab_arabian_sword_d", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
421, weight(1.9)|difficulty(9)|spd_rtng(97) | weapon_length(100)|swing_damage(30 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],

["broad_short_sword", "Broad Short Sword", [("Faradon_onehanded",0),("Faradon_onehanded_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
172, weight(1.3)|difficulty(9)|spd_rtng(100) | weapon_length(85)|swing_damage(30 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],

["katzbalger_a", "Katzbalger", [("katzbalger_a",0),("Faradon_onehanded_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
228, weight(1.2)|difficulty(7)|spd_rtng(100) | weapon_length(88)|swing_damage(31 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],

["thegn_sword", "Thegn Sword", [("thegn",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
432, weight(1.1)|difficulty(7)|spd_rtng(101) | weapon_length(85)|swing_damage(31 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],
["nordic_nobleman_sword", "Nordic Nobleman Sword", [("LOKI_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
511, weight(2.2)|difficulty(9)|spd_rtng(97) | weapon_length(104)|swing_damage(32 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
["lombardic_sword", "Lombardic_Sword", [("OWBrescia",0),("OWBrescia_scab.0",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
419, weight(1.6)|difficulty(8)|spd_rtng(98) | weapon_length(99)|swing_damage(31 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["nobleman_sword_a", "Nobleman's Sword", [("OWAlbiCastellan",0),("OWCastellan_scab.0",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
461, weight(1.1)|difficulty(7)|spd_rtng(101) | weapon_length(91)|swing_damage(28 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
["nobleman_sword_b", "Gilded Nobleman's Sword", [("OWKingmaker",0),("OWKingmaker_scab.0",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
433, weight(1.1)|difficulty(7)|spd_rtng(102) | weapon_length(88)|swing_damage(30 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
["nobleman_sword_c", "Gilded Nobleman's Sword", [("OWDT2150Sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
426, weight(0.9)|difficulty(6)|spd_rtng(103) | weapon_length(80)|swing_damage(28 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
["nobleman_sword_d", "Condottier Sword", [("OWCondottierSword",0),("OWCondottierSword_scab.0",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
493, weight(1.1)|difficulty(7)|spd_rtng(101) | weapon_length(91)|swing_damage(32 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
["venetian_sword", "Venetian Sword", [("OWDogeSword",0),("OWDogeSword_scab.0",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
510, weight(1.3)|difficulty(7)|spd_rtng(99) | weapon_length(91)|swing_damage(30 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
["cav_sword", "European Cavalry Sword", [("senni_cavsword",0),("senni_cavsword_sheath",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
716, weight(2.3)|difficulty(9)|spd_rtng(96) | weapon_length(105)|swing_damage(31 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],
["crusader_sword", "Crusader Sword", [("crusader_sword",0),("crusader_sword_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
511, weight(1.2)|difficulty(7)|spd_rtng(100) | weapon_length(93)|swing_damage(30 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],
["espada_eslavona_a", "Espada Eslavona", [("espada_eslavona_a",0),("espada_eslavona_a_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
433, weight(1)|difficulty(7)|spd_rtng(101) | weapon_length(90)|swing_damage(26 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],	
["espada_eslavona_b", "Long Espada Eslavona", [("espada_eslavona_b",0),("espada_eslavona_b_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
489, weight(1.5)|difficulty(8)|spd_rtng(99) | weapon_length(103)|swing_damage(27 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
["italian_sword", "Italian Sword", [("italian_sword",0),("italian_sword_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
322, weight(1.5)|difficulty(8)|spd_rtng(99) | weapon_length(98)|swing_damage(30 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],
["scottish_sword", "Scottish Sword", [("scottish_sword",0),("scottish_sword_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
328, weight(1)|difficulty(7)|spd_rtng(102) | weapon_length(80)|swing_damage(27 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
["side_sword", "Side Sword", [("side_sword",0),("side_sword_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
394, weight(1.4)|difficulty(7)|spd_rtng(99) | weapon_length(95)|swing_damage(28 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
["byzantine_spathion", "Spathion", [("byzantine_spathion",0),("byzantine_spathion_scabb",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
621, weight(1.8)|difficulty(8)|spd_rtng(96) | weapon_length(102)|swing_damage(28 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
["milanese_sword", "Milanese Sword", [("milanese_sword",0),("milanese_sword_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
232, weight(1)|difficulty(7)|spd_rtng(103) | weapon_length(75)|swing_damage(26 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],	
["longbowman_sword", "Coltellaccio", [("longbowman_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
337, weight(1.2)|difficulty(7)|spd_rtng(100) | weapon_length(84)|swing_damage(32 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],
["irish_sword", "Irish Sword", [("irish_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
502, weight(1.7)|difficulty(8)|spd_rtng(98) | weapon_length(104)|swing_damage(30 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],
["grosse_messer_a", "Grosses Messer", [("grosse_messer",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
271, weight(1.2)|difficulty(7)|spd_rtng(99) | weapon_length(85)|swing_damage(34 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
["grosse_messer_b", "Langes Messer", [("grosse_messer_b",0),("grosse_messer_b_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
333, weight(1.7)|difficulty(8)|spd_rtng(98) | weapon_length(92)|swing_damage(32 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],		
["flammard", "One Handed Flambard", [("flammard",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
228, weight(2.1)|difficulty(10)|spd_rtng(101) | weapon_length(86)|swing_damage(31 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
#["flammard_alt", "One Handed Flambard", [("flammard",0)], itp_type_two_handed_wpn|itp_secondary, itc_greatsword|itcf_carry_sword_left_hip,
# 456 , weight(2.1)|difficulty(10)|spd_rtng(101) | weapon_length(86)|swing_damage(31 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],

 
 
##########################################
########### 1H Axes ######################
##########################################
["hatchet",         "Hatchet", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
6, weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(60)|swing_damage(23 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["hand_axe",         "Hand Axe", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
12, weight(2)|difficulty(7)|spd_rtng(95) | weapon_length(75)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["one_handed_war_axe_a", "One Handed Axe", [("one_handed_war_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
110, weight(1)|difficulty(7)|spd_rtng(99) | weapon_length(71)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_a", "Light One Handed Battle Axe", [("one_handed_battle_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
171, weight(1)|difficulty(8)|spd_rtng(99) | weapon_length(73)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_war_axe_b", "One Handed War Axe", [("one_handed_war_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
272, weight(1.2)|difficulty(8)|spd_rtng(98) | weapon_length(71)|swing_damage(36 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_b", "One Handed Battle Axe", [("one_handed_battle_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
439, weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(76)|swing_damage(37 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_c", "Broad One Handed Battle Axe", [("one_handed_battle_axe_c",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
510, weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(73)|swing_damage(37 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["sarranid_axe_a", "Iron Battle Axe", [("one_handed_battle_axe_g",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
710, weight(3)|difficulty(12)|spd_rtng(97) | weapon_length(71)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["sarranid_axe_b", "Iron War Axe", [("one_handed_battle_axe_h",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
660, weight(3.2)|difficulty(12)|spd_rtng(96) | weapon_length(69)|swing_damage(39 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

 
 
################################################################
########### 1H Falchions, Cleavers and other  ##################
################################################################
["cleaver",         "Cleaver", [("cleaver_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver, 
7, weight(1.5)|difficulty(0)|spd_rtng(103) | weapon_length(35)|swing_damage(24 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["military_cleaver_b", "Soldier's Cleaver", [("military_cleaver_b",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
337, weight(1.9)|difficulty(9)|spd_rtng(97) | weapon_length(92)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["military_cleaver_c", "Military Cleaver", [("military_cleaver_c",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
439, weight(2.2)|difficulty(10)|spd_rtng(96) | weapon_length(92)|swing_damage(36 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
 
["falchion",   "Falchion", [("medieval_falchion_b",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
117, weight(2)|difficulty(9)|spd_rtng(99) | weapon_length(88)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
["falchion_b",         "French Falchion", [("mackie_falchion03_edited",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_thrust_onehanded|itcf_carry_sword_left_hip, 
288, weight(1.5)|difficulty(8)|spd_rtng(97) | weapon_length(94)|swing_damage(33 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
["falchion_c",         "Falchion", [("medieval_falchion_a",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_thrust_onehanded|itcf_carry_sword_left_hip, 
57, weight(1)|difficulty(7)|spd_rtng(104) | weapon_length(61)|swing_damage(31 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],	
["italian_falchion", "Italian Falchion", [("italian_falchion",0),("italian_falchion_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
216, weight(1)|difficulty(7)|spd_rtng(101) | weapon_length(70)|swing_damage(34 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],	

["wooden_stick",         "Wooden Stick", [("wooden_stick",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 
2, weight(1)|difficulty(0)|spd_rtng(99) | weapon_length(63)|swing_damage(15 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["cudgel",         "Cudgel", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar|itcf_carry_mace_left_hip, 
2, weight(1.2)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(15 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["hammer",         "Hammer", [("iron_hammer_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar, 
3, weight(1)|difficulty(0)|spd_rtng(100) | weapon_length(55)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["club",         "Club", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar|itcf_carry_mace_left_hip, 
5, weight(1.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["winged_mace",         "Flanged Mace", [("flanged_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
61, weight(1.5)|difficulty(9)|spd_rtng(99) | weapon_length(70)|swing_damage(25 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["spiked_mace",         "Spiked Mace", [("spiked_mace_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
111, weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(70)|swing_damage(29 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick ],
["pickaxe",         "Pickaxe *", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
13, weight(3)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(19 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["spiked_club",         "Spiked Club", [("spiked_club",0)], itp_type_one_handed_wpn|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
41, weight(2)|difficulty(6)|spd_rtng(99) | weapon_length(68)|swing_damage(21 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],

["military_sickle_a", "Military Sickle", [("military_sickle_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
160, weight(1.5)|difficulty(9)|spd_rtng(99) | weapon_length(75)|swing_damage(26 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],
["fighting_pick", "Fighting Pick", [("czekan_a",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
117, weight(1.5)|difficulty(8)|spd_rtng(96) | weapon_length(80)|swing_damage(27 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["military_pick", "Military Pick", [("steel_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
382, weight(2.2)|difficulty(10)|spd_rtng(98) | weapon_length(70)|swing_damage(29 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["steel_pick", "Steel Pick", [("steel_pick_swup",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
716, weight(2.2)|difficulty(9)|spd_rtng(98) | weapon_length(64)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["military_hammer",         "Military Hammer", [("czekan_b",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
212, weight(3.1)|difficulty(12)|spd_rtng(95) | weapon_length(80)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick ],
["one_handed_warhammer",         "Warhammer", [("Faradon_warhammer",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_thrust_onehanded |itcf_carry_mace_left_hip, 
726, weight(3.3)|difficulty(14)|spd_rtng(96) | weapon_length(65)|swing_damage(32 , blunt) | thrust_damage(24 ,  pierce),imodbits_mace ],
#["one_handed_warhammer_alt",         "Warhammer", [("Faradon_warhammer",0)], itp_offset_flip|itp_type_one_handed_wpn| itp_secondary|itp_wooden_parry, itc_scimitar|itcf_thrust_onehanded|itcf_carry_mace_left_hip, 
# 1452 , weight(3.3)|difficulty(14)|spd_rtng(97) | weapon_length(65)|swing_damage(31 , pierce) | thrust_damage(24 ,  pierce),imodbits_mace ],
 
["mace_1",         "Spiked Club", [("mace_d",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
61, weight(1.5)|difficulty(6)|spd_rtng(99) | weapon_length(70)|swing_damage(21 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_2",         "Knobbed Mace", [("mace_a",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
117, weight(2.2)|difficulty(7)|spd_rtng(98) | weapon_length(70)|swing_damage(26 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_3",         "Spiked Mace", [("mace_c",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
167, weight(2.8)|difficulty(8)|spd_rtng(97) | weapon_length(70)|swing_damage(27 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_4",         "Winged Mace", [("mace_b",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
217, weight(2)|difficulty(7)|spd_rtng(99) | weapon_length(70)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["iberian_mace",         "Iberian Mace", [("Faradon_IberianMace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
117, weight(2.8)|difficulty(13)|spd_rtng(98) | weapon_length(71)|swing_damage(29 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sarranid_mace_1",         "Iron Mace", [("mace_small_d",0)], itp_type_one_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
514, weight(3.5)|difficulty(13)|spd_rtng(97) | weapon_length(69)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["one_handed_bar_mace",         "One Handed Bar Mace", [("Faradon_Rico_1hbarmace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
716, weight(3.6)|difficulty(18)|spd_rtng(96) | weapon_length(72)|swing_damage(32 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["spathovaklion", "Spathovaklion", [("spathovaklion_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_thrust_onehanded|itcf_carry_sword_left_hip, 
667, weight(1.5)|difficulty(8)|spd_rtng(99) | weapon_length(75)|swing_damage(27 , blunt) | thrust_damage(25 ,  blunt),imodbits_mace ],

##["military_hammer", "Military Hammer *", [("military_hammer",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
##317 , weight(2)|difficulty(7)|spd_rtng(95) | weapon_length(70)|swing_damage(31 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],




################################################################
########### 1H Sabres  #########################################
################################################################
["scimitar",         "Scimitar", [("scimitar_a",0),("scab_scimeter_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
282, weight(1.4)|difficulty(8)|spd_rtng(100) | weapon_length(95)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["scimitar_b",         "Elite Scimitar", [("scimitar_b",0),("scab_scimeter_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
494, weight(1.5)|difficulty(9)|spd_rtng(99) | weapon_length(100)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["sword_khergit_1", "Nomad Sabre", [("khergit_sword_b",0),("khergit_sword_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
217, weight(1)|difficulty(5)|spd_rtng(103) | weapon_length(86)|swing_damage(29 , cut),imodbits_sword_high ],
["sword_khergit_2", "Sabre", [("khergit_sword_c",0),("khergit_sword_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
433, weight(1.2)|difficulty(6)|spd_rtng(102) | weapon_length(88)|swing_damage(31 , cut),imodbits_sword_high ],
["sword_khergit_3", "Sabre", [("khergit_sword_a",0),("khergit_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
327, weight(1)|difficulty(5)|spd_rtng(102) | weapon_length(87)|swing_damage(30 , cut),imodbits_sword_high ],
["sword_khergit_4", "Heavy Sabre", [("khergit_sword_d",0),("khergit_sword_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
516, weight(1.5)|difficulty(6)|spd_rtng(101) | weapon_length(88)|swing_damage(32 , cut),imodbits_sword_high ],
["paramerion", "Paramerion", [("paramerion",0),("paramerion_scabb",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
617, weight(1.6)|difficulty(8)|spd_rtng(96) | weapon_length(103)|swing_damage(31 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],



################################################################
########### 2H Swords  #########################################
################################################################
 
["sword_of_war", "Sword of War", [("b_bastard_sword",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_cant_use_on_horseback| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
899, weight(2.3)|difficulty(10)|spd_rtng(94) | weapon_length(121)|swing_damage(40 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["sword_two_handed_b",         "Two Handed Sword", [("sword_two_handed_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
617, weight(2)|difficulty(10)|spd_rtng(97) | weapon_length(110)|swing_damage(38 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["sword_two_handed_a",         "Great Sword", [("sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
933, weight(2.2)|difficulty(10)|spd_rtng(94) | weapon_length(120)|swing_damage(37 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
["flambard_a",         "Flambard", [("flambard_v1",0)], itp_type_two_handed_wpn|itp_merchandise|itp_cant_use_on_horseback| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
487, weight(2.5)|difficulty(11)|spd_rtng(95) | weapon_length(117)|swing_damage(41 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
#["flambard_b",         "Flambard", [("flambard",0)], itp_type_two_handed_wpn|itp_merchandise|itp_cant_use_on_horseback| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
# 975 , weight(2.5)|difficulty(11)|spd_rtng(95) | weapon_length(117)|swing_damage(41 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
["estoc",         "Estoc", [("estoc",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
488, weight(1.7)|difficulty(9)|spd_rtng(98) | weapon_length(107)|swing_damage(30 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],
["german_greatsword",         "German Greatsword", [("Faradon_twohanded1",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_sword_back,
933, weight(2.2)|difficulty(10)|spd_rtng(92) | weapon_length(123)|swing_damage(39 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
["danish_greatsword",         "Danish Greatsword", [("Faradon_twohanded2",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_sword_back,
983, weight(2.3)|difficulty(11)|spd_rtng(92) | weapon_length(124)|swing_damage(41 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],
["kreigsmesser",         "Kreigsmesser", [("kriegsmesser_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_cant_use_on_horseback| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
773, weight(2.3)|difficulty(11)|spd_rtng(94) | weapon_length(116)|swing_damage(42 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
["flamberge",         "Flamberge", [("flamberge",0)], itp_type_two_handed_wpn|itp_cant_use_on_horseback|itp_merchandise| itp_two_handed|itp_primary, itc_flamberge|itcf_carry_sword_back,
1002, weight(4)|difficulty(14)|spd_rtng(87) | weapon_length(152)|swing_damage(47 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
["greatsword_a",         "Greatsword", [("OWDaneSword",0)], itp_type_two_handed_wpn|itp_cant_use_on_horseback|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
489, weight(2.1)|difficulty(10)|spd_rtng(95) | weapon_length(115)|swing_damage(39 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
["greatsword_b",         "Greatsword", [("OWSvanteSword",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
517, weight(1.7)|difficulty(9)|spd_rtng(101) | weapon_length(92)|swing_damage(40 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["claymore",         "Highland Claymore", [("2h_claymore_new",0),("2h_claymore_scabbard_new", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_cant_use_on_horseback| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
894, weight(3)|difficulty(12)|spd_rtng(93) | weapon_length(117)|swing_damage(43 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],
["merc_sword",         "Mercenary Sword", [("merc_sword",0),("merc_sword_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
728, weight(2.1)|difficulty(10)|spd_rtng(95) | weapon_length(111)|swing_damage(39 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
#["swiss_longsword_a",         "Golden Swiss Longsword", [("golden_swiss_longsword",0)], itp_type_two_handed_wpn|itp_cant_use_on_horseback|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
# 1752 , weight(2.8)|difficulty(11)|spd_rtng(93) | weapon_length(116)|swing_damage(43 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],
["swiss_longsword",         "Swiss Longsword", [("swiss_longsword",0)], itp_type_two_handed_wpn|itp_merchandise|itp_cant_use_on_horseback| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
826, weight(2.8)|difficulty(11)|spd_rtng(93) | weapon_length(116)|swing_damage(43 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],
["french_greatsword",         "French Greatsword", [("fleur_de_lys",0),("fleur_de_lys_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_cant_use_on_horseback|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
877, weight(2.3)|difficulty(10)|spd_rtng(94) | weapon_length(118)|swing_damage(39 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
["heavy_great_sword",         "Heavy Great Sword", [("senni_heavy",0)], itp_type_two_handed_wpn|itp_merchandise|itp_cant_use_on_horseback| itp_two_handed|itp_primary, itc_flamberge|itcf_carry_sword_back,
955, weight(3.3)|difficulty(12)|spd_rtng(91) | weapon_length(140)|swing_damage(42 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["khergit_sword_two_handed_a",         "Baguadao", [("khergit_sword_two_handed_a",0)], itp_cant_use_on_horseback|itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
394, weight(2.4)|difficulty(10)|spd_rtng(95) | weapon_length(115)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["khergit_sword_two_handed_b",         "Miaodao", [("khergit_sword_two_handed_b",0)], itp_cant_use_on_horseback|itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
505, weight(2.1)|difficulty(10)|spd_rtng(96) | weapon_length(115)|swing_damage(42 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["two_handed_cleaver", "War Cleaver", [("military_cleaver_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
320, weight(3.5)|difficulty(13)|spd_rtng(93) | weapon_length(120)|swing_damage(45 , cut) | thrust_damage(0 ,  cut),imodbits_sword_high ],
["shortened_military_scythe",         "Shortened Military Scythe", [("two_handed_battle_scythe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
216, weight(2.2)|difficulty(10)|spd_rtng(93) | weapon_length(112)|swing_damage(40 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

 
################################################################
########### 2H Mauls, Maces, Axes and others  ##################
################################################################
["nailed_warclub",         "Nailed Warclub", [("mackie_nailed_warclub",0)], itp_type_two_handed_wpn|itp_merchandise|itp_cant_use_on_horseback| itp_two_handed|itp_primary|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
111, weight(2.5)|difficulty(11)|spd_rtng(94) | weapon_length(117)|swing_damage(27 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sarranid_two_handed_mace_1",         "Long Iron Mace", [("mace_long_d",0)], itp_type_two_handed_wpn|itp_can_knock_down|itp_two_handed|itp_merchandise| itp_primary|itp_crush_through|itp_unbalanced, itc_greatsword|itcf_carry_axe_back,
611, weight(4)|difficulty(14)|spd_rtng(95) | weapon_length(95)|swing_damage(32 , blunt) | thrust_damage(25 ,  blunt),imodbits_mace ],
["bar_mace",         "Bar Mace", [("Faradon_IronClub",0)], itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down| itp_two_handed|itp_primary|itp_unbalanced|itp_cant_use_on_horseback, itc_nodachi|itcf_carry_axe_back,
717, weight(4.5)|difficulty(15)|spd_rtng(93) | weapon_length(96)|swing_damage(35 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["warhammer_b",         "Two Handed Warhammer", [("2H_Faradon_warhammer",0)], itp_type_two_handed_wpn|itp_cant_use_on_horseback|itp_merchandise|itp_can_knock_down| itp_two_handed|itp_primary|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
372, weight(4.5)|difficulty(15)|spd_rtng(93) | weapon_length(96)|swing_damage(35 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["maul",         "Maul", [("maul_b",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
87, weight(5)|difficulty(15)|spd_rtng(87) | weapon_length(69)|swing_damage(34 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sledgehammer", "Sledgehammer", [("maul_c",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
327, weight(6)|difficulty(16)|spd_rtng(84) | weapon_length(71)|swing_damage(37, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["warhammer",         "Great Maul", [("maul_d",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
944, weight(8)|difficulty(18)|spd_rtng(81) | weapon_length(68)|swing_damage(43 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

["morningstar",         "Morningstar", [("mace_morningstar_new",0)],itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_mace_left_hip, 
888, weight(3.7)|difficulty(13)|spd_rtng(92) | weapon_length(82)|swing_damage(38 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],

["voulge",         "Voulge *", [("voulge",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
64, weight(4.5)|difficulty(8)|spd_rtng(87) | weapon_length(119)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["shortened_voulge",         "Shortened Voulge", [("two_handed_battle_axe_c",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
270, weight(2.8)|difficulty(11)|spd_rtng(93) | weapon_length(100)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["axe",                 "Axe", [("iron_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
32, weight(2)|difficulty(9)|spd_rtng(94) | weapon_length(94)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["battle_axe",         "Battle Axe", [("medieval_battle_axe_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
282, weight(3.3)|difficulty(12)|spd_rtng(89) | weapon_length(93)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["war_axe",         "War Axe *", [("war_ax",0)], itp_cant_use_on_horseback|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
#645 , weight(3)|difficulty(10)|spd_rtng(86) | weapon_length(110)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["war_axe",         "War Axe", [("medieval_battle_axe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
392, weight(4.2)|difficulty(14)|spd_rtng(90) | weapon_length(96)|swing_damage(50 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["bardiche",         "Bardiche", [("two_handed_battle_axe_d",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
475, weight(3)|difficulty(12)|spd_rtng(92) | weapon_length(102)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["great_bardiche",         "Great Bardiche", [("two_handed_battle_axe_f",0)], itp_type_two_handed_wpn|itp_cant_use_on_horseback|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
561, weight(3.2)|difficulty(12)|spd_rtng(90) | weapon_length(116)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["two_handed_axe",         "Two Handed Axe", [("two_handed_battle_axe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
394, weight(2.2)|difficulty(11)|spd_rtng(95) | weapon_length(90)|swing_damage(37 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["two_handed_battle_axe_2",         "Two Handed War Axe", [("two_handed_battle_axe_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
451, weight(2.5)|difficulty(11)|spd_rtng(96) | weapon_length(92)|swing_damage(42 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["sarranid_two_handed_axe_b",         "Persian War Axe", [("two_handed_battle_axe_h",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
521, weight(3.5)|difficulty(13)|spd_rtng(94) | weapon_length(90)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["bearded_axe",         "Bearded Axe", [("mackie_bearded_axe",0)], itp_type_two_handed_wpn|itp_cant_use_on_horseback|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
328, weight(3.2)|difficulty(12)|spd_rtng(93) | weapon_length(108)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["great_axe",         "Great Axe", [("two_handed_battle_axe_e",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
521, weight(3.2)|difficulty(12)|spd_rtng(95) | weapon_length(96)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["celtic_axe",         "Celtic Axe", [("mackie_celtic_axe",0)], itp_type_two_handed_wpn|itp_cant_use_on_horseback|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
444, weight(3.2)|difficulty(12)|spd_rtng(93) | weapon_length(100)|swing_damage(48 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["sarranid_two_handed_axe_a",         "Persian Battle Axe", [("two_handed_battle_axe_g",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
562, weight(4.7)|difficulty(16)|spd_rtng(92) | weapon_length(95)|swing_damage(49 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

##["fighting_pick", "Fighting Pick *", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
##108 , weight(1.0)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(22 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],

################################################################
########### Bastard weapons  ###################################
################################################################
["bastard_sword_a", "Bastard Sword", [("bastard_sword_a",0),("bastard_sword_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
394, weight(1.8)|difficulty(9)|spd_rtng(100) | weapon_length(101)|swing_damage(35 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["bastard_sword_b", "Heavy Bastard Sword", [("bastard_sword_b",0),("bastard_sword_b_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
484, weight(1.9)|difficulty(9)|spd_rtng(99) | weapon_length(105)|swing_damage(36 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["longsword", "Longsword", [("Faradon_handandahalf",0),("Faradon_handandahalf_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
935, weight(1.8)|difficulty(9)|spd_rtng(98) | weapon_length(106)|swing_damage(37 , cut) | thrust_damage(24 ,  pierce),imodbits_sword ],
["studded_warclub",         "Studded Warclub", [("Faradon_LargeClub",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary, itc_warclub|itcf_carry_axe_back,
172, weight(2.3)|difficulty(10)|spd_rtng(96) | weapon_length(92)|swing_damage(29 , blunt) | thrust_damage(24 ,  blunt),imodbits_sword_high ],
["executioner_sword_a", "Executioner Sword", [("ray_Executioner_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip,
839, weight(2.3)|difficulty(10)|spd_rtng(96) | weapon_length(96)|swing_damage(44 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
["executioner_sword_a_alt", "Executioner Sword", [("ray_Executioner_sword",0)], itp_type_two_handed_wpn|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip,
839, weight(2.3)|difficulty(10)|spd_rtng(97) | weapon_length(96)|swing_damage(44 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
["danish_bastard_sword", "Danish Bastard Sword", [("OWEarlLongSw",0),("OWEarlLongSw_scab.0", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
778, weight(1.8)|difficulty(9)|spd_rtng(100) | weapon_length(100)|swing_damage(36 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["french_longsword", "French Longsword", [("OWCluny",0),("OWCluny_scab.0", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
661, weight(1.8)|difficulty(9)|spd_rtng(99) | weapon_length(104)|swing_damage(33 , cut) | thrust_damage(27 ,  pierce),imodbits_sword ],
["longsword_b", "Longsword", [("OWMunich",0),("OWMunich_scab.0", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
716, weight(1.4)|difficulty(8)|spd_rtng(100) | weapon_length(101)|swing_damage(34 , cut) | thrust_damage(25 ,  pierce),imodbits_sword ],
["longsword_c", "Crusader Longsword", [("OWDT5157Sword",0),("OWDT5157Sword_scab.0", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
767, weight(2)|difficulty(10)|spd_rtng(97) | weapon_length(110)|swing_damage(35 , cut) | thrust_damage(27 ,  pierce),imodbits_sword ],
["german_bastard_sword", "German Longsword", [("german_bastard_sword",0),("german_bastard_sword_scabbard.0", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
761, weight(1.8)|difficulty(9)|spd_rtng(98) | weapon_length(106)|swing_damage(35 , cut) | thrust_damage(27 ,  pierce),imodbits_sword ],
# Goedendag
["club_with_spike_head",  "Goedendag", [("mace_e",0)],  itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_wooden_parry, itc_bastardsword|itcf_carry_axe_back,
110, weight(2.5)|difficulty(9)|spd_rtng(96) | weapon_length(117)|swing_damage(25 , blunt) | thrust_damage(24 ,  pierce),imodbits_mace ],

################################################################
########### Spears and pikes  ##################################
################################################################

["boar_spear",         "Boar Spear", [("boar_spear_new",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear|itcf_carry_spear,
61, weight(1.8)|difficulty(8)|spd_rtng(93) | weapon_length(145)|swing_damage(19 , pierce) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["shortened_spear",         "Shortened Spear", [("spear_g_1-9m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
43, weight(1.3)|difficulty(6)|spd_rtng(102) | weapon_length(120)|swing_damage(18 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["spear",         "Spear", [("spear_h_2-15m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
56, weight(1.4)|difficulty(7)|spd_rtng(97) | weapon_length(135)|swing_damage(20 , pierce) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["bamboo_spear",         "Bamboo Spear", [("arabian_spear_a_3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
62, weight(2.0)|difficulty(8)|spd_rtng(91) | weapon_length(200)|swing_damage(16 , blunt) | thrust_damage(25 ,  pierce),imodbits_polearm ],
["war_spear",         "War Spear", [("spear_i_2-3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
116, weight(1.5)|difficulty(9)|spd_rtng(95) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["pike",         "Long Spear", [("spear_a_3m",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_wooden_parry|itp_two_handed, itc_pike|itcf_carry_spear,
217, weight(2)|difficulty(10)|spd_rtng(81) | weapon_length(245)|swing_damage(0 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
##["spear_e_3-25m",         "Spear_3-25m", [("spear_e_3-25m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
## 150 , weight(4.5)|difficulty(0)|spd_rtng(81) | weapon_length(225)|swing_damage(19 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["ashwood_pike", "Ashwood Pike", [("pike",0)], itp_type_polearm|itp_penalty_with_shield|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_cutting_spear,
484, weight(2)|difficulty(10)|spd_rtng(93) | weapon_length(166)|swing_damage(18 , blunt) | thrust_damage(30,  pierce),imodbits_polearm ],
["awlpike",    "Awlpike", [("awl_pike_b",0)], itp_type_polearm|itp_offset_lance|itp_two_handed|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
571, weight(2.25)|difficulty(10)|spd_rtng(92) | weapon_length(165)|swing_damage(20 , blunt) | thrust_damage(33 ,  pierce),imodbits_polearm ],
["awlpike_long",  "Long Awlpike", [("awl_pike_a",0)], itp_type_polearm|itp_offset_lance|itp_two_handed|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
615, weight(2.8)|difficulty(11)|spd_rtng(89) | weapon_length(185)|swing_damage(21 , blunt) | thrust_damage(32 ,  pierce),imodbits_polearm ],
#["awlpike",         "Awlpike", [("pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
# 378 , weight(3.5)|difficulty(12)|spd_rtng(92) | weapon_length(160)|swing_damage(20 ,blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],
["pike_b",         "Pike", [("pike_long",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_wooden_parry|itp_two_handed|itp_unbalanced, itc_pike|itcf_carry_spear,
283, weight(4.0)|difficulty(14)|spd_rtng(69) | weapon_length(300)|swing_damage(0 , blunt) | thrust_damage(24 ,  pierce),imodbits_polearm ],



################################################################
########### Polearms  ##########################################
################################################################
["staff",         "Staff", [("wooden_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
18, weight(1)|difficulty(5)|spd_rtng(103) | weapon_length(128)|swing_damage(15 , blunt) | thrust_damage(15 ,  blunt),imodbits_polearm ], 
["scythe",         "Scythe", [("scythe",0)], itp_type_polearm|itp_two_handed|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
21, weight(3)|difficulty(6)|spd_rtng(87) | weapon_length(182)|swing_damage(27 , cut) | thrust_damage(14 ,  pierce),imodbits_polearm ],
["military_scythe",         "Military Scythe", [("spear_e_2-5m",0),("spear_c_2-5m",imodbits_bad)], itp_type_polearm|itp_offset_lance|itp_two_handed|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
172, weight(2.5)|difficulty(11)|spd_rtng(92) | weapon_length(155)|swing_damage(35 , cut) | thrust_damage(24 ,  pierce),imodbits_polearm ],
["pitch_fork",         "Pitch Fork", [("pitch_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff|itcf_carry_spear,
32, weight(1.5)|difficulty(6)|spd_rtng(91) | weapon_length(154)|swing_damage(15 , blunt) | thrust_damage(25 ,  pierce),imodbits_polearm ],
["military_fork", "Military Fork", [("military_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry,itc_staff,
171, weight(1.5)|difficulty(9)|spd_rtng(96) | weapon_length(135)|swing_damage(19 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["battle_fork",         "Battle Fork", [("battle_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry,itc_staff, 
217, weight(1.7)|difficulty(9)|spd_rtng(94) | weapon_length(142)|swing_damage(24, pierce) | thrust_damage(33 ,  pierce),imodbits_polearm ],

["long_axe",         "Long Axe", [("long_axe_a",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced|itp_merchandise,itc_staff|itcf_carry_axe_back,
431, weight(3)|difficulty(12)|spd_rtng(97) | weapon_length(115)|swing_damage(41 , cut) | thrust_damage(21 ,  cut),imodbits_axe ],
["long_axe_b",         "Long War Axe", [("long_axe_b",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced|itp_merchandise, itc_staff|itcf_carry_axe_back,
493, weight(3.2)|difficulty(13)|spd_rtng(95) | weapon_length(123)|swing_damage(42 , cut) | thrust_damage(18 ,  blunt),imodbits_axe ],
["long_axe_c",         "Great Long Axe", [("long_axe_c",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced|itp_merchandise, itc_staff|itcf_carry_axe_back,
560, weight(3.5)|difficulty(13)|spd_rtng(92) | weapon_length(125)|swing_damage(45 , cut) | thrust_damage(18 ,  blunt),imodbits_axe ],

["long_voulge",         "Long Voulge", [("two_handed_battle_long_axe_a",0)], itp_type_polearm|itp_merchandise|itp_cant_use_on_horseback| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_cant_use_on_horseback, itc_staff,
501, weight(3.5)|difficulty(13)|spd_rtng(88) | weapon_length(175)|swing_damage(44 , cut) | thrust_damage(12 ,  pierce),imodbits_axe ],
["long_bardiche",         "Long Bardiche", [("two_handed_battle_long_axe_b",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_staff,
510, weight(3.5)|difficulty(13)|spd_rtng(90) | weapon_length(140)|swing_damage(46 , cut) | thrust_damage(13 ,  pierce),imodbits_axe ],
["great_long_bardiche",         "Great Long Bardiche", [("two_handed_battle_long_axe_c",0)], itp_type_polearm|itp_cant_use_on_horseback|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_staff,
715, weight(3.9)|difficulty(14)|spd_rtng(88) | weapon_length(155)|swing_damage(47 , cut) | thrust_damage(15 ,  pierce),imodbits_axe ],
 
["hafted_blade_b",         "Hafted Blade", [("khergit_pike_b",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
110, weight(1.7)|difficulty(9)|spd_rtng(96) | weapon_length(132)|swing_damage(33 , cut) | thrust_damage(32 ,  cut),imodbits_polearm ], 
["hafted_blade_a",         "Long Hafted Blade", [("khergit_pike_a",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
175, weight(2)|difficulty(10)|spd_rtng(92) | weapon_length(153)|swing_damage(36 , cut) | thrust_damage(33 ,  cut),imodbits_polearm ],


["long_spiked_club",         "Long Spiked Club", [("mace_long_c",0)], itp_type_polearm|itp_merchandise|itp_two_handed| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
117, weight(3)|difficulty(11)|spd_rtng(96) | weapon_length(126)|swing_damage(30 , pierce) | thrust_damage(23 ,  blunt),imodbits_mace ],
["long_hafted_knobbed_mace",         "Long Hafted Knobbed Mace", [("mace_long_a",0)], itp_type_polearm| itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
222, weight(3.3)|difficulty(12)|spd_rtng(94) | weapon_length(133)|swing_damage(28 , blunt) | thrust_damage(27 ,  blunt),imodbits_mace ],
["long_hafted_spiked_mace",         "Long Hafted Spiked Mace", [("mace_long_b",0)], itp_type_polearm|itp_unbalanced|itp_can_knock_down|itp_two_handed|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
328, weight(3.5)|difficulty(13)|spd_rtng(92) | weapon_length(139)|swing_damage(33 , blunt) | thrust_damage(23 ,  blunt),imodbits_mace ],

["glaive",         "Glaive", [("glaive_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
452, weight(2.8)|difficulty(11)|spd_rtng(90) | weapon_length(157)|swing_damage(39 , cut) | thrust_damage(22 ,  pierce),imodbits_polearm ],


["bec_de_corbin_a",  "Bec De Corbin", [("bec_de_corbin_a",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_poleaxe|itcf_carry_spear,
932, weight(3.0)|difficulty(12)|spd_rtng(91) | weapon_length(120)|swing_damage(34, pierce) | thrust_damage(24 ,  pierce),imodbits_polearm ],
["scottish_halberd",         "Scottish Halberd", [("alrok_halberd",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_wooden_parry, itc_staff|itcf_carry_spear,
943, weight(3)|difficulty(12)|spd_rtng(92) | weapon_length(144)|swing_damage(39 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],

["morningstar_a",         "Long Morningstar", [("mackie_morning_star_long",0)], itp_type_polearm|itp_cant_use_on_horseback |itp_merchandise|itp_bonus_against_shield| itp_primary|itp_two_handed|itp_wooden_parry|itp_unbalanced, itc_staff|itcf_carry_spear,
933, weight(4.5)|difficulty(15)|spd_rtng(88) | weapon_length(132)|swing_damage(37 , pierce) | thrust_damage(24 ,  pierce),imodbits_polearm ],
["voulge_new",         "Voulge", [("voulge_new",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry|itp_unbalanced|itp_bonus_against_shield, itc_staff|itcf_carry_spear,
127, weight(3)|difficulty(12)|spd_rtng(88) | weapon_length(124)|swing_damage(44 , cut) | thrust_damage(25 ,  pierce),imodbits_polearm ],
["fauchard_fork",         "Fauchard", [("fauchard_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_two_handed| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear|itcf_carry_spear,
121, weight(3)|difficulty(12)|spd_rtng(91) | weapon_length(172)|swing_damage(30 , cut) | thrust_damage(22 ,  pierce),imodbits_polearm ],
["long_maul",         "Long Maul", [("longmaul",0)], itp_type_polearm|itp_cant_use_on_horseback |itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry|itp_unbalanced|itp_crush_through|itp_can_knock_down, itc_staff|itcf_carry_spear,
986, weight(7)|difficulty(20)|spd_rtng(77) | weapon_length(125)|swing_damage(38 , blunt) | thrust_damage(21 ,  blunt),imodbits_polearm ],
["spetum_a",         "Spetum", [("spetum",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_wooden_parry|itp_two_handed, itc_cutting_spear|itcf_carry_spear,
327, weight(2.5)|difficulty(11)|spd_rtng(89) | weapon_length(186)|swing_damage(23 , blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],
["spetum_b",         "Ranseur", [("spetum_b",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_wooden_parry|itp_two_handed, itc_cutting_spear|itcf_carry_spear,
272, weight(2.5)|difficulty(11)|spd_rtng(89) | weapon_length(189)|swing_damage(32 , cut) | thrust_damage(31 ,  pierce),imodbits_polearm ],
["ranseur",         "Corseque", [("ranseur",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_wooden_parry|itp_two_handed, itc_cutting_spear|itcf_carry_spear,
427, weight(2.5)|difficulty(11)|spd_rtng(89) | weapon_length(186)|swing_damage(23 , pierce) | thrust_damage(31 ,  pierce),imodbits_polearm ],
["partisan",         "Partisan", [("partisan",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_wooden_parry|itp_two_handed|itp_bonus_against_shield, itc_cutting_spear|itcf_carry_spear,
394, weight(2.8)|difficulty(11)|spd_rtng(90) | weapon_length(176)|swing_damage(38 , cut) | thrust_damage(38 ,  cut),imodbits_polearm ],
["poleaxe_b",         "Elegant Poleaxe", [("elegant_poleaxe",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_wooden_parry, itc_staff|itcf_carry_spear,
879, weight(2.8)|difficulty(11)|spd_rtng(94) | weapon_length(132)|swing_damage(39 , cut) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["poleaxe_c",         "German Poleaxe", [("german_poleaxe",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_wooden_parry, itc_staff|itcf_carry_spear,
1000, weight(3)|difficulty(12)|spd_rtng(92) | weapon_length(131)|swing_damage(43 , cut) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["poleaxe_d",         "Poleaxe", [("poleaxe_a",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_cant_use_on_horseback|itp_wooden_parry, itc_staff|itcf_carry_spear,
978, weight(3.2)|difficulty(12)|spd_rtng(90) | weapon_length(141)|swing_damage(42 , cut) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["english_bill",         "English Bill", [("english_bill",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_wooden_parry|itp_two_handed, itc_cutting_spear|itcf_carry_spear,
1000, weight(3)|difficulty(12)|spd_rtng(90) | weapon_length(176)|swing_damage(31 , pierce) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["swiss_halberd",         "Swiss Halberd", [("swiss_halberd",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_bonus_against_shield|itp_primary|itp_wooden_parry|itp_two_handed, itc_cutting_spear|itcf_carry_spear,
899, weight(2.7)|difficulty(11)|spd_rtng(92) | weapon_length(162)|swing_damage(40 , cut) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["guisarme_a",         "Guisarme", [("guisarme_a_work",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_wooden_parry|itp_two_handed, itc_cutting_spear|itcf_carry_spear,
771, weight(2.5)|difficulty(11)|spd_rtng(92) | weapon_length(165)|swing_damage(29 , pierce) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["glaive1",         "Light Glaive", [("glaive1",0)], itp_type_polearm|itp_merchandise|itp_primary|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,
823, weight(2.3)|difficulty(10)|spd_rtng(92) | weapon_length(148)|swing_damage(39 , cut) | thrust_damage(22 ,  pierce),imodbits_polearm ],
["glaive2",         "Svaerdstav", [("glaive2",0)], itp_type_polearm|itp_merchandise|itp_primary|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,
606, weight(2.4)|difficulty(10)|spd_rtng(93) | weapon_length(166)|swing_damage(34 , cut) | thrust_damage(25 ,  pierce),imodbits_polearm ],


################################################################
########### Lances  ##########################################
################################################################
["jousting_lance", "Jousting Lance", [("joust_of_peace",0)], itp_crush_through|itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itcf_force_64_bits,
398, weight(5)|difficulty(16)|spd_rtng(61) | weapon_length(240)|swing_damage(0 , cut) | thrust_damage(17 ,  blunt),imodbits_polearm ],
["double_sided_lance", "Double Sided Lance", [("lance_dblhead",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff,
271, weight(1.8)|difficulty(9)|spd_rtng(96) | weapon_length(128)|swing_damage(22, blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],
["light_lance",         "Light Lance", [("spear_b_2-75m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
328, weight(1.6)|difficulty(8)|spd_rtng(92) | weapon_length(175)|swing_damage(16 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["lance",         "Lance", [("spear_d_2-8m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
437, weight(1.7)|difficulty(9)|spd_rtng(86) | weapon_length(180)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["heavy_lance",         "Heavy Lance", [("spear_f_2-9m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
616, weight(2.1)|difficulty(10)|spd_rtng(78) | weapon_length(190)|swing_damage(18 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["great_lance",         "Great Lance", [("heavy_lance",0)], itp_crush_through|itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itcf_force_64_bits, 
521, weight(5)|difficulty(16)|spd_rtng(66) | weapon_length(230)|swing_damage(0 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],


["sickle",         "Sickle", [("sickle",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver, 
4, weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(40)|swing_damage(20 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["knife",         "Knife", [("peasant_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left, 
9, weight(0.5)|difficulty(0)|spd_rtng(110) | weapon_length(40)|swing_damage(21 , cut) | thrust_damage(13 ,  pierce),imodbits_sword ],
["butchering_knife", "Butchering Knife", [("khyber_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right, 
11, weight(0.75)|difficulty(0)|spd_rtng(108) | weapon_length(60)|swing_damage(24 , cut) | thrust_damage(17 ,  pierce),imodbits_sword ],
["dagger",         "Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry),("dagger_b",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn, 
18, weight(0.75)|difficulty(0)|spd_rtng(109) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["dagger_c",         "Noble Dagger", [("mackie_noble_dagger",0),("mackie_noble_dagger_scabbard.1",ixmesh_carry),("mackie_noble_dagger",imodbits_good),("mackie_noble_dagger_scabbard.1",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn, 
 161 , weight(0.2)|difficulty(0)|spd_rtng(110) | weapon_length(38)|swing_damage(27 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],

#["nordic_sword", "Nordic Sword N", [("viking_sword",0),("scab_vikingsw", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
#656 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(98)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
##["arming_sword", "Arming Sword N", [("b_long_sword",0),("scab_longsw_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
##545 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(25 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
#["sword",         "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 148 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],

#["falchion",         "Falchion * ", [("falchion_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
#105 , weight(2.5)|difficulty(8)|spd_rtng(96) | weapon_length(73)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],

#["broadsword",         "Broadsword N", [("broadsword",0),("scab_broadsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
#122 , weight(2.5)|difficulty(8)|spd_rtng(91) | weapon_length(101)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["scimitar",         "Scimitar N", [("scimeter",0),("scab_scimeter", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
#108 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

#["nomad_sabre",         "Nomad Sabre N", [("shashqa",0),("scab_shashqa", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
# 343 , weight(1.75)|difficulty(9)|spd_rtng(98) | weapon_length(100)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["bastard_sword", "Bastard Sword N", [("bastard_sword",0),("scab_bastardsw", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
# 1123 , weight(2)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(35 , cut) | thrust_damage(25 ,  pierce),imodbits_sword ],
#["great_sword",         "Great Sword * ", [("b_bastard_sword",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
# 423 , weight(2.75)|difficulty(10)|spd_rtng(95) | weapon_length(125)|swing_damage(39 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high ],
#["fighting_axe", "Fighting Axe *", [("fighting_ax",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
#123 , weight(2.5)|difficulty(9)|spd_rtng(92) | weapon_length(90)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["battle_axe",         "Battle Axe *", [("battle_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
#455 , weight(2.5)|difficulty(9)|spd_rtng(88) | weapon_length(108)|swing_damage(41 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

#["double_axe",         "Double Axe", [("dblhead_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 1677 , weight(6)|difficulty(18)|spd_rtng(85) | weapon_length(95)|swing_damage(49 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["great_axe_b",         "Great Axe", [("great_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 1453 , weight(4.5)|difficulty(15)|spd_rtng(82) | weapon_length(120)|swing_damage(49 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

#["war_axe_b",         "War Axe", [("medieval_battle_axe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
# 785 , weight(4.2)|difficulty(14)|spd_rtng(90) | weapon_length(96)|swing_damage(50 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
  
#["battle_axe_b",         "Battle Axe", [("medieval_battle_axe_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
# 564 , weight(3.3)|difficulty(12)|spd_rtng(89) | weapon_length(93)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

#["sword_medieval_d", "sword_medieval_d", [("sword_medieval_d",0),("sword_medieval_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 131 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(24 , cut) | thrust_damage(21 ,  pierce),imodbits_sword ],
#["sword_medieval_e", "sword_medieval_e", [("sword_medieval_e",0),("sword_medieval_e_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 131 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(24 , cut) | thrust_damage(21 ,  pierce),imodbits_sword ],

#["falchion_d",         "Falchion", [("medieval_falchion_b",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_thrust_onehanded|itcf_carry_sword_left_hip, 
# 234 , weight(2)|difficulty(9)|spd_rtng(99) | weapon_length(88)|swing_damage(32 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],

##["czekan_a",         "Fighting Pick", [("czekan_a",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
## 234 , weight(1.5)|difficulty(8)|spd_rtng(96) | weapon_length(80)|swing_damage(27 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],

#["czekan_b",         "Military Hammer", [("czekan_b",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
# 424 , weight(3.1)|difficulty(12)|spd_rtng(95) | weapon_length(80)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick ],


#["boar_spear",         "Boar Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff|itcf_carry_spear, 
#76 , weight(1.5)|difficulty(9)|spd_rtng(90) | weapon_length(157)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_polearm ],


#["spear",         "Spear", [("spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear, 173 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],

#["lance",         "Lance", [("pike",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 196 , weight(5)|difficulty(0)|spd_rtng(72) | weapon_length(170)|swing_damage(0 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
#["pike",         "Pike", [("pike",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_spear,
# 212 , weight(6)|difficulty(0)|spd_rtng(77) | weapon_length(167)|swing_damage(0 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
#["poleaxe",         "Poleaxe", [("pole_ax",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff,
# 384 , weight(4.5)|difficulty(15)|spd_rtng(77) | weapon_length(180)|swing_damage(50 , cut) | thrust_damage(15 ,  blunt),imodbits_polearm ],
#["polehammer",         "Polehammer", [("pole_hammer",0)], itp_crush_through|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff,
# 745 , weight(7)|difficulty(20)|spd_rtng(50) | weapon_length(126)|swing_damage(50 , blunt) | thrust_damage(35 ,  blunt),imodbits_polearm ],
#["quarter_staff", "Quarter Staff", [("quarter_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
# 60 , weight(1.2)|difficulty(6)|spd_rtng(99) | weapon_length(137)|swing_damage(18 , blunt) | thrust_damage(18 ,  blunt),imodbits_polearm ],
#["iron_staff",         "Iron Staff", [("iron_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary, itc_staff|itcf_carry_sword_back,
# 343 , weight(2)|difficulty(10)|spd_rtng(95) | weapon_length(140)|swing_damage(25 , blunt) | thrust_damage(26 ,  blunt),imodbits_polearm ],

#["glaive_b",         "Glaive_b", [("glaive_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 352 , weight(4.5)|difficulty(0)|spd_rtng(83) | weapon_length(157)|swing_damage(38 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],


#TODO:["shortened_spear",         "shortened_spear", [("spear_e_2-1m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 65 , weight(2.0)|difficulty(0)|spd_rtng(98) | weapon_length(110)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
#TODO:["spear_2-4m",         "spear", [("spear_e_2-25m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 67 , weight(2.0)|difficulty(0)|spd_rtng(95) | weapon_length(125)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
 
#["bec_de_corbin_a_alt",  "Bec De Corbin", [("bec_de_corbin_a",0)], itp_offset_flip|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_poleaxe|itcf_carry_spear,
# 1864 , weight(3.0)|difficulty(12)|spd_rtng(91) | weapon_length(120)|swing_damage(32, blunt) | thrust_damage(24 ,  pierce),imodbits_polearm ],


#["boar_spear_b",         "Boar Spear", [("boar_spear_new",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear|itcf_carry_spear,
# 122 , weight(1.8)|difficulty(8)|spd_rtng(93) | weapon_length(145)|swing_damage(19 , pierce) | thrust_damage(27 ,  pierce),imodbits_polearm ],


#["qiang_a",         "Red Tassel Spear", [("qiang",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 645 , weight(1.5)|difficulty(8)|spd_rtng(95) | weapon_length(150)|swing_damage(18 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],

#["qiang_b",         "Red long Tassel Spear", [("qiang_b",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_wooden_parry|itp_two_handed|itp_unbalanced, itc_cutting_spear|itcf_carry_spear,
# 899 , weight(2.7)|difficulty(11)|spd_rtng(81) | weapon_length(200)|swing_damage(0 , blunt) | thrust_damage(25 ,  pierce),imodbits_polearm ],

 		
	#not merchandise	
		
#["naginata",         "Naginata", [("naginata",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff,
# 1685 , weight(3)|difficulty(12)|spd_rtng(88) | weapon_length(167)|swing_damage(42 , cut) | thrust_damage(33 ,  cut),imodbits_polearm ],
 
 
 
 ########################################## zrobione po crpgowemu

# SHIELDS

["wooden_shield", "Wooden Shield *", [("shield_round_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
##["wooden_shield", "Wooden Shield", [("shield_round_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield],




["round_shield", "Nordic Shield", [("shield_round_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  64 , weight(2)|hit_points(400)|body_armor(20)|spd_rtng(100)|shield_width(25),imodbits_shield ],
["nordic_shield", "Nordic Shield", [("shield_round_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  123 , weight(3.5)|difficulty(2)|hit_points(275)|body_armor(17)|spd_rtng(98)|shield_width(34),imodbits_shield ],
#["kite_shield_a",         "Yellow and Red Kite Shield", [("shield_kite_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  221 , weight(3.5)|hit_points(300)|difficulty(3)|body_armor(20)|spd_rtng(96)|shield_width(25)|shield_height(73),imodbits_shield ],
#["kite_shield_b", "White and Orange Kite Shield", [("shield_kite_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  221 , weight(3.5)|hit_points(300)|difficulty(3)|body_armor(20)|spd_rtng(96)|shield_width(25)|shield_height(73),imodbits_shield ],
["large_shield", "Templar's Shield", [("shield_kite_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  165 , weight(2.5)|hit_points(520)|body_armor(20)|spd_rtng(80)|shield_width(25)|shield_height(90),imodbits_shield ],
["battle_shield", "Blue and Yellow Kite Shield", [("shield_kite_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  432 , weight(6)|difficulty(3)|hit_points(380)|body_armor(20)|spd_rtng(89)|shield_width(25)|shield_height(89),imodbits_shield ],
["fur_covered_shield",  "Fur Covered Shield", [("shield_kite_m",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  227 , weight(3.5)|hit_points(600)|body_armor(20)|spd_rtng(76)|shield_width(40),imodbits_shield ],
#["heraldric_shield", "Heraldric Shield *", [("shield_heraldic",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  301 , weight(3.5)|hit_points(230)|body_armor(15)|spd_rtng(98)|shield_width(32),imodbits_shield ],
#["heater_shield", "Heater Shield *", [("shield_heater_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  477 , weight(3.5)|hit_points(230)|body_armor(15)|spd_rtng(98)|shield_width(30),imodbits_shield ],
["steel_shield", "Steel Shield", [("shield_dragon",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  697 , weight(4)|difficulty(4)|hit_points(700)|body_armor(17)|spd_rtng(61)|shield_width(40),imodbits_shield ],
#["nomad_shield", "Nomad Shield *", [("shield_wood_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  123 , weight(11.5)|difficulty(5)|hit_points(236)|body_armor(74)|spd_rtng(73)|shield_width(31),imodbits_shield ],

["plate_covered_round_shield", "Plate Covered Round Shield", [("shield_round_e",0)], itp_type_shield, itcf_carry_round_shield,  678 , weight(4)|hit_points(222)|difficulty(4)|body_armor(61)|spd_rtng(80)|shield_width(31),imodbits_shield ],
["leather_covered_round_shield", "Leather Covered Round Shield", [("shield_round_d",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  80 , weight(3)|hit_points(160)|body_armor(28)|spd_rtng(99)|shield_width(34),imodbits_shield ],
["hide_covered_round_shield", "Hide Covered Round Shield", [("shield_round_f",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  40 , weight(2)|hit_points(160)|body_armor(21)|spd_rtng(100)|shield_width(34),imodbits_shield ],

["shield_heater_c", "Heater Shield", [("shield_heater_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  277 , weight(3.5)|difficulty(3)|hit_points(410)|body_armor(2)|spd_rtng(80)|shield_width(25)|shield_height(50),imodbits_shield ],
["shield_heater_d", "Green Crescent Heater Shield", [("shield_heater_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  673 , weight(5.5)|difficulty(3)|hit_points(322)|body_armor(22)|spd_rtng(95)|shield_width(24)|shield_height(51),imodbits_shield ],

#["shield_kite_g",         "Blue and Purple Kite Shield", [("shield_kite_g",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  532 , weight(6.5)|difficulty(3)|hit_points(380)|body_armor(24)|spd_rtng(87)|shield_width(25)|shield_height(80),imodbits_shield ],
["shield_kite_h",         "White Black and Red Kite Shield", [("shield_kite_h",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(6)|difficulty(3)|hit_points(380)|body_armor(20)|spd_rtng(89)|shield_width(25)|shield_height(89),imodbits_shield ],
["shield_kite_i",         "Brown Kite Shield", [("shield_kite_i",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(3.5)|hit_points(300)|difficulty(3)|body_armor(20)|spd_rtng(96)|shield_width(25)|shield_height(53),imodbits_shield ],
["shield_kite_k",         "Black and White Kite Shield", [("shield_kite_k",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(3.5)|hit_points(300)|difficulty(3)|body_armor(20)|spd_rtng(96)|shield_width(25)|shield_height(83),imodbits_shield ],

["norman_shield_1",         "Brown Heavy Norman Shield", [("norman_shield_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  258 , weight(7.5)|difficulty(4)|hit_points(480)|body_armor(24)|spd_rtng(85)|shield_width(25)|shield_height(95),imodbits_shield ],
["norman_shield_2",         "Green Norman Shield", [("norman_shield_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(6)|difficulty(3)|hit_points(380)|body_armor(20)|spd_rtng(89)|shield_width(25)|shield_height(95),imodbits_shield ],
["norman_shield_3",         "Blue Heavy Norman Shield", [("norman_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  258 , weight(7.5)|difficulty(4)|hit_points(480)|body_armor(24)|spd_rtng(85)|shield_width(25)|shield_height(95),imodbits_shield ],
["norman_shield_4",         "Yellow Norman Shield", [("norman_shield_4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(6)|difficulty(3)|hit_points(380)|body_armor(20)|spd_rtng(89)|shield_width(25)|shield_height(95),imodbits_shield ],
["norman_shield_5",         "Dark Blue Heavy Norman Shield", [("norman_shield_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  258 , weight(7.5)|difficulty(4)|hit_points(480)|body_armor(24)|spd_rtng(85)|shield_width(25)|shield_height(95),imodbits_shield ],
["norman_shield_6",         "Dark Red Heavy Norman Shield", [("norman_shield_6",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  258 , weight(7.5)|difficulty(4)|hit_points(480)|body_armor(24)|spd_rtng(85)|shield_width(25)|shield_height(95),imodbits_shield ],
["norman_shield_7",         "White Heavy Norman Shield", [("norman_shield_7",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  258 , weight(7.5)|difficulty(4)|hit_points(480)|body_armor(24)|spd_rtng(85)|shield_width(25)|shield_height(95),imodbits_shield ],
#["norman_shield_8",         "Purple Norman Shield", [("norman_shield_8",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(6)|difficulty(3)|hit_points(380)|body_armor(20)|spd_rtng(89)|shield_width(25)|shield_height(95),imodbits_shield ],

["tab_shield_round_a", "Old Round Shield", [("tableau_shield_round_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
25 , weight(2.2)|hit_points(260)|body_armor(10)|spd_rtng(96)|shield_width(35),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_5", ":agent_no", ":troop_no")])]],
["tab_shield_round_b", "Plain Round Shield", [("tableau_shield_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
65 , weight(4)|difficulty(2)|hit_points(285)|body_armor(16)|spd_rtng(98)|shield_width(39),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_round_c", "Round Shield", [("tableau_shield_round_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
105 , weight(5.5)|difficulty(3)|hit_points(300)|body_armor(20)|spd_rtng(90)|shield_width(39),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_round_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_round_d", "Heavy Round Shield", [("tableau_shield_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
210 , weight(6.5)|difficulty(4)|hit_points(349)|body_armor(23)|spd_rtng(85)|shield_width(39),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_round_e", "Huscarl's Round Shield", [("tableau_shield_round_4",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  
430 , weight(8)|difficulty(5)|hit_points(400)|body_armor(26)|spd_rtng(80)|shield_width(42),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_4", ":agent_no", ":troop_no")])]],

["tab_shield_kite_a", "Old Kite Shield",   [("tableau_shield_kite_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
33 , weight(2.5)|difficulty(0)|hit_points(270)|body_armor(14)|spd_rtng(97)|shield_width(22)|shield_height(90),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_kite_b", "Plain Kite Shield",   [("tableau_shield_kite_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
77 , weight(3)|difficulty(2)|hit_points(330)|body_armor(16)|spd_rtng(94)|shield_width(22)|shield_height(90),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_kite_c", "Kite Shield",   [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
156 , weight(3)|difficulty(3)|hit_points(385)|body_armor(16)|spd_rtng(96)|shield_width(22)|shield_height(90),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_kite_d", "Heavy Kite Shield",   [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
320 , weight(4.5)|difficulty(4)|hit_points(370)|body_armor(23)|spd_rtng(96)|shield_width(22)|shield_height(90),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_kite_cav_a", "Horseman's Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
204 , weight(2.5)|difficulty(2)|hit_points(260)|body_armor(18)|spd_rtng(100)|shield_width(23)|shield_height(63),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])]],
["tab_shield_kite_cav_b", "Knightly Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,  
360 , weight(3)|difficulty(5)|hit_points(270)|body_armor(29)|spd_rtng(103)|shield_width(23)|shield_height(63),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])]],

 
 ["tab_shield_heater_a", "Old Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
36 , weight(2.7)|difficulty(0)|hit_points(250)|body_armor(15)|spd_rtng(96)|shield_width(23)|shield_height(86),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_b", "Plain Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
74 , weight(3.2)|difficulty(2)|hit_points(310)|body_armor(17)|spd_rtng(93)|shield_width(23)|shield_height(86),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_c", "Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
160 , weight(6)|difficulty(3)|hit_points(360)|body_armor(22)|spd_rtng(92)|shield_width(23)|shield_height(86),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_d", "Heavy Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
332 , weight(7)|difficulty(4)|hit_points(460)|body_armor(27)|spd_rtng(90)|shield_width(23)|shield_height(86),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_cav_a", "Horseman's Heater Shield",   [("tableau_shield_heater_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
229 , weight(3.5)|difficulty(2)|hit_points(220)|body_armor(25)|spd_rtng(100)|shield_width(25)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_heater_cav_b", "Knightly Heater Shield",   [("tableau_shield_heater_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
390 , weight(2.5)|difficulty(4)|hit_points(232)|body_armor(35)|spd_rtng(101)|shield_width(25)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])]],

 ["tab_shield_pavise_a", "Old Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,  
60 , weight(5)|difficulty(0)|hit_points(370)|body_armor(15)|spd_rtng(89)|shield_width(30)|shield_height(84),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_b", "Plain Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,  
114 , weight(6)|difficulty(2)|hit_points(435)|body_armor(16)|spd_rtng(89)|shield_width(30)|shield_height(84),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_c", "Board Shield",   [("tableau_shield_pavise_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,  
210 , weight(7.5)|difficulty(3)|hit_points(500)|body_armor(17)|spd_rtng(86)|shield_width(30)|shield_height(84),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_d", "Heavy Board Shield",   [("tableau_shield_pavise_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,  
370 , weight(9)|difficulty(4)|hit_points(600)|body_armor(17)|spd_rtng(80)|shield_width(30)|shield_height(84),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],

["tab_shield_small_round_a", "Plain Cavalry Shield", [("tableau_shield_small_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
96 , weight(3)|difficulty(0)|hit_points(250)|body_armor(14)|spd_rtng(105)|shield_width(33),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_b", "Round Cavalry Shield", [("tableau_shield_small_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
195 , weight(3.5)|difficulty(2)|hit_points(210)|body_armor(22)|spd_rtng(100)|shield_width(32),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_c", "Elite Cavalry Shield", [("tableau_shield_small_round_2",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  
370 , weight(4.5)|difficulty(4)|hit_points(250)|body_armor(25)|spd_rtng(100)|shield_width(32),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":agent_no", ":troop_no")])]],


 ####################################### SHIELDS
 
 
["lithuanian_shield",         "Lithuanian Shield", [("shield_1_big",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
343 , weight(2.5)|hit_points(340)|body_armor(23)|spd_rtng(97)|shield_width(58)|shield_height(60)|difficulty(3),imodbits_shield ],

#["steel_buckler_a", "Round Steel Buckler", [("steel_buckler1",0)], itp_merchandise|itp_type_shield, itcf_carry_buckler_left ,  
#314 , weight(1.5)|difficulty(3)|hit_points(130)|body_armor(50)|spd_rtng(107)|shield_width(6),imodbits_shield ],

#["steel_buckler_b", "Steel Buckler", [("steel_buckler2",0)], itp_merchandise|itp_type_shield, itcf_carry_buckler_left ,  
#432 , weight(2.5)|difficulty(5)|hit_points(150)|body_armor(62)|spd_rtng(104)|shield_width(4)|shield_height(2),imodbits_shield ],

 
["hand_pavise_a",         "Long Pavise Shield", [("hand_pavise",0)], itp_merchandise|itp_type_shield|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield,  
356 , weight(10)|difficulty(5)|hit_points(620)|body_armor(21)|spd_rtng(81)|shield_width(30)|shield_height(62)|difficulty(5),imodbits_shield ],

["hand_pavise_b",         "Hand Pavise Shield", [("hand_pavise_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
377 , weight(5.5)|difficulty(5)|hit_points(365)|body_armor(25)|spd_rtng(100)|shield_width(28)|shield_height(60)|difficulty(5),imodbits_shield ],

["triangle_shield",         "Triangle Shield", [("triangle_shield_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,  
385 , weight(5.5)|difficulty(5)|hit_points(440)|body_armor(20)|spd_rtng(97)|shield_width(24)|shield_height(92)|difficulty(5),imodbits_shield ],



 #RANGED


#TODO:
["darts",         "Darts", [("dart_b",0),("dart_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn, 
211 , weight(4)|difficulty(1)|spd_rtng(95) | shoot_speed(28) | thrust_damage(22 ,  pierce)|max_ammo(8)|weapon_length(32),imodbits_thrown ],
["war_darts",         "War Darts", [("dart_a",0),("dart_a_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
324 , weight(5)|difficulty(1)|spd_rtng(93) | shoot_speed(27) | thrust_damage(25 ,  pierce)|max_ammo(8)|weapon_length(45),imodbits_thrown ],

["javelin",         "Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
424, weight(4)|difficulty(1)|spd_rtng(91) | shoot_speed(25) | thrust_damage(34 ,  pierce)|max_ammo(6)|weapon_length(75),imodbits_thrown ],
["javelin_melee",         "Javelin", [("javelin",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff, 
424, weight(1)|difficulty(11)|spd_rtng(95) |swing_damage(12, cut)| thrust_damage(14,  pierce)|weapon_length(75),imodbits_polearm ],

["throwing_spears",         "Throwing Spears", [("jarid_new_b",0),("jarid_new_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
740 , weight(3)|difficulty(2)|spd_rtng(87) | shoot_speed(22) | thrust_damage(44 ,  pierce)|max_ammo(6)|weapon_length(65),imodbits_thrown ],
["throwing_spear_melee",         "Throwing Spear", [("jarid_new_b",0),("javelins_quiver", ixmesh_carry)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff, 
740 , weight(1)|difficulty(11)|spd_rtng(91) | swing_damage(18, cut) | thrust_damage(23 ,  pierce)|weapon_length(75),imodbits_thrown ],

["jarid",         "Jarids", [("jarid_new",0),("jarid_quiver", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
665 , weight(2.75)|difficulty(2)|spd_rtng(89) | shoot_speed(24) | thrust_damage(45 ,  pierce)|max_ammo(5)|weapon_length(65),imodbits_thrown ],
["jarid_melee",         "Jarid", [("jarid_new",0),("jarid_quiver", ixmesh_carry)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff,
665 , weight(1)|difficulty(11)|spd_rtng(93) | swing_damage(16, cut) | thrust_damage(20 ,  pierce)|weapon_length(65),imodbits_thrown ],


#TODO:
#TODO: Heavy throwing Spear
["stones",         "Stones", [("throwing_stone",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_stone, 
 1 , weight(4)|difficulty(0)|spd_rtng(97) | shoot_speed(30) | thrust_damage(11 ,  blunt)|max_ammo(24)|weapon_length(8),imodbit_large_bag ],

["throwing_knives", "Throwing Knives", [("throwing_knife",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 
 76 , weight(2.5)|difficulty(1)|spd_rtng(121) | shoot_speed(25) | thrust_damage(22 ,  cut)|max_ammo(6)|weapon_length(0),imodbits_thrown ],
["throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 
 93 , weight(2.5)|difficulty(1)|spd_rtng(110) | shoot_speed(24) | thrust_damage(27 ,  cut)|max_ammo(6)|weapon_length(0),imodbits_thrown ],
#TODO: Light Trowing axe, Heavy Throwing Axe
["light_throwing_axes", "Light Throwing Axes", [("francisca",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
 443, weight(5)|difficulty(2)|spd_rtng(99) | shoot_speed(18) | thrust_damage(35,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown_minus_heavy ],
["light_throwing_axes_melee", "Light Throwing Axe", [("francisca",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
 443, weight(1)|difficulty(11)|spd_rtng(99)|weapon_length(53)| swing_damage(26,cut),imodbits_thrown_minus_heavy ],
["throwing_axes", "Throwing Axes", [("throwing_axe_a",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
 546, weight(5)|difficulty(3)|spd_rtng(98) | shoot_speed(18) | thrust_damage(39,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["throwing_axes_melee", "Throwing Axe", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
 546, weight(1)|difficulty(11)|spd_rtng(98) | swing_damage(29,cut)|weapon_length(53),imodbits_thrown_minus_heavy ],
["heavy_throwing_axes", "Heavy Throwing Axes", [("throwing_axe_b",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
 733, weight(5)|difficulty(4)|spd_rtng(97) | shoot_speed(18) | thrust_damage(44,cut)|max_ammo(3)|weapon_length(53),imodbits_thrown_minus_heavy ],
["heavy_throwing_axes_melee", "Heavy Throwing Axe", [("throwing_axe_b",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
 733, weight(1)|difficulty(11)|spd_rtng(97) | swing_damage(32,cut)|weapon_length(53),imodbits_thrown_minus_heavy ],



["hunting_bow",         "Hunting Bow", [("hunting_bow",0),("hunting_bow_carry",ixmesh_carry)],itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 
17 , weight(1.7)|difficulty(0)|accuracy(95)|spd_rtng(100) | shoot_speed(50) | thrust_damage(16 ,  pierce),imodbits_bow ],
["short_bow",         "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
57 , weight(2)|difficulty(1)|accuracy(95)|spd_rtng(97) | shoot_speed(51) | thrust_damage(18 ,  pierce  ),imodbits_bow ],
["nomad_bow",         "Nomad Bow", [("nomad_bow",0),("nomad_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
166 , weight(2.4)|difficulty(2)|accuracy(96)|spd_rtng(97) | shoot_speed(53) | thrust_damage(17 ,  pierce),imodbits_bow ],

############################       NEW           ###########

#["rus_bow",         "Rus Bow", [("rus_bow_h1",0),("rus_bow_carry_h1",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
#145 , weight(3.75)|difficulty(6)|accuracy(104)|spd_rtng(55) | shoot_speed(42) | thrust_damage(26 ,  pierce),imodbits_bow ],

#["long_bow_b",         "Long Bow", [("long_bow_h1",0),("long_bow_carry_h1",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
#145 , weight(4)|difficulty(6)|accuracy(105)|spd_rtng(51) | shoot_speed(42) | thrust_damage(28 ,  pierce),imodbits_bow ],

#["yumi",         "Yumi", [("yumi_h1",0),("yumi_carry_h1",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
#145 , weight(3.2)|difficulty(6)|accuracy(104)|spd_rtng(59) | shoot_speed(40) | thrust_damage(24 ,  pierce),imodbits_bow ],

#["horn_bow",         "Horn Bow", [("horn_bow_h1",0),("horn_bow_scabbard_h1", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
#269 , weight(2.7)|difficulty(5)|accuracy(103)|spd_rtng(61) | shoot_speed(40) | thrust_damage(22 ,pierce),imodbits_bow ],

#["bow_a",         "Bow", [("bow_h1",0),("bow_carry_h1",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
#100 , weight(3.5)|difficulty(4)|spd_rtng(58) | shoot_speed(42) | thrust_damage(25 ,  pierce  ),imodbits_bow ],



["long_bow",         "Long Bow", [("long_bow",0),("long_bow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_use_on_horseback ,itcf_shoot_bow|itcf_carry_bow_back, 
145 , weight(4)|difficulty(3)|accuracy(100)|spd_rtng(79) | shoot_speed(56) | thrust_damage(24 ,  pierce),imodbits_bow ],
["khergit_bow",         "Tatar Bow", [("khergit_bow",0),("khergit_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
277 , weight(2.4)|difficulty(3)|accuracy(97)|spd_rtng(94) | shoot_speed(59) | thrust_damage(19 ,pierce),imodbits_bow ],
["strong_bow",         "Strong Bow", [("strong_bow",0),("strong_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
455 , weight(2.7)|difficulty(3)|accuracy(97)|spd_rtng(88) | shoot_speed(61) | thrust_damage(20 ,pierce),imodbit_cracked | imodbit_bent | imodbit_masterwork ],
["war_bow",         "War Bow", [("war_bow",0),("war_bow_carry",ixmesh_carry)],itp_type_bow|itp_merchandise|itp_primary|itp_two_handed|itp_cant_use_on_horseback ,itcf_shoot_bow|itcf_carry_bow_back, 
728 , weight(3.7)|difficulty(4)|accuracy(98)|spd_rtng(84) | shoot_speed(60) | thrust_damage(23 ,pierce),imodbits_bow ],
["hunting_crossbow", "Hunting Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
33 , weight(2.7)|difficulty(7)|accuracy(87)|spd_rtng(94) | shoot_speed(50) | thrust_damage(36 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["light_crossbow", "Light Crossbow", [("crossbow_b",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
70 , weight(3)|difficulty(9)|accuracy(86)|spd_rtng(90) | shoot_speed(59) | thrust_damage(41 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["crossbow",         "Crossbow",         [("crossbow_a",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
182 , weight(3.5)|difficulty(12)|accuracy(90)|spd_rtng(86) | shoot_speed(66) | thrust_damage(46,pierce)|max_ammo(1),imodbits_crossbow ],
["heavy_crossbow", "Heavy Crossbow", [("crossbow_c",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
360 , weight(4)|difficulty(13)|accuracy(92)|spd_rtng(82) | shoot_speed(68) | thrust_damage(54 ,pierce)|max_ammo(1),imodbits_crossbow ],
["sniper_crossbow", "Siege Crossbow", [("crossbow_c",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
754 , weight(4.5)|difficulty(14)|accuracy(95)|spd_rtng(74) | shoot_speed(70) | thrust_damage(65 ,pierce)|max_ammo(1),imodbits_crossbow ],
["flintlock_pistol", "Flintlock Pistol", [("flintlock_pistol",0)], itp_type_pistol |itp_primary ,itcf_shoot_pistol|itcf_reload_pistol, 230 , weight(1.5)|difficulty(0)|spd_rtng(38) | shoot_speed(160) | thrust_damage(150 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["torch",         "Torch", [("club",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar, 11 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none,
 [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),
])]],

["lyre",         "Lyre", [("lyre",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
["lute",         "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],

##["short_sword", "Short Sword",
## [("sword_norman",0),("sword_norman_scabbard", ixmesh_carry),("sword_norman_rusty",imodbit_rusty),("sword_norman_rusty_scabbard", ixmesh_carry|imodbit_rusty)],
## itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(75)|swing_damage(25 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],

#["strange_armor",  "Strange Armor", [("samurai_armor",0)], itp_type_body_armor|itp_merchandise  |itp_covers_legs ,0, 
# 2831 , weight(12.4)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(17)|difficulty(10) ,imodbits_armor ],
#["strange_boots",  "Strange Boots", [("samurai_boots",0)], itp_type_foot_armor|itp_merchandise | itp_attach_armature,0, 
# 602 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(19)|difficulty(6) ,imodbits_cloth ],
#["strange_helmet", "Strange Helmet", [("samurai_helmet",0)], itp_type_head_armor|itp_merchandise   ,0, 
# 2169 , weight(2.1)|abundance(100)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
#["strange_sword", "Katana", [("katana",0),("katana_scabbard",ixmesh_carry)], itp_type_two_handed_wpn| itp_primary|itp_merchandise, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 
# 1241 , weight(1.5)|difficulty(9)|spd_rtng(100) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(21 ,  pierce),imodbits_sword ],
#["strange_great_sword",  "Nodachi", [("no_dachi",0),("no_dachi_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_merchandise, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn,
# 1765 , weight(3)|difficulty(12)|spd_rtng(92) | weapon_length(122)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["strange_short_sword", "Wakizashi", [("wakizashi",0),("wakizashi_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_merchandise, itc_longsword|itcf_carry_wakizashi|itcf_show_holster_when_drawn, 
# 975 , weight(1)|difficulty(0)|spd_rtng(104) | weapon_length(65)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
["court_dress", "Court Dress", [("court_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 
 473 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["rich_outfit", "Rich Outfit", [("merchant_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 
 453 , weight(0.7)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
#["leather_steppe_cap_c", "Leather Steppe Cap", [("leather_steppe_cap_c",0)], itp_type_head_armor   ,0, 51 , weight(2)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#["felt_steppe_cap", "Felt Steppe Cap", [("felt_steppe_cap",0)], itp_type_head_armor   ,0, 
# 788 , weight(0.4)|abundance(100)|head_armor(17)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#["khergit_sword", "Khergit Sword", [("khergit_sword",0),("khergit_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(23 , cut) | thrust_damage(14 ,  pierce),imodbits_sword ],


#["byzantion_helmet_a", "Byzantion Helmet", [("byzantion_helmet_a",0)], itp_type_head_armor|itp_merchandise   ,0, 
# 278 , weight(1.2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#["rus_helmet_a", "Rus Helmet", [("rus_helmet_a",0)], itp_type_head_armor|itp_merchandise   ,0,
# 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["keys", "Ring of Keys", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
240, weight(5)|spd_rtng(98) | swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown ], 
["bride_dress", "Bride Dress", [("bride_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["bride_crown", "Crown of Flowers", [("bride_crown",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bride_shoes", "Bride Shoes", [("bride_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["practice_bow_2","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
["practice_arrows_2","Practice Arrows", [("arena_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],



["heraldic_mail_with_surcoat_for_tableau", "{!}Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_type_body_armor |itp_covers_legs ,0,
 1, weight(22)|abundance(100)|head_armor(0)|body_armor(1)|leg_armor(1),imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],
["mail_boots_for_tableau", "Mail Boots", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1, weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],


 #barded_warhorse_heraldic	heraldic_horse_bg	tableau_mesh_barded_warhorse_heraldic
 
#colored_pelt_hood



 
 

["rider_pistol", "Flintlock Pistol", [("flintlock_pistol",0)], itp_type_pistol|itp_no_pick_up_from_ground|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol, 230 , weight(0.1)|difficulty(0)|spd_rtng(900) | shoot_speed(300) | thrust_damage(150 ,pierce)|max_ammo(800)|accuracy(600),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],

["mitsubiszi", "Mitsubiszi", [("one_handed_war_axe_b",0)], itp_crush_through|itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 544 , weight(10.2)|difficulty(8)|spd_rtng(200) | weapon_length(71)|swing_damage(63 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

# ["heraldic_tunic_over_mail", "Heraldic Tunic over Mail", [("blue_tunic_over_mail",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 # 2179 , weight(11.1)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(13)|difficulty(10) ,imodbits_armor,
 # [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_h", ":agent_no", ":troop_no")])]],

#########OWSwords_v2






["items_end", "Items End", [("shield_round_a",0)], 0, 0, 1, 0, 0],


##INVASION MODE START
["javelin_bow",         "Javelin Bow", [("war_bow",0),("war_bow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
0 , weight(1.5)|difficulty(0)|spd_rtng(84) | shoot_speed(59) | thrust_damage(25 ,pierce), 0, [(ti_on_weapon_attack, [(play_sound,"snd_throw_javelin")])] ],
["knockdown_mace",         "Knockdown Mace", [("flanged_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
0 , weight(3.5)|difficulty(0)|spd_rtng(103) | weapon_length(70)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["blood_drain_throwing_knives", "Blood Drain Throwing Knives", [("throwing_knife",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(2.5)|difficulty(0)|spd_rtng(121) | shoot_speed(25) | thrust_damage(25 ,  pierce)|max_ammo(5)|weapon_length(0),imodbits_thrown ],
["doom_javelins",         "Doom Javelins", [("jarid_new_b",0),("jarid_new_b_bag", ixmesh_carry)], itp_type_thrown |itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
0 , weight(3)|difficulty(0)|spd_rtng(87) | shoot_speed(22) | thrust_damage(44 ,  pierce)|max_ammo(2)|weapon_length(65),imodbits_thrown ],
#["unblockable_morningstar",         "Unblockable Morningstar", [("mace_morningstar_new",0)], itp_crush_through|itp_type_two_handed_wpn|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_mace_left_hip, 
#305 , weight(20)|difficulty(13)|spd_rtng(95) | weapon_length(85)|swing_damage(38 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["disarming_throwing_axe", "Disarming Throwing Axe", [("throwing_axe_a",0)], itp_type_thrown |itp_primary,itcf_throw_axe,
0, weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(18) | thrust_damage(10,cut)|max_ammo(1)|weapon_length(53),imodbits_thrown_minus_heavy ],
["instakill_knife",         "Instakill Knife", [("peasant_knife_new",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_two_handed, itc_dagger|itcf_carry_dagger_front_left, 
0 , weight(0.5)|difficulty(0)|spd_rtng(101) | weapon_length(40)|swing_damage(21 , cut) | thrust_damage(13 ,  pierce),imodbits_sword ],
["backstabber", "Backstabber", [("sword_viking_a_small",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
0 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(86)|swing_damage(20 , cut) | thrust_damage(13 ,  pierce),imodbits_sword_high ],
["weak_beserker_dart",         "Weak Beserker Dart", [("dart_b",0),("dart_b_bag", ixmesh_carry)], itp_type_thrown |itp_primary ,itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn, 
0 , weight(4)|difficulty(0)|spd_rtng(95) | shoot_speed(28) | thrust_damage(5 ,  pierce)|max_ammo(1)|weapon_length(32),imodbits_thrown ],
["team_change_dart",         "Team Change Dart", [("dart_a",0),("dart_a_bag", ixmesh_carry)], itp_type_thrown |itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
0 , weight(5)|difficulty(0)|spd_rtng(93) | shoot_speed(27) | thrust_damage(5 ,  pierce)|max_ammo(1)|weapon_length(45),imodbits_thrown ],
["awesome_spear",         "Awesome Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff|itcf_carry_spear, 
0 , weight(1.5)|difficulty(0)|spd_rtng(110) | weapon_length(157)|swing_damage(41 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm ],


["running_boots",  "Running Boots", [("samurai_boots",0)], itp_type_foot_armor | itp_attach_armature,0, 0 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_cloth ],
["power_gloves","Power Gloves", [("scale_gauntlets_a_L",0)], itp_type_hand_armor,0, 0, weight(0.9)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
#["wielding_gloves","Wielding Gloves", [("scale_gauntlets_b_L",0)], itp_type_hand_armor,0, 0, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor],
["invulnerable_helmet", "Invulnerable Helmet", [("maciejowski_helmet_new",0)], itp_type_head_armor|itp_covers_head,0, 1240 , weight(2.75)|abundance(100)|head_armor(63)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
["kicking_boots", "Kicking Boots", [("sarranid_camel_boots",0)],  itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 0 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_plate ],
["restore_health_armour",  "Restore Health Armour", [("samurai_armor",0)], itp_type_body_armor  |itp_covers_legs ,0, 0 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(11)|difficulty(0) ,imodbits_armor ],
#["extra_life_helmet", "Extra Life Helmet", [("byzantion_helmet_a",0)], itp_type_head_armor   ,0, 0 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#["scatter_crossbow", "Scatter Crossbow", [("crossbow_c",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
#0 , weight(3.75)|spd_rtng(20) | shoot_speed(90) | thrust_damage(90 ,pierce)|max_ammo(1),imodbits_crossbow ],

#additional items for coop
["javelin_bow_ammo",         "Shooting Javelins", [("javelin_bow_ammo",0),("javelins_quiver_new", ixmesh_carry)], itp_type_arrows|itp_default_ammo ,itcf_carry_quiver_back, 
0, weight(4) | thrust_damage(34 ,  pierce)|max_ammo(15)|weapon_length(75),0 ],
#["scatter_bolts","Scatter Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 
#0,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(1,pierce)|max_ammo(4),imodbits_missile],
["ccoop_new_items_end", "Items End", [("shield_round_a",0)], 0, 0, 1, 0, 0],
#INVASION MODE END

]
