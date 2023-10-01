from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
  ("looters","Looters",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,3,45)]),
# Ryan END
  ("manhunters","Manhunters",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_manhunter,9,40)]),
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),
  ("steppe_bandits","Steppe Bandits",icon_khergit|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_steppe_bandit_leader,0,1),(trp_steppe_bandit,4,20),(trp_steppe_bandit_archer,0,20),(trp_steppe_bandit_lancer,0,20)]),
  ("taiga_bandits","Tundra Bandits",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_taiga_bandit,4,58)]),
  ("desert_bandits","Desert Bandits",icon_vaegir_knight|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_desert_bandits_leader,0,1),(trp_desert_horse_warrior,0,20),(trp_desert_horse_archer,0,20),(trp_desert_bandit,4,20)]),
  ("forest_bandits","Forest Bandits",icon_axeman|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit_leader,0,1),(trp_forest_fighters,0,20),(trp_forest_archer,0,20),(trp_forest_bandit,4,20)]),
  ("mountain_bandits","Mountain Bandits",icon_axeman|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_mountain_leader,0,1),(trp_mountain_warrior,0,20),(trp_mountain_archer,0,20),(trp_mountain_bandit,4,20)]),
  ("sea_raiders","Sea Raiders",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_sea_raider_leader_a,0,1),(trp_sea_raider,0,30),(trp_sea_raider_light,5,20)]),

  ("deserters","Deserters",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),
    
  ("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(40)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),	### 28.07.2018   carries_goods - was 20
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),

  ("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
  ("village_patrol_party","Patrol",icon_gray_knight|carries_goods(5)|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(40)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,12,40)]), ##carries_goods was 25
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
  ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),  

  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total

  ("player_reinforcements_a", "{!}player_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_player_recruit,4,8),(trp_player_footman,3,6)]),
  ("player_reinforcements_b", "{!}player_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_player_trained_footman,3,6),(trp_player_skirmisher,2,4)]),
  ("player_reinforcements_c", "{!}player_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_player_archer,1,2),(trp_player_horseman,2,3)]),

  
  
  ("neutrals_reinforcements_swadian_a", "{!}neutrals_reinforcements_swadian_a", 0, 0, fac_commoners, 0, [(trp_swadian_militia_merc,4,8),(trp_swadian_militia_merc,3,6)]),
  ("neutrals_reinforcements_swadian_b", "{!}neutrals_reinforcements_swadian_b", 0, 0, fac_commoners, 0, [(trp_swadian_footman_merc,2,4),(trp_swadian_crossbowman_merc,3,6)]),
  ("neutrals_reinforcements_swadian_c", "{!}neutrals_reinforcements_swadian_c", 0, 0, fac_commoners, 0, [(trp_swadian_infantry_merc,2,3),(trp_swadian_man_at_arms_merc,1,2)]),

  ("neutrals_reinforcements_vaegirs_a", "{!}neutrals_reinforcements_vaegirs_a", 0, 0, fac_commoners, 0, [(trp_vaegir_footman_merc,4,8),(trp_vaegir_footman_merc,3,6)]),
  ("neutrals_reinforcements_vaegirs_b", "{!}neutrals_reinforcements_vaegirs_b", 0, 0, fac_commoners, 0, [(trp_vaegir_skirmisher_merc,2,4),(trp_vaegir_veteran_merc,3,6)]),
  ("neutrals_reinforcements_vaegirs_c", "{!}neutrals_reinforcements_vaegirs_c", 0, 0, fac_commoners, 0, [(trp_vaegir_infantry_merc,2,3),(trp_vaegir_horseman_merc,1,2)]),

  ("neutrals_reinforcements_khergits_a", "{!}neutrals_reinforcements_khergits_a", 0, 0, fac_commoners, 0, [(trp_khergit_skirmisher_merc,4,8),(trp_khergit_skirmisher_merc,3,6)]),
  ("neutrals_reinforcements_khergits_b", "{!}neutrals_reinforcements_khergits_b", 0, 0, fac_commoners, 0, [(trp_khergit_horseman_merc,2,4),(trp_khergit_horse_archer_merc,3,6)]),
  ("neutrals_reinforcements_khergits_c", "{!}neutrals_reinforcements_khergits_c", 0, 0, fac_commoners, 0, [(trp_khergit_veteran_horse_archer_merc,2,3),(trp_khergit_lancer_merc,1,2)]),

  ("neutrals_reinforcements_nords_a", "{!}neutrals_reinforcements_nords_a", 0, 0, fac_commoners, 0, [(trp_nord_footman_merc,4,8),(trp_nord_footman_merc,3,6)]),
  ("neutrals_reinforcements_nords_b", "{!}neutrals_reinforcements_nords_b", 0, 0, fac_commoners, 0, [(trp_nord_trained_footman_merc,2,4),(trp_nord_huntsman_merc,3,6)]),
  ("neutrals_reinforcements_nords_c", "{!}neutrals_reinforcements_nords_c", 0, 0, fac_commoners, 0, [(trp_nord_warrior_merc,2,3),(trp_nord_archer_merc,1,2)]),

  ("neutrals_reinforcements_rhodoks_a", "{!}neutrals_reinforcements_rhodoks_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman_merc,4,8),(trp_rhodok_spearman_merc,3,6)]),
  ("neutrals_reinforcements_rhodoks_b", "{!}neutrals_reinforcements_rhodoks_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman_merc,2,4),(trp_rhodok_crossbowman_merc,3,6)]),
  ("neutrals_reinforcements_rhodoks_c", "{!}neutrals_reinforcements_rhodoks_c", 0, 0, fac_commoners, 0, [(trp_rhodok_veteran_spearman_merc,2,3),(trp_rhodok_trained_crossbowman_merc,1,2)]),

  ("neutrals_reinforcements_sarranids_a", "{!}neutrals_reinforcements_sarranids_a", 0, 0, fac_commoners, 0, [(trp_sarranid_footman_merc,4,8),(trp_sarranid_footman_merc,3,6)]),
  ("neutrals_reinforcements_sarranids_b", "{!}neutrals_reinforcements_sarranids_b", 0, 0, fac_commoners, 0, [(trp_sarranid_veteran_footman_merc,2,4),(trp_sarranid_skirmisher_merc,3,6)]),
  ("neutrals_reinforcements_sarranids_c", "{!}neutrals_reinforcements_sarranids_c", 0, 0, fac_commoners, 0, [(trp_sarranid_infantry_merc,2,3),(trp_sarranid_horseman_merc,1,2)]),

  
  
  ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_recruit,5,8),(trp_swadian_militia,2,6)]), ##14
  ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_footman,2,4),(trp_swadian_skirmisher,2,4),(trp_swadian_man_at_arms,1,2)]), ##6
  ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,2,3),(trp_swadian_infantry,1,2)]), #5

  ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_recruit,5,8),(trp_vaegir_footman,2,6)]),
  ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,2,4),(trp_vaegir_archer,2,4),(trp_vaegir_footman,1,2)]),
  ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,1,2),(trp_vaegir_infantry,2,3)]),

  ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_tribesman,5,8),(trp_khergit_footman,2,6)]), #
  ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_warrior,2,4),(trp_khergit_skirmisher,2,4),(trp_khergit_footman,1,2)]),
  ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,2,3),(trp_khergit_veteran_warrior,1,2)]), #

  ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_recruit,5,8),(trp_nord_footman,2,6)]),
  ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_trained_footman,2,4),(trp_nord_huntsman,2,4),(trp_nord_footman,1,2)]),
  ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_horseman,2,3),(trp_nord_warrior,1,2)]),

  ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_tribesman,5,8),(trp_rhodok_spearman,2,6)]),
  ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman,2,4),(trp_rhodok_crossbowman,2,4),(trp_rhodok_spearman,1,2)]),
  ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_horseman,2,3),(trp_rhodok_veteran_spearman,1,2)]), 

  ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sarranid_recruit,5,8),(trp_sarranid_footman,2,6)]),
  ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sarranid_veteran_footman,2,4),(trp_sarranid_skirmisher,2,4),(trp_sarranid_footman,1,2)]),
  ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sarranid_horseman,2,3),(trp_sarranid_infantry,1,2)]),

  ("kingdom_7_reinforcements_a", "{!}kingdom_7_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_eques_tribesman,5,8),(trp_eques_spearman,2,6)]),
  ("kingdom_7_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_eques_trained_spearman,2,4),(trp_eques_crossbowman,2,4),(trp_eques_spearman,1,2)]),
  ("kingdom_7_reinforcements_c", "{!}kingdom_7_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_eques_horseman,2,3),(trp_eques_veteran_spearman,1,2)]), 

  ("kingdom_8_reinforcements_a", "{!}kingdom_8_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_norse_recruit,5,8),(trp_norse_footman,2,6)]),
  ("kingdom_8_reinforcements_b", "{!}kingdom_8_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_norse_trained_footman,2,4),(trp_norse_archer,2,4),(trp_norse_footman,1,2)]),
  ("kingdom_8_reinforcements_c", "{!}kingdom_8_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_norse_warrior,2,3),(trp_norse_axeman,1,2)]), 

  ("kingdom_9_reinforcements_a", "{!}kingdom_9_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_order_recruit,5,8),(trp_order_footman,2,6)]),
  ("kingdom_9_reinforcements_b", "{!}kingdom_9_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_order_trained_footman,2,4),(trp_order_crossbowman,2,4),(trp_order_nobleman,1,2)]),
  ("kingdom_9_reinforcements_c", "{!}kingdom_9_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_order_veteran_footman,2,3),(trp_order_knight,1,2)]), 

##  ("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_footman,3,7),(trp_swadian_skirmisher,5,10),(trp_swadian_militia,11,26)]),
##  ("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,5,10),(trp_swadian_infantry,5,10),(trp_swadian_crossbowman,3,8)]),
##  ("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_knight,2,6),(trp_swadian_sergeant,2,5),(trp_swadian_sharpshooter,2,5)]),
##
##  ("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,3,7),(trp_vaegir_skirmisher,5,10),(trp_vaegir_footman,11,26)]),
##  ("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,4,9),(trp_vaegir_infantry,5,10),(trp_vaegir_archer,3,8)]),
##  ("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_knight,3,7),(trp_vaegir_guard,2,5),(trp_vaegir_marksman,2,5)]),
##
##  ("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,3,7),(trp_khergit_skirmisher,5,10),(trp_khergit_tribesman,11,26)]),
##  ("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_veteran_horse_archer,4,9),(trp_khergit_horse_archer,5,10),(trp_khergit_horseman,3,8)]),
##  ("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_lancer,3,7),(trp_khergit_veteran_horse_archer,2,5),(trp_khergit_horse_archer,2,5)]),
##
##  ("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_trained_footman,3,7),(trp_nord_footman,5,10),(trp_nord_recruit,11,26)]),
##  ("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_veteran,4,9),(trp_nord_warrior,5,10),(trp_nord_footman,3,8)]),
##  ("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_champion,1,3),(trp_nord_veteran,2,5),(trp_nord_warrior,2,5)]),
##
##  ("kingdom_5_reinforcements_a", "kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,3,7),(trp_rhodok_crossbowman,5,10),(trp_rhodok_tribesman,11,26)]),
##  ("kingdom_5_reinforcements_b", "kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman,4,9),(trp_rhodok_spearman,5,10),(trp_rhodok_crossbowman,3,8)]),
##  ("kingdom_5_reinforcements_c", "kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant,3,7),(trp_rhodok_veteran_spearman,2,5),(trp_rhodok_veteran_crossbowman,2,5)]),



  ("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,5,20),(trp_steppe_bandit_archer,5,20),(trp_steppe_bandit_lancer,5,20),(trp_steppe_bandit_leader,1,1)]),
  ("taiga_bandit_lair","Tundra Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,58)]),
  ("desert_bandit_lair" ,"Desert Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,58)]),
  ("forest_bandit_lair" ,"Forest Bandit Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58)]),
  ("mountain_bandit_lair" ,"Mountain Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58)]),
  ("sea_raider_lair","Sea Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider_light,5,20),(trp_sea_raider,10,30),(trp_sea_raider_leader_a,1,1)]),
  ("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),
  
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),

  ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),
  
  ("player_troops_company_25", "{!}player_troops_company_25", 0, 0, fac_commoners, 0, [(trp_player_recruit,5,5),(trp_player_footman,5,5),(trp_player_trained_footman,3,3),(trp_player_skirmisher,5,5),(trp_player_archer,3,3),(trp_player_horseman,4,4)]),
  ("player_troops_company_50", "{!}player_troops_company_50", 0, 0, fac_commoners, 0, [(trp_player_recruit,10,10),(trp_player_footman,10,10),(trp_player_trained_footman,6,6),(trp_player_skirmisher,10,10),(trp_player_archer,6,6),(trp_player_horseman,8,8)]),
  ("player_troops_company_75", "{!}player_troops_company_75", 0, 0, fac_commoners, 0, [(trp_player_recruit,15,15),(trp_player_footman,15,15),(trp_player_trained_footman,9,9),(trp_player_skirmisher,15,15),(trp_player_archer,9,9),(trp_player_horseman,12,12)]),
]
