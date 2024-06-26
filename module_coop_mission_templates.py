from header_common import *
from header_operations import *
from header_mission_templates import *
from header_animations import *
from header_sounds import *
from header_music import *
from header_items import *
from module_constants import *
from module_mission_templates import *

#from module_mission_templates import *


####################################################################################################################
#   Each mission-template is a tuple that contains the following fields:
#  1) Mission-template id (string): used for referencing mission-templates in other files.
#     The prefix mt_ is automatically added before each mission-template id
#
#  2) Mission-template flags (int): See header_mission-templates.py for a list of available flags
#  3) Mission-type(int): Which mission types this mission template matches.
#     For mission-types to be used with the default party-meeting system,
#     this should be 'charge' or 'charge_with_ally' otherwise must be -1.
#     
#  4) Mission description text (string).
#  5) List of spawn records (list): Each spawn record is a tuple that contains the following fields:
#    5.1) entry-no: Troops spawned from this spawn record will use this entry
#    5.2) spawn flags.
#    5.3) alter flags. which equipment will be overriden
#    5.4) ai flags.
#    5.5) Number of troops to spawn.
#    5.6) list of equipment to add to troops spawned from here (maximum 8).
#  6) List of triggers (list).
#     See module_triggers.py for infomation about triggers.
#
#  Please note that mission templates is work in progress and can be changed in the future versions.
# 
####################################################################################################################

common_battle_order_panel = (
  0, 0, 0, [],
  [
    (game_key_clicked, gk_view_orders),
    (neg|is_presentation_active, "prsnt_battle"),
    (start_presentation, "prsnt_battle"),
    ])

common_battle_order_panel_tick = (
  0.1, 0, 0, [],
  [
    (is_presentation_active, "prsnt_battle"),
    (call_script, "script_update_order_panel_statistics_and_map"),
    ])


coop_server_check_polls = (
  1, 5, 0,
  [
    (multiplayer_is_server),
    (eq, "$g_multiplayer_poll_running", 1),
    (eq, "$g_multiplayer_poll_ended", 0),
    (store_mission_timer_a, ":mission_timer"),
    (store_add, ":total_votes", "$g_multiplayer_poll_no_count", "$g_multiplayer_poll_yes_count"),
    (this_or_next|eq, ":total_votes", "$g_multiplayer_poll_num_sent"),
    (gt, ":mission_timer", "$g_multiplayer_poll_end_time"),
    (call_script, "script_cf_multiplayer_evaluate_poll"),
    ],
  [
    (assign, "$g_multiplayer_poll_running", 0),
    ])


coop_store_respawn_as_bot = (  
      ti_on_agent_killed_or_wounded, 0, 0, [(multiplayer_is_server)],
       [
         (store_trigger_param_1, ":dead_agent_no"),
         (try_begin),#store player location for respawn as bot
           
           (agent_is_human, ":dead_agent_no"),
           (neg|agent_is_non_player, ":dead_agent_no"),

           (ge, ":dead_agent_no", 0),
           (agent_get_player_id, ":dead_agent_player_id", ":dead_agent_no"),
           (ge, ":dead_agent_player_id", 0),

           (set_fixed_point_multiplier, 100),

           (agent_get_player_id, ":dead_agent_player_id", ":dead_agent_no"),
           (agent_get_position, pos0, ":dead_agent_no"),

           (position_get_x, ":x_coor", pos0),
           (position_get_y, ":y_coor", pos0),
           (position_get_z, ":z_coor", pos0),
         
           (player_set_slot, ":dead_agent_player_id", slot_player_death_pos_x, ":x_coor"),
           (player_set_slot, ":dead_agent_player_id", slot_player_death_pos_y, ":y_coor"),
           (player_set_slot, ":dead_agent_player_id", slot_player_death_pos_z, ":z_coor"),
         (try_end), 
 
    ])



coop_respawn_as_bot = (  
      2, 0, 0, [
        (multiplayer_is_server),
        (eq, "$g_multiplayer_player_respawn_as_bot", 1),
      ],#respawn as bot
       [
       #spawning as a bot (if option ($g_multiplayer_player_respawn_as_bot) is 1)
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (neg|player_is_busy_with_menus, ":player_no"),
           (try_begin),
            (player_get_team_no, ":player_team", ":player_no"),

            (assign, ":continue", 0),
            (player_get_agent_id, ":player_agent", ":player_no"),
            (try_begin),
             (ge, ":player_agent", 0),
             (neg|agent_is_alive, ":player_agent"),
             (assign, ":continue", 1),
            (else_try),
             (lt, ":player_agent", 0),
             (player_get_slot, ":player_selected_troop", ":player_no", slot_player_coop_selected_troop),
             (le, ":player_selected_troop", 0),
             (assign, ":continue", 2),
            (try_end),
            (gt, ":continue", 0),

             # (agent_get_time_elapsed_since_removed, ":elapsed_time", ":player_agent"),
             # (gt, ":elapsed_time", "$g_multiplayer_respawn_period"),

             (assign, ":is_found", 0),
             (try_for_agents, ":cur_agent"),
               (eq, ":is_found", 0),
               (agent_is_alive, ":cur_agent"),
               (agent_is_human, ":cur_agent"),
               (agent_is_non_player, ":cur_agent"),
               (agent_get_team ,":cur_team", ":cur_agent"),
               (eq, ":cur_team", ":player_team"),
               (agent_get_position, pos0, ":cur_agent"),
               (assign, ":is_found", 1),
             (try_end),

            (try_begin), #if we have not spawned store pos of ally
             (eq, ":continue", 2),
             (set_fixed_point_multiplier, 100),
             (position_get_x, ":x_coor", pos0),
             (position_get_y, ":y_coor", pos0),
             (position_get_z, ":z_coor", pos0),
             (player_set_slot, ":player_no", slot_player_death_pos_x, ":x_coor"),
             (player_set_slot, ":player_no", slot_player_death_pos_y, ":y_coor"),
             (player_set_slot, ":player_no", slot_player_death_pos_z, ":z_coor"),
            (try_end),

             (try_begin),
               (eq, ":is_found", 1),
               (call_script, "script_find_most_suitable_bot_to_control", ":player_no"),
               (player_control_agent, ":player_no", reg0),
             (try_end),
           (try_end),
         (try_end),
         ])



# Trigger Param 1: damage inflicted agent_id
# Trigger Param 2: damage dealer agent_id
# Trigger Param 3: inflicted damage
# Register 0: damage dealer item_id
# Position Register 0: position of the blow
#                      rotation gives the direction of the blow
# Trigger result: if returned result is greater than or equal to zero, inflicted damage is set to the value specified by the module.
coop_server_reduce_damage = (
  ti_on_agent_hit, 0, 0,
    [    
      (multiplayer_is_server),
      (eq, "$coop_reduce_damage", 1),
    ],
    [
        (store_trigger_param_1, ":hit_agent"),
        (store_trigger_param_2, ":attacker_agent"),
        (store_trigger_param_3, ":damage"),
        # (assign, ":weapon", reg0),
        (gt, ":damage", 0), #dont do anything for 0 damage
        (agent_is_human, ":hit_agent"),
        (agent_is_human, ":attacker_agent"),
        (neg|agent_is_non_player, ":hit_agent"), #damage is for player agent
        (store_div, ":new_damage", ":damage", 4),
        (set_trigger_result, ":new_damage"),
    ])

# #### MOD BEGIN    
lance_breaking = (
  ti_on_agent_hit, 0, 0, [],
  [
    (store_trigger_param_1,":damage"),
	(store_trigger_param_2,":agent"),
	(assign,":weapon",reg0),
	
	(try_begin),
		(gt,":agent",0),
		(agent_is_human, ":agent"),
		(gt,":weapon",0),
		(gt,":damage",70),
		
		(this_or_next|eq,":weapon","itm_great_lance"),
		(this_or_next|eq,":weapon","itm_jousting_lance"),
		(eq,":weapon","itm_practice_lance"),
		(agent_unequip_item, ":agent", ":weapon"),
	(try_end),	
    ])
##### MOD END


#### MOD BEGIN    
lance_breaking_multiplayer = (
  ti_on_agent_hit, 0, 0, [],
  [
   # (store_trigger_param_1,":agent_rec"),
	(store_trigger_param,":agent",2),
	(store_trigger_param,":damage",3),	
	(store_trigger_param,":raw_damage",6),
	(assign,":weapon",reg0),
	
	
	(try_begin),
		(gt,":agent",0),
		(agent_is_human, ":agent"),
		(gt,":weapon",0),
		(gt,":damage",100),
		
		(this_or_next|eq,":weapon","itm_great_lance"),
		(this_or_next|eq,":weapon","itm_jousting_lance"),
		(eq,":weapon","itm_practice_lance"),
		(agent_unequip_item, ":agent", ":weapon"),
		
		(play_sound_at_position,"snd_shield_broken", pos1, sf_vol_15),		## 20.09.2018
	(try_end),	
	 (assign,reg3,":damage"),
	 (assign,reg4,":raw_damage"),
	 (try_begin),
	 (neg|agent_is_non_player, ":agent"),
		(agent_get_player_id,":player_no",":agent"),
		(multiplayer_send_string_to_player, ":player_no", multiplayer_event_show_server_message, "@You did {reg3} dmg. Raw dmg: {reg4}"),
	 (try_end),
	
    ])


#### AI_kick_enhancement - https://forums.taleworlds.com/index.php?threads/python-script-scheme-exchange.8652/page-39#post-9634677
## by KnowsCount
ai_kick_enhancement =  (
    2, 0, 0,
    [], [
    (try_begin),
    (neg|multiplayer_is_server),
        (get_player_agent_no,":player"),
	(else_try),
		(assign,":player",-1),
    (try_end),
    (try_for_agents, ":agent"),
		(neq, ":agent", ":player"),
		(agent_is_non_player, ":agent"),
        (agent_is_alive, ":agent"),
        (agent_is_human, ":agent"),
        (agent_is_active, ":agent"),
        (agent_slot_eq, ":agent", slot_agent_is_running_away, 0),
		(agent_get_horse,":horse",":agent"),	### kicker is not mounted
		(eq,":horse",-1),
        (agent_get_animation,":anim",":agent",0),
        (neg|is_between,":anim","anim_fall_face_hold","anim_strike_chest_front_stop"), ### checking if agent didnt just fall of horse and is getting up

        ##He's an eligible human.  Now see if he's in a position to kick.
        (agent_get_attack_action, ":attack_action", ":agent"), # return value: spare - 0, prepare - 1, attack - 2, hit - 3, was defended - 4, reload - 5, release - 6, cancel - 7
        (agent_get_defend_action, ":defend_action", ":agent"),
        (this_or_next|eq,":attack_action",4),
        (this_or_next|eq,":defend_action",1), # defend enemy
        ##So he'll only try to kick if he just parried an enemy attack, or his own attack just got parried.
        (agent_get_team, ":team", ":agent"),
        (assign, ":maximum_distance", 100),
        # get target
        (agent_ai_get_look_target,":suspect",":agent"),
        (gt,":suspect",0),
        (agent_is_alive, ":suspect"),
        (agent_is_human, ":suspect"),
        (agent_is_active, ":suspect"),
        (agent_get_team, ":suspect_team", ":suspect"),
        (neq, ":suspect_team", ":team"),
		(agent_get_horse,":horse_suspect",":suspect"),	### enemy is not mounted
		(eq,":horse_suspect",-1),
        (agent_get_position, pos1, ":agent"), # distance check
        (agent_get_position, pos2, ":suspect"),
        (neg|position_is_behind_position, pos2, pos1), #enemy cannot be behind player
        (get_distance_between_positions, ":distance", pos1, pos2),
        (le, ":distance", ":maximum_distance"),
        (store_random_in_range,":kickchance", 1, 10),
        (try_begin),
            (lt,":kickchance",2),
               # (display_message, "@Agent kicks."),
                (agent_set_animation, ":agent", "anim_prepare_kick_0"),
                (agent_set_animation, ":agent", "anim_kick_right_leg"),### added 13.03.2023
				(agent_set_animation, ":suspect", "anim_strike3_abdomen_front"), ### it was after agent_deliver_damage_to_agent
                (agent_deliver_damage_to_agent, ":agent", ":suspect", 3),
				#(agent_set_animation, ":suspect", "anim_strike3_abdomen_front"),
            (try_end),
       (try_end),
       ])	
       
       
       
#### trigger for changing agents modifiers according to:		
### kingdom building bonuses 
### alcohol use	- ###### mod, party drinking script
# by Rider of Rohirrim
effects_on_troops =  (
    ti_on_agent_spawn, 0, 0,
    [], [
	(store_trigger_param_1, ":agent"),
	(agent_is_human,":agent"),
	(agent_set_kick_allowed, ":agent", 1),
    
    (agent_get_slot,":agent_party",":agent",slot_agent_coop_spawn_party), #getting agent party
    (display_message,"@Party {reg1}"),
	# (try_begin),
	# (eq,":agent_party","p_main_party"),
		# (try_begin), ### if party uses alcohol - alcohol unlocked and in inventory
		# (eq,"$party_was_drinking",1),
			# (store_random_in_range,":rand",0,100),
			# (try_begin),
			# (lt,":rand",51),		## 50% chance for agent got drunk before battle 
				# ## 20 % penalty in everything ( horse speed 10% penalty)
				# (agent_set_damage_modifier, ":agent", 80),
				# (agent_set_accuracy_modifier, ":agent", 80),
				# (agent_set_speed_modifier, ":agent", 80),
				# (agent_set_reload_speed_modifier, ":agent", 80),
				# (agent_set_use_speed_modifier, ":agent", 80),
				# (agent_set_ranged_damage_modifier, ":agent", 80),
				# (agent_set_horse_speed_factor, ":agent", 90),
				# #bonus to health
				# (store_agent_hit_points,":current_hp",":agent",1),
				# #(assign,reg3,":current_hp"),#DEBUG
				# #(display_message,"@ agent hp before change: {reg3}"),
				# (store_mul,":new_hp",":current_hp",3),
				# (val_div,":new_hp",2),
				# (agent_set_max_hit_points,":agent",":new_hp",1),
				# (agent_set_hit_points,":agent",":new_hp",1),
				# #(store_agent_hit_points,reg3,":agent",1), #DEBUG
				# #(assign,reg4,":new_hp"),	
				# #(display_message,"@ agent hp after change: {reg3} new: {reg4}"),
			# (try_end),
		# (try_end),
		
        
		# ### if player has built buildings: smith, ...   (agent_set_item_slot_modifier, <agent_no>, <item_slot_no>, <item_modifier_no>),
        # #####           Check if item is between e.g. - 1h swords begin - 1h swords end - set modifiers for 1h swords ### +1,+2,+3 (Balanced=35c, tempered=36c , masterwork=37c,    - DONE
		# ### to do: variable for player, lords if they have built buildings - DONE
		# #### to do: randomly build buildings in lords centers  -  DONE
		# ### bonus for troops in castles/towns and lord's party  -  
		# ### deleting buildings  or transforming  -  
        # ### TO DO: make an if statement for lords to not let them build all buildings which gives better eq for troops - DONE
    # (try_end),
    
    
 
    # (try_begin),  ### if party is not - town/castle/village
 # #   (party_slot_eq, ":agent_party", slot_party_type, spt_kingdom_hero_party),

# #    (else_try), ### if party is town/castle/village
    # (this_or_next|party_slot_eq,":agent_party",slot_party_type, spt_town),
    # (this_or_next|party_slot_eq,":agent_party",slot_party_type, spt_village),
    # (party_slot_eq,":agent_party",slot_party_type, spt_castle),
        # (party_get_slot, ":party_leader", ":agent_party", slot_town_lord),
        # (str_store_troop_name,s2,":party_leader"),
        
        # (call_script,"script_check_troop_built_improvements",":party_leader"),
        # #### DEBUG
        # #(assign,reg2,":party_leader"),
       # # (display_message,"@party_leader {s2}"),
        # #### DEBUG END
    # (else_try),
        # (party_stack_get_troop_id, ":party_leader",":agent_party",0),
        # (str_store_troop_name,s2,":party_leader"),
        # (call_script,"script_check_troop_built_improvements",":party_leader"),
        # #### DEBUG
        # #(assign,reg0,":party_leader"),
       # # (display_message,"@party_leader {s2}"),
        # #### DEBUG END
    # (try_end),
	###DEBUG
	#(display_message,"@ reg0 {reg0}, reg1 {reg1}, reg2 {reg2}, reg3 {reg3}"),
    (try_begin),
    (gt,":agent_party",-1),
        (party_stack_get_troop_id, ":party_leader",":agent_party",0),
		### DEBUG
        #(str_store_troop_name,s2,":party_leader"),
        #(display_message,"@Troop: {s2}"),
		### DEBUG
    (try_end),
    (try_begin),
    #(is_between,":party_leader",kings_begin, lords_end),
        (call_script,"script_check_troop_built_improvements",":party_leader"),
    (try_end),
    (try_begin),
    (this_or_next|gt,reg0,0),
    (gt,reg3,0),	
        (try_for_range,":item_slot",ek_item_0,ek_head),
            (store_add,":slot",reg0,slot_item_is_blocked),
            (agent_get_item_slot, ":item_no", ":agent", ":item_slot"),
			(gt,":item_no",-1),
			(lt,":item_no","itm_items_end"),
			(item_get_type, ":item_type", ":item_no"),
            (try_begin),	### melee weapons
            (gt,reg0,0),
            (this_or_next|eq,":item_type",itp_type_one_handed_wpn),
            (this_or_next|eq,":item_type",itp_type_two_handed_wpn),
            (this_or_next|eq,":item_type",itp_type_polearm),
            (eq,":item_type",itp_type_shield),
                (item_get_slot,":modifier",":item_no", ":slot"),
                (agent_set_item_slot_modifier, ":agent", ":item_slot", ":modifier"),
				###DEBUG
				#(display_message,"@setting melee weapon modifier"),
            (try_end),            
            (store_add,":slot",reg3,slot_item_is_blocked),
            (try_begin),## ranged weapons
            (gt,reg3,0),
            (this_or_next|eq,":item_type",itp_type_bow),
            (this_or_next|eq,":item_type",itp_type_arrows),
            (this_or_next|eq,":item_type",itp_type_crossbow),
            (this_or_next|eq,":item_type",itp_type_bolts),
            (eq,":item_type",itp_type_thrown),
                (item_get_slot,":modifier",":item_no", ":slot"),
                (agent_set_item_slot_modifier, ":agent", ":item_slot", ":modifier"),
				###DEBUG
				#(display_message,"@setting ranged weapon modifier"),
            (try_end),
        (try_end),
	(try_end),
	
    (try_begin),##armors
    (gt,reg1,0),
        (try_for_range,":item_slot",ek_head,ek_horse),
            (store_add,":slot",reg1,slot_item_is_blocked),
            (agent_get_item_slot, ":item_no", ":agent", ":item_slot"),
			(gt,":item_no",-1),
			(lt,":item_no","itm_items_end"),
            (item_get_slot,":modifier",":item_no", ":slot"),
            (agent_set_item_slot_modifier, ":agent", ":item_slot", ":modifier"),
			###DEBUG
			#(display_message,"@setting armor parts modifier"),
        (try_end),
    (try_end),
	
	(try_begin),###horses
    (gt,reg2,0),
            (store_add,":slot",reg2,slot_item_is_blocked),
            (agent_get_item_slot, ":item_no", ":agent", ek_horse),
			(gt,":item_no",-1),
			(lt,":item_no","itm_items_end"),
            (item_get_slot,":modifier",":item_no", ":slot"),
            (agent_set_item_slot_modifier, ":agent", ek_horse, ":modifier"),
			###DEBUG
			##(display_message,"@setting horse modifier"),
    (try_end),
    
	
	])	       


### removing same type items from agents (so they wont have two bardiches for instance...)   
remove_duplicated_item_types =  (
	 ti_on_agent_spawn, 0, 0,
	  [],
	  [
		(store_trigger_param_1, ":agent"),
		(agent_get_troop_id,":troop_no", ":agent"),
		
		(try_begin),
		(agent_is_human, ":agent"),
		(agent_is_alive, ":agent"),
		(agent_is_non_player, ":agent"),
		(neg|troop_is_hero,":troop_no"),
			(array_create, ":agent_items", 0, 4),
			(array_set_val_all, ":agent_items", -1),
			
			### get agents items and save it to array
			(try_for_range, ":slot",0,4),
				(agent_get_item_slot, ":agent_item",":agent", ":slot"),
				(try_begin),
				(neq,":agent_item",-1),
					(array_set_val, ":agent_items", ":agent_item", ":slot"),
				(try_end),
			(try_end),
			
			# ## counting items
			# (assign,":items" ,0),
			# (assign,":last_item",-1),
			# (try_for_range, ":slot",0,4),
				# (array_get_val, ":item", ":agent_items", ":slot"),
				# (try_begin),
				# (gt,":item",-1),
					# (val_add,":items",1),
					# (assign,":last_item",":item"),
				# (try_end),
			# (try_end),
			
			
			### add 1h weapon for troops with only pikes or long spears
			## TODO:
			## add random item that is added for troop 
			## in case no second item is assigned to troop, add club
			# (try_begin),
			# (lt,":items",2),
				# (try_begin),
				# (this_or_next|eq,":last_item","itm_pike"),
				# (eq,":last_item","itm_pike_b"),
					# (agent_equip_item, ":agent", "itm_one_handed_war_axe_b", 4),
				# (try_end),
			# (else_try),
			
			### delete duplicated items
			(assign,":duplicated_1h",0),
			(assign,":duplicated_2h",0),
			(try_for_range, ":slot",0,4),
				(array_get_val, ":item", ":agent_items", ":slot"),
				(gt,":item",-1),
				(item_get_type, ":item_type", ":item"),
				(try_begin),
				(ge,":duplicated_1h",1),
				(eq,":item_type",itp_type_one_handed_wpn),
					(agent_get_item_slot, ":agent_item",":agent", ":slot"),
					(agent_unequip_item, ":agent", ":agent_item", ":slot"),
				#	(display_message,"@Droppping duplicated 1h item"),
				(else_try),
				(ge,":duplicated_2h",1),
				(eq,":item_type",itp_type_two_handed_wpn),
					(agent_get_item_slot, ":agent_item",":agent", ":slot"),
					(agent_unequip_item, ":agent", ":agent_item", ":slot"),
				#	(display_message,"@Droppping duplicated 2h item"),
				(try_end),
				
				(try_begin),
				(eq,":item_type",itp_type_one_handed_wpn),
					(val_add,":duplicated_1h",1),
				(else_try),
				(eq,":item_type",itp_type_two_handed_wpn),
					(val_add,":duplicated_2h",1),
				(try_end),
			(try_end),
			#(try_end),
			
			### check if agent has only pike or longspear
			
			
			
		#	(assign,":duplicate",0),
			
			# (try_for_range, ":slot",0,4),
				# (array_get_val, ":item_type", ":agent_weapons", ":slot"),
				
				# (try_begin),
				# (ge,":duplicate",1),
				# (neq,":item_type",-1),
					# (agent_get_item_slot, ":agent_item",":agent", ":slot"),
					# (neq,":agent_item",-1),
					# (agent_unequip_item, ":agent", ":agent_item", ":slot"),
				# #	(display_message,"@Droppping duplicated item"),
				# (try_end),
				
				# (try_begin),
				# (eq,":item_type",itp_type_two_handed_wpn),
					# (val_add,":duplicate",1),
				# (try_end),
			# (try_end),
		(try_end),
  ])     
  
#### MOD END   

	

coop_mission_templates = [

# USE FOR COOP BATTLE
    (
    "coop_battle",mtf_battle_mode,-1,
    "You lead your men to battle.",
    [     #need spawns 0-63 in multiplayer mode
      (0,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_1|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_1|mtef_no_auto_reset,af_override_horse,0,1,[]),
      (4,mtef_visitor_source|mtef_no_auto_reset,af_override_horse,0,1,[]),
      (5,mtef_visitor_source|mtef_no_auto_reset,af_override_horse,0,1,[]),
      (6,mtef_visitor_source|mtef_no_auto_reset,af_override_horse,0,1,[]),
      (7,mtef_visitor_source|mtef_no_auto_reset,af_override_horse,0,1,[]),

      (8,mtef_visitor_source|mtef_no_auto_reset,af_override_horse,0,1,[]),
      (9,mtef_visitor_source|mtef_no_auto_reset,af_override_horse,0,1,[]),
      (10,mtef_visitor_source|mtef_no_auto_reset,af_override_horse,0,1,[]),
      (11,mtef_visitor_source|mtef_no_auto_reset,af_override_horse,aif_start_alarmed,1,[]),#NEW
      (12,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (32,mtef_visitor_source|mtef_team_1|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (33,mtef_visitor_source|mtef_team_1|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (34,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (35,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (36,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (37,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (38,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (39,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (40,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (41,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (42,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (43,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (44,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (45,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (46,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (47,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (48,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (49,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (50,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (51,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (52,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (53,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (54,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (55,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (56,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (57,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (58,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (59,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (60,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (61,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (62,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (63,mtef_visitor_source,0,aif_start_alarmed,1,[]),

     ],
    [
	

	
	

      coop_server_check_polls,
      coop_server_reduce_damage,
      coop_respawn_as_bot,
      coop_store_respawn_as_bot,
	  lance_breaking_multiplayer,
	  #ai_kick_enhancement_mp,
      ai_kick_enhancement,
	  remove_duplicated_item_types,

#mordr does not work in MP = SCRIPT ERROR ON OPCODE 1785: Invalid Group ID: 1;

  #    common_battle_order_panel,
  #    common_battle_order_panel_tick,


#multiplayer_once_at_the_first_frame
      
      (ti_server_player_joined, 0, 0, [],
       [
        (store_trigger_param_1, ":player_no"),
       #  (call_script, "script_multiplayer_server_player_joined_common", ":player_no"), #dont clear slots
        (call_script, "script_multiplayer_send_initial_information", ":player_no"),
        (call_script, "script_coop_server_player_joined_common", ":player_no"),

         ]),



      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_multiplayer_game_type", multiplayer_game_type_coop_battle),
#remove
#         (call_script, "script_multiplayer_server_before_mission_start_common"), #dont set time of day, reset commanded troops
 #        (call_script, "script_multiplayer_init_mission_variables"),
##########

         (call_script, "script_coop_init_mission_variables"),
         (call_script, "script_initialize_banner_info"),


         (assign, "$g_waiting_for_confirmation_to_terminate", 0),
         (assign, "$g_round_ended", 0),
         (assign, "$coop_winner_team", -1),
         (assign, "$coop_battle_started", 0),

        # (assign, reg1, "$coop_time_of_day"), 
        # (assign, reg2, "$coop_cloud"), 
        # (assign, reg3, "$coop_haze"), 
        # (display_message, "@time {reg1} cloud {reg2} haze {reg3}"),

          #set_weather
         (scene_set_day_time, "$coop_time_of_day"),
	       (set_global_cloud_amount, "$coop_cloud"),
	       (set_global_haze_amount, "$coop_haze"),

          #removed set_fog_distance needs correct color in 1.143
         # (try_begin),
           # (gt, "$coop_cloud", 65), #if cloud cover
           # (lt,  "$coop_haze", 91), #not heavy fog
           # (set_global_haze_amount, 95), #remove sunlight
         # (try_end),

         (assign, ":rain_amount", "$coop_cloud"),
         (assign, ":rain_type", "$coop_rain"),
         (try_begin),
           (lt, ":rain_amount", 75), #less than = no rain
           (assign, ":rain_amount", 0),
           (assign, ":rain_type", 0),
         (try_end),
         (set_rain, ":rain_type" , ":rain_amount"), #1=rain 2=snow

         ]),

      (ti_after_mission_start, 0, 0, [], 
       [
         (call_script, "script_initialize_all_scene_prop_slots"),
         (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),
         (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),
         (assign, "$g_multiplayer_bot_type_1_wanted", 1),#set player wants all troops in party (host will override clients)#this should be optional

        # (assign, "$g_multiplayer_ready_for_spawning_agent", 1), #set by start battle command in presentations

          #removed set_fog_distance needs correct color in 1.143
         # (try_begin),#limit fog
           # (gt, "$coop_cloud", 65), #if cloud cover
           # (lt,  "$coop_haze", 91), #not heavy fog
           # (try_begin),
             # (eq,  "$coop_rain", 2), #if snow
             # (set_fog_distance, 200), #set fog closer
           # (else_try),
             # (set_fog_distance, 600),
           # (try_end),
         # (try_end),

        (try_begin),
          (multiplayer_is_server),
          (start_presentation, "prsnt_coop_start_battle"),
        (else_try),
          (multiplayer_get_my_player, ":my_player_no"),
          (ge, ":my_player_no", 0),
          (player_is_admin, ":my_player_no"),
          (start_presentation, "prsnt_coop_start_battle"),
        (try_end),

        (try_begin),
          (multiplayer_is_server),
          (assign, "$coop_reinforce_size", 25), ## was 10
          (assign, "$coop_reinforce", 1),
          (assign, "$coop_alive_team1", 0),#store count for reinforcement spawn
          (assign, "$coop_alive_team2", 0),


            #init spawn positions
          (entry_point_get_position, pos25, 32),
          (copy_position, pos26, pos25),
          (position_move_y, pos26, 600),
          (copy_position, pos27, pos25),
          (position_move_y, pos27, 1500),

          (entry_point_get_position, pos30, 0),
          (copy_position, pos31, pos30),
          (position_move_y, pos31, 600),
          (copy_position, pos32, pos30),
          (position_move_y, pos32, 1500),

            (try_begin),
              (eq, "$coop_battle_type", coop_battle_type_village_player_attack),
              (assign, ":ally", 1), 
              (assign, ":enemy", 2),#inside village
            (else_try),
              (eq, "$coop_battle_type", coop_battle_type_village_player_defend),
              (assign, ":ally", 2),#inside village
              (assign, ":enemy", 1),
            (else_try),
              (assign, ":ally", 0),
              (assign, ":enemy", 32),
            (try_end),

           (entry_point_get_position, pos2, ":enemy"),
           (entry_point_get_position, pos3, ":ally"),
           (position_set_z_to_ground_level, pos2),
           (position_set_z_to_ground_level, pos3),

           (set_spawn_position, pos2),
           (spawn_scene_prop, "spr_coop_inventory", 0),   

           (set_spawn_position, pos3),
           (spawn_scene_prop, "spr_coop_inventory", 0),  
           (assign, "$coop_inventory_box", reg0),

        (try_end),
		
			## MOD BEGIN Rewrite of items of troops
			(call_script,"script_coop_read_eq_from_file_to_troops"),
			## MOD END

		
        ]),


 #multiplayer_server_spawn_bots
      (0, 0, 0, [],
       [
        (try_begin),
        (multiplayer_is_server),
        (eq, "$g_multiplayer_ready_for_spawning_agent", 1),


        (assign, ":battle_size", "$coop_battle_size"),
        (try_begin), 
          (eq, "$coop_battle_type", coop_battle_type_bandit_lair),
          (assign, ":battle_size", coop_min_battle_size),
        (try_end),

        #regulate troop spawn
        (store_add, ":total_bots", "$coop_alive_team1", "$coop_alive_team2"),
        (store_sub, ":reinforce_bots", ":battle_size", "$coop_reinforce_size"),#when less troops than battle size
        (try_begin),
          (le, ":total_bots", ":reinforce_bots"), #when total alive < battle size - reinforce size
          (assign, "$coop_reinforce", 1),
        (try_end),
        (try_begin),
          (ge, ":total_bots", ":battle_size"), 
          (assign, "$coop_reinforce", 0),
        (try_end),

        (try_begin),
          (eq, "$coop_reinforce", 1), #ready for reinforcements

          #pick team by size
          (store_add, ":total_req", "$coop_num_bots_team_1", "$coop_num_bots_team_2"),
          (gt, ":total_req", 0), #reserves 

          (assign, ":alive_team1", "$coop_alive_team1"),
          (assign, ":alive_team2", "$coop_alive_team2"),
          (val_max, ":alive_team1", 1),
          (val_mul, ":alive_team2", 1000),
          (store_div, ":ratio_current", ":alive_team2", ":alive_team1"), 

          (try_begin),
            (this_or_next|eq, "$coop_num_bots_team_2", 0), #skip ratio if other team has no reinforcements
            (ge, ":ratio_current", "$coop_team_ratio"),
            (gt, "$coop_num_bots_team_1", 0),
            (assign, ":selected_team", 0),#add to team 1
          (else_try),
            (gt, "$coop_num_bots_team_2", 0),
            (assign, ":selected_team", 1),#add to team 2
          (try_end),



          #if one team is almost out of troops, choose that team
          (try_begin), #use one try so small armies don't override
            (le, "$coop_alive_team1", "$coop_reinforce_size"),
            (gt, "$coop_num_bots_team_1", 0),
            (assign, ":selected_team", 0),
          (else_try),
            (le, "$coop_alive_team2", "$coop_reinforce_size"),
            (gt, "$coop_num_bots_team_2", 0),
            (assign, ":selected_team", 1),
          (try_end),

          (call_script, "script_coop_find_bot_troop_for_spawn", ":selected_team"),
          (assign, ":selected_troop", reg0),

          (try_begin),
            (eq, ":selected_team", 0),     
            (try_begin),
              (eq, "$coop_battle_type", coop_battle_type_village_player_attack),
              (assign, reg0, 2),#peasants inside village
            (else_try),
              (eq, "$coop_battle_type", coop_battle_type_village_player_defend),
              (assign, reg0, 1),#bandits outside village
            (else_try),
              (eq, "$coop_battle_type", coop_battle_type_bandit_lair),
              (store_random_in_range, ":random_entry_point", 2, 11),
              (assign, reg0, ":random_entry_point"),#bandits 
            (else_try),
              (assign, reg0, 32),#spawn point 32
            (try_end),
          (else_try),
            (try_begin),#player team
              (eq, "$coop_battle_type", coop_battle_type_village_player_attack),
              (assign, reg0, 1), #player outside village
            (else_try),
              (eq, "$coop_battle_type", coop_battle_type_village_player_defend),
              (assign, reg0, 2),#player inside village

#NEW
            (else_try),
              (eq, "$coop_battle_type", coop_battle_type_bandit_lair),
              (assign, reg0, 11),#player inside village

            (else_try),
              (assign, reg0, 0),#spawn point 0
            (try_end),
          (try_end),

          (store_current_scene, ":cur_scene"),
          (modify_visitors_at_site, ":cur_scene"),
          (add_visitors_to_current_scene, reg0, ":selected_troop", 1, ":selected_team", -1),#don't assign group at spawn
          (assign, "$g_multiplayer_ready_for_spawning_agent", 0),

          (try_begin),
            (eq, ":selected_team", 0),
            (val_sub, "$coop_num_bots_team_1", 1),
          (else_try),
            (eq, ":selected_team", 1),
            (val_sub, "$coop_num_bots_team_2", 1),
          (try_end),
        (try_end),    

        (try_end),   


        ]),
        
        
     # effects_on_troops,
 #### mod end
 
 
 

#multiplayer_server_manage_bots
      (3, 0, 0, [], 
       [
        (multiplayer_is_server),
        (store_mission_timer_a, ":seconds_past_since_round_started"),

        #this can be used to make the bigger team charge first
        # (try_begin),#pick attacker to charge
          # (gt, "$coop_alive_team1", "$coop_alive_team2"), 
          # (assign, ":team_charge", 0),
        # (else_try),
          # (assign, ":team_charge", 1),
        # (try_end),

          # (assign, ":hold_time", "$coop_alive_team1"),
          # (val_max, ":hold_time", "$coop_alive_team2"), 
          # (val_div, ":hold_time", 5), #larger team / 5
          (store_add, ":hold_time", "$coop_alive_team1", "$coop_alive_team2"),
          (val_div, ":hold_time", 2), 
          (val_clamp, ":hold_time", 10, 41),

        (try_for_agents, ":cur_agent"),
          (agent_is_non_player, ":cur_agent"),
          (agent_is_human, ":cur_agent"),
          (agent_is_alive, ":cur_agent"),
          (call_script, "script_coop_change_leader_of_bot", ":cur_agent"),

          # (agent_get_group, ":agent_group", ":cur_agent"),
          # (agent_get_team, ":agent_team", ":cur_agent"),
          (try_begin),
            (this_or_next|eq, "$coop_battle_type", coop_battle_type_village_player_attack), #no delay for village raid
            (eq, "$coop_battle_type", coop_battle_type_village_player_defend), #village battle
            (agent_clear_scripted_mode, ":cur_agent"),
          (else_try),
            (gt, ":seconds_past_since_round_started", ":hold_time"), #everyone hold
            # (this_or_next|ge, ":agent_group", 0),#player commanded
            # (this_or_next|eq, ":agent_team", ":team_charge"), #start attacker charge
            # (gt, ":seconds_past_since_round_started", 40), #all charge
            (agent_clear_scripted_mode, ":cur_agent"),
          (try_end),
        (try_end),

          (get_max_players, ":num_players"),
          (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
            (player_is_active, ":player_no"),
            (multiplayer_send_3_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_num_reserves, 1,  "$coop_num_bots_team_1"),
            (multiplayer_send_3_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_num_reserves, 2,  "$coop_num_bots_team_2"),
          (try_end),

        ]),

		
		
      (ti_on_agent_spawn, 0, 0, [],#called by client also
       [
        (store_trigger_param_1, ":agent_no"),
        (try_begin),
          (eq, "$coop_battle_started", 0),
          (assign, "$coop_battle_started", 1),
        (try_end),
          (try_begin), #add alive team counts for server and client
            (agent_is_human, ":agent_no"),
            (agent_get_team, ":agent_team", ":agent_no"),
            (try_begin),
              (eq, ":agent_team", 0),
              (val_add, "$coop_alive_team1", 1),
            (else_try),
              (eq, ":agent_team", 1),
              (val_add, "$coop_alive_team2", 1),
            (try_end),
          (try_end),


        (try_begin),
          (multiplayer_is_server),
          (try_begin),
            (eq, "$coop_battle_spawn_formation", 1),
            (eq, "$coop_battle_type", coop_battle_type_field_battle), #not for village raids
            (call_script, "script_coop_spawn_formation", ":agent_no"), #move agent to spawn position
          (try_end),


#NEW
          (try_begin),
            (eq, "$coop_battle_type", coop_battle_type_bandit_lair),
            (agent_is_human, ":agent_no"),
            (agent_get_team, ":agent_team", ":agent_no"),
            (eq, ":agent_team", 1),
            (entry_point_get_position, pos30, 0),
            (agent_set_position, ":agent_no", pos30),
          (try_end),

          #check this script for changes, currently only sets multiplayer_ready_for_spawning_agent
          # (call_script, "script_multiplayer_server_on_agent_spawn_common", ":agent_no"),
          (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
          (agent_set_slot, ":agent_no", slot_agent_coop_spawn_party, "$coop_agent_party"), #store party of agent

          (call_script, "script_coop_equip_player_agent", ":agent_no"), #ITEM BUG WORKAROUND
        (try_end),

        (try_begin),
          (agent_is_human, ":agent_no"),
          (agent_get_troop_id,":troop_no", ":agent_no"),

      #common_battle_init_banner 
        (call_script, "script_troop_agent_set_banner", "tableau_game_troop_label_banner", ":agent_no", ":troop_no"),

        #when client's chosen troop spawns, request control of it
          (eq, ":troop_no", "$coop_my_troop_no"),

          (multiplayer_get_my_player, ":my_player_no"),
          (ge, ":my_player_no", 0),
          (player_set_team_no, ":my_player_no", "$coop_my_team"),
          (multiplayer_send_int_to_server, multiplayer_event_change_team_no, "$coop_my_team"),
          (multiplayer_send_int_to_server, multiplayer_event_change_troop_id, "$coop_my_troop_no"),
        (try_end),
        (agent_set_slot, ":agent_no", slot_agent_coop_spawn_party, "$coop_agent_party"), #store party of agent
       # (assign,reg2,"$coop_agent_party"),
       # (display_message,"@Party: {reg2}"),
        (try_begin),
        (gt,"$coop_agent_party",-1),
           # (party_stack_get_troop_id, ":party_leader","$coop_agent_party",0),
            (party_get_slot,":party_leader", "$coop_agent_party", coop_party_leader),
			### DEBUG
            # (str_store_troop_name,s2, ":party_leader"),
            # (display_message,"@Troop: {s2}"),
			### DEBUG
        (try_end),
        
        #(is_between,":party_leader",kings_begin, lords_end),
        (call_script,"script_check_troop_built_improvements",":party_leader"),
		### DEBUG
        ##(display_message,"@0:{reg0}, 1:{reg1}, 2:{reg2}, 3:{reg3}"),
        ### DEBUG
        (try_begin),
        (this_or_next|gt,reg0,0),
        (gt,reg3,0),	
            (try_for_range,":item_slot",ek_item_0,ek_head),
                (store_add,":slot",reg0,slot_item_is_blocked),
                (agent_get_item_slot, ":item_no", ":agent_no", ":item_slot"),
                (gt,":item_no",-1),
                (lt,":item_no","itm_items_end"),
                (item_get_type, ":item_type", ":item_no"),
                (try_begin),	### melee weapons
                (gt,reg0,0),
                (this_or_next|eq,":item_type",itp_type_one_handed_wpn),
                (this_or_next|eq,":item_type",itp_type_two_handed_wpn),
                (this_or_next|eq,":item_type",itp_type_polearm),
                (eq,":item_type",itp_type_shield),
                    (item_get_slot,":modifier",":item_no", ":slot"),
                    (agent_set_item_slot_modifier, ":agent_no", ":item_slot", ":modifier"),
                    ###DEBUG
                    #(display_message,"@setting melee weapon modifier"),
                (try_end),            
                (store_add,":slot",reg3,slot_item_is_blocked),
                (try_begin),## ranged weapons
                (gt,reg3,0),
                (this_or_next|eq,":item_type",itp_type_bow),
                (this_or_next|eq,":item_type",itp_type_arrows),
                (this_or_next|eq,":item_type",itp_type_crossbow),
                (this_or_next|eq,":item_type",itp_type_bolts),
                (eq,":item_type",itp_type_thrown),
                    (item_get_slot,":modifier",":item_no", ":slot"),
                    (agent_set_item_slot_modifier, ":agent_no", ":item_slot", ":modifier"),
                    ###DEBUG
                    #(display_message,"@setting ranged weapon modifier"),
                (try_end),
            (try_end),
        (try_end),
        
        (try_begin),##armors
        (gt,reg1,0),
            (try_for_range,":item_slot",ek_head,ek_horse),
                (store_add,":slot",reg1,slot_item_is_blocked),
                (agent_get_item_slot, ":item_no", ":agent_no", ":item_slot"),
                (gt,":item_no",-1),
                (lt,":item_no","itm_items_end"),
                (item_get_slot,":modifier",":item_no", ":slot"),
                (agent_set_item_slot_modifier, ":agent_no", ":item_slot", ":modifier"),
                ###DEBUG
                #(display_message,"@setting armor parts modifier"),
            (try_end),
        (try_end),
        
        (try_begin),###horses
        (gt,reg2,0),
                (store_add,":slot",reg2,slot_item_is_blocked),
                (agent_get_item_slot, ":item_no", ":agent_no", ek_horse),
                (gt,":item_no",-1),
                (lt,":item_no","itm_items_end"),
                (item_get_slot,":modifier",":item_no", ":slot"),
                (agent_set_item_slot_modifier, ":agent_no", ek_horse, ":modifier"),
                ###DEBUG
                ##(display_message,"@setting horse modifier"),
        (try_end),
    
        
        
        
        
        
		#### MOD begin		10.12.2021
		##### 	- UNEQUIPING SPAWNING AGENTS ITEMS FOR CLIENTS	( WITHOUT IT IT CREATES CONFLICTS LIKE AGENTS HAS ITEMS THAT CAN ONLY BE ACCESSED BY NUMERIC KEYBOARD 1-4 AND NOT BY THE NEXT WEAPON BTN)
		#####   - ADDING ITEMS FOR AGENTS AFTER THEY SPAWN
		#####   - SERVER UPDATES ITEMS FOR AGENTS 
		
		# (try_for_range,reg50,0,4),
			# (agent_get_item_slot,":item_som",":agent_no",reg50),
			# (gt,":item_som",-1),
			# (agent_unequip_item, ":agent_no", ":item_som", reg50),
		# (try_end),
         
		]),
        
        
      
       
       
       
	  # (ti_on_agent_spawn,0,0,[],
	  # [
		# (this_or_next|multiplayer_is_dedicated_server),
		# (multiplayer_is_server),
		# (store_trigger_param_1, ":agent_no"),

 
 # ###### spawning troops trigger # MOD BEGIN

		# (agent_get_troop_id,":troop_no", ":agent_no"),

		# (str_store_troop_name,s1,":troop_no"),
		
			# (try_begin),
			# (is_between,":troop_no",player_troops_begin, player_troops_end),
				# (call_script,"script_coop_read_eq_from_file",":troop_no"),
			# (else_try),
				# (call_script,"script_coop_read_eq_from_troop",":troop_no"),	
			# (try_end),

		
		# (try_for_range,reg50,0,4),
		
			# (agent_get_item_slot,":item_som",":agent_no",reg50),
			


			# (gt,":item_som",-1),
			# (agent_unequip_item, ":agent_no", ":item_som", reg50),
		
		# (try_end),
		# ############## TO DO : 
		
		# (try_begin),
		# (get_player_agent_no, ":player_agent"),				#this_or_next|
		# (this_or_next|neg|is_between, ":troop_no",troops_not_matching_begin, troops_not_matching_end),
		# (eq, ":agent_no", ":player_agent"),
			# # (display_message,"@lord/lady/gracz/npc"),
			# (call_script,"script_select_items_for_lords",":troop_no"),
			
			# (try_begin),
			# (neg|eq,reg45,-1),
				# (agent_equip_item, ":agent_no", reg45, 1),
			# (try_end),
			
			# (try_begin),
			# (neg|eq,reg46,-1),
				# (agent_equip_item, ":agent_no", reg46, 2),
			# (try_end),
			
			# (try_begin),
			# (neg|eq,reg47,-1),
				# (agent_equip_item, ":agent_no", reg47, 3),
			# (try_end),
			
			# (try_begin),
			# (neg|eq,reg48,-1),
				# (agent_equip_item, ":agent_no", reg48, 4),
			# (try_end),

		# (else_try),	
		# (troop_get_class, ":trp_type",":troop_no"),
		# (eq,":trp_type",1),### Ranged troops	
		# #(neq, ":agent_no", ":player_agent"),
		# #(this_or_next|neg|eq,reg40,0),
		# #(neg|eq,reg41,0),
			# (try_begin),
			# (neg|eq,reg31,0),
				# (call_script,"script_select_items_1h"),	
				# (agent_equip_item, ":agent_no", reg0, 1),	
		# #		(display_message,"@item{reg0}"),
			# (try_end),
			

			
			
			# (try_begin),		
			# (neg|eq,reg40,0),
				# (call_script,"script_select_items_bow",":troop_no"),
				# (agent_equip_item, ":agent_no", reg5, 2),	
				# (try_begin),				
				# (neg|eq,reg42,0),
					# (call_script,"script_select_items_arrows",":troop_no"),
			# #		(display_message,"@item{reg2}"),
			# #		(display_message,"@item{reg3}"),
					# (agent_equip_item, ":agent_no", reg2, 3),					
					# #(agent_equip_item, ":agent_no", reg2, 4),
				# (try_end),	
	# #			(display_message,"@item{reg5}"),
			# (try_end),				
			
			# (try_begin),		
			# (neg|eq,reg41,0),
				# (call_script,"script_select_items_xbow",":troop_no"),
				# (agent_equip_item, ":agent_no", reg10, 2),
				# (try_begin),				
				# (neg|eq,reg43,0),
					# (call_script,"script_select_items_bolts",":troop_no"),
			# #		(display_message,"@item{reg2}"),
			# #		(display_message,"@item{reg3}"),
					# (agent_equip_item, ":agent_no", reg3, 3),					
					# #(agent_equip_item, ":agent_no", reg3, 4),
				# (try_end),						
	# #			(display_message,"@item{reg5}"),
			# (try_end),		

			
			


		# (else_try),
		# #(is_between,":troop_no",player_cav_begin,player_cav_end),### Cavalry
			
			# # (assign,":licznik_1h",0),
			# # (assign,":licznik_2h",0),
			# # (assign,":licznik_polearm",0),

			# (call_script,"script_set_probability_values"),	######################################
			

			# (store_random_in_range,":los",0,1000),	
			# (assign,reg60,":los"),
			
			# (try_begin),
						# ##### TEST begin
			# (troop_has_flag, ":troop_no", tf_guarantee_ranged),
				
				# (try_begin),
				# (neg|eq,reg31,0),
					# (call_script,"script_select_items_1h"),	
					# (agent_equip_item, ":agent_no", reg0, 1),	
			# #		(display_message,"@item{reg0}"),
				# (try_end),
				
				# (try_begin),		
				# (neg|eq,reg40,0),
					# (call_script,"script_select_items_bow",":troop_no"),
					# (agent_equip_item, ":agent_no", reg5, 2),	
					# (try_begin),				
					# (neg|eq,reg42,0),
						# (call_script,"script_select_items_arrows",":troop_no"),
				# #		(display_message,"@item{reg2}"),
				# #		(display_message,"@item{reg3}"),
						# (agent_equip_item, ":agent_no", reg2, 3),					
						# #(agent_equip_item, ":agent_no", reg2, 4),
					# (try_end),	
		# #			(display_message,"@item{reg5}"),
				# (try_end),	
				
				
				# (try_begin),		
				# (neg|eq,reg41,0),
					# (call_script,"script_select_items_xbow",":troop_no"),
					# (agent_equip_item, ":agent_no", reg10, 2),
					# (try_begin),				
					# (neg|eq,reg43,0),
						# (call_script,"script_select_items_bolts",":troop_no"),
				# #		(display_message,"@item{reg2}"),
				# #		(display_message,"@item{reg3}"),
						# (agent_equip_item, ":agent_no", reg3, 3),					
						# #(agent_equip_item, ":agent_no", reg3, 4),
					# (try_end),						
		# #			(display_message,"@item{reg5}"),
				# (try_end),	
				
				# (try_begin),
				# (neg|eq,reg44,0),
					# (call_script,"script_select_items_throwings",":troop_no"),##returns reg9 - throwing weapon
					# (agent_equip_item, ":agent_no", reg9, 2),
				# (try_end),	
			
				# (try_begin),
				# (neg|eq,reg44,0),
					# (call_script,"script_select_items_throwings",":troop_no"),##returns reg9 - throwing weapon
					# (agent_equip_item, ":agent_no", reg9, 3),
				# (try_end),		
				
				# (try_begin),
				# (neg|eq,reg44,0),
					# (call_script,"script_select_items_throwings",":troop_no"),##returns reg9 - throwing weapon
					# (agent_equip_item, ":agent_no", reg9, 4),
				# (try_end),	
			
			# (else_try),
			# #### TEST end
			# (assign,":los2_1",0),
			# (assign,":los2_2",0),
			# (assign,":los2_22",0),
			# (assign,":los2_3",0),
			# (assign,":los2_4",0),
			# (assign,":los3_1",0),
			# (assign,":los4_1",0),
			# (is_between,":los",-1.0,"$los2"),
				# (call_script,"script_select_items_1h"),	##returns reg0 - 1h weapon
				# (agent_equip_item, ":agent_no", reg0, 1),
				
				# (try_begin),
				# (neg|eq,reg34,0),	
					# (store_mul,":los2_1","$los2",9.8),
					# (store_div,":los2_1",":los2_1",10.0),
				# #	(assign,reg51,":los2_1"),
				# #	(display_message,"@ los2_1 : {reg51}"),
					# (try_begin),
					# (is_between,":los",0.0,":los2_1"),				# 70% chance to get shield and 1h		
						# (call_script,"script_select_items_shield",":troop_no"), ##returns reg8 - shield
						# (agent_equip_item, ":agent_no", reg8, 4),
					# (try_end),
				# (try_end),	
				
				# (try_begin),
				# (neg|eq,reg33,0),	
					# (store_mul,":los2_2","$los2",4),
					# (store_div,":los2_2",":los2_2",10),
					# (store_mul,":los2_22","$los2",8),
					# (store_div,":los2_22",":los2_22",10),
					
			# ############### TODO: if weapon has 'cannot be used with shield' dont add it		
				# #	(assign,reg51,":los2_2"),
				# #	(assign,reg52,":los2_22"),
				# #	(display_message,"@ los2_2 : {reg51}"),
				# #	(display_message,"@ los2_22 : {reg52}"),
					# (try_begin),
					# (is_between,":los",":los2_2",":los2_22"),	# 40% chance to get polearm and 1h
						# (call_script,"script_select_items_polearm",":troop_no"),##returns reg7 - polearm weapon
						# (agent_equip_item, ":agent_no", reg7, 3),	
					# (try_end),
				# (else_try),
				# (neg|eq,reg44,0),
					# (store_div,":los2_4","$los2",10),	
					# (store_mul,":los2_3","$los2",4),							
					# (store_div,":los2_3",":los2_3",10),		
				# #	(assign,reg51,":los2_3"),
				# #	(assign,reg52,":los2_4"),
				# #	(display_message,"@ los2_3 : {reg51}, los2_4 {reg52}"),	
					# (try_begin),
					# (is_between,":los",":los2_4",":los2_3"),
						# (call_script,"script_select_items_throwings",":troop_no"),##returns reg9 - throwing weapon
						# (agent_equip_item, ":agent_no", reg9, 3),
					# (try_end),
				# (try_end),		
			# (else_try),
			# (is_between,":los","$los2","$los3"),	
				# (try_begin),
				# (neg|eq,reg32,0),
					# (call_script,"script_select_items_2h",":troop_no"),	##returns reg6	- 2h weapon
					# (agent_equip_item, ":agent_no", reg6, 1),						
					# (try_begin),
					# (neg|eq,reg44,0),
						# (store_mul,":los3_1","$los3",6),		
						# (store_div,":los3_1",":los3_1",10),		
					# #	(assign,reg51,":los3_1"),
					# #	(display_message,"@ los3_1 : {reg51}"),
						# (try_begin),
						# (is_between,":los",":los3_1","$los3"),	# 40% chances to get throwings + 2h
							# (call_script,"script_select_items_throwings",":troop_no"),##returns reg9	- throwing weapon
							# (agent_equip_item, ":agent_no", reg9, 2),
						# (try_end),									
					# (try_end),
				# (try_end),	
			# (else_try),
			# (is_between,":los","$los3","$los4"),	
				# (try_begin),
				# (neg|eq,reg33,0),
					# (call_script,"script_select_items_polearm",":troop_no"),##returns reg7	- polearm weapon
					# (agent_equip_item, ":agent_no", reg7, 1),	
					# (try_begin),
					# (neg|eq,reg44,0),
						# (store_mul,":los4_1","$los4",6),	 
						# (store_div,":los4_1",":los4_1",10),		
					# #	(assign,reg51,":los4_1"),
					# #	(display_message,"@ los4_1 : {reg51}"),
						# (try_begin),
						# (is_between,":los",":los4_1","$los4"),	
							# (call_script,"script_select_items_throwings",":troop_no"),##returns reg9	- throwing weapon
							# (agent_equip_item, ":agent_no", reg9, 2),	
						# (try_end),
					# (try_end),
				# (try_end),
			# (try_end),

		 
 #### mod begin		26.02.2020
 


	  #   ]),
	
#### MOD END

      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
         (store_trigger_param_1, ":dead_agent_no"),
         (store_trigger_param_2, ":killer_agent_no"),
#new
         (call_script, "script_coop_server_on_agent_killed_or_wounded_common", ":dead_agent_no", ":killer_agent_no"),
	       (call_script, "script_multiplayer_server_on_agent_killed_or_wounded_common", ":dead_agent_no", ":killer_agent_no"),
     

         (assign, ":number_of_alive_1", 0),
         (assign, ":number_of_alive_2", 0),
          (try_for_agents, ":cur_agent"),
            (agent_is_human, ":cur_agent"),
            (agent_is_alive, ":cur_agent"),
            (agent_get_team, ":cur_agent_team", ":cur_agent"),
            (try_begin),
              (eq, ":cur_agent_team", 0),
              (val_add, ":number_of_alive_1", 1),
            (else_try),
              (eq, ":cur_agent_team", 1),
              (val_add, ":number_of_alive_2", 1),
            (try_end),
          (try_end),
         (assign, "$coop_alive_team1", ":number_of_alive_1"),
         (assign, "$coop_alive_team2", ":number_of_alive_2"),

        (try_begin), #check round end        
          (this_or_next|eq, ":number_of_alive_1", 0),
          (eq, ":number_of_alive_2", 0),
          (try_begin), #assign my initial team value (only used to set color of multiplayer_message_type_round_result_in_battle_mode)
            (multiplayer_get_my_player, ":my_player_no"),
            (ge, ":my_player_no", 0),
            (player_get_team_no, "$coop_my_team", ":my_player_no"),
            (player_get_team_no, "$my_team_at_start_of_round", ":my_player_no"),
            (player_get_agent_id, ":my_agent_id", ":my_player_no"),
            (ge, ":my_agent_id", 0),
            (agent_get_troop_id, "$coop_my_troop_no", ":my_agent_id"),
          (try_end),     

          (try_begin),
            (eq, "$coop_alive_team1", 0),#if team 1 is dead
            (assign, "$coop_winner_team", 1),
          (else_try),
            (eq, "$coop_alive_team2", 0),#if team 2 is dead
            (assign, "$coop_winner_team", 0),
          (try_end),

          (call_script, "script_show_multiplayer_message", multiplayer_message_type_round_result_in_battle_mode, "$coop_winner_team"), #team 2 is winner 
          (store_mission_timer_a, "$g_round_finish_time"),
          (assign, "$g_round_ended", 1),
        (try_end),


         ]),

		 
	#mod begin	 
#	  (0, 0, ti_once, [
#          (store_mission_timer_a,":mission_time"),(ge,":mission_time",2),
#          ],
#       [(call_script, "script_select_battle_tactic"),
#        (call_script, "script_battle_tactic_init"),
        #(call_script, "script_battle_calculate_initial_powers"), #deciding run away method changed and that line is erased
#        ]),
      

 #     (5, 0, 0, [
  #        (store_mission_timer_a,":mission_time"),

#          (ge,":mission_time",3),
#          
#          (call_script, "script_battle_tactic_apply"),
#          ], []), #applying battle tactic

	#mod end

    # #AI Triggers
     # (0, 5, ti_once, [
          # (this_or_next|multiplayer_is_server),
          # (multiplayer_is_dedicated_server),
          # (store_mission_timer_a,":mission_time"),(ge,":mission_time",6),
         # # (eq,"$load_ai_tactics",1),
          # ],
        # [
        # # (try_for_range,":team_no",-1,10),
            # # (team_get_leader, ":ai_leader", ":team_no"),
            # # (assign,reg1,":ai_leader"),
            
            # # (display_message,"@AI leader: {reg1}"),
           
        # # (try_end),
         # (try_begin),
         # (num_active_teams_le,2),
            # (display_message,"@ Less teams than 2"),
         # (else_try),
            # (display_message,"@ More teams than 2"),
         # (try_end),
         # (call_script, "script_select_battle_tactic_mp"),
         # (call_script, "script_battle_tactic_init_mp"),
        # #(call_script, "script_battle_calculate_initial_powers"), #deciding run away method changed and that line is erased
        # ]),
 



#	 END BATTLE ##################	
      (3, 4, ti_once, [(eq, "$g_round_ended", 1)],
       [
        (try_begin),
          (multiplayer_is_server),
          (eq, "$coop_skip_menu", 1),  #do this automatically if skip menu is checked
          (eq, "$coop_battle_started", 1),

          (call_script, "script_coop_copy_parties_to_file_mp"),
          (neg|multiplayer_is_dedicated_server),
          (finish_mission),
        (try_end), 

        ]),


      (ti_tab_pressed, 0, 0, [],
       [
         (try_begin),
           (assign, "$g_multiplayer_stats_chart_opened_manually", 1),
           (start_presentation, "prsnt_coop_stats_chart"),
         (try_end),


         ]),

      (ti_escape_pressed, 0, 0, [],
       [
         (neg|is_presentation_active, "prsnt_coop_escape_menu"),
         (neg|is_presentation_active, "prsnt_coop_stats_chart"),
         (eq, "$g_waiting_for_confirmation_to_terminate", 0),
         (start_presentation, "prsnt_coop_escape_menu"),
         ]),


      ],
  ),



#################  
    (
    "coop_siege",mtf_battle_mode,-1, #siege
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,af_override_horse,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_1|mtef_no_auto_reset,af_override_horse,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,af_override_horse,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,af_override_horse,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,af_override_horse,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),

      (32,mtef_visitor_source|mtef_team_1|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (33,mtef_visitor_source|mtef_team_1|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (34,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (35,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (36,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (37,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (38,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (39,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (40,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (41,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (42,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (43,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (44,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (45,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (46,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (47,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),

      (48,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (49,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (50,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (51,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (52,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (53,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (54,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (55,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (56,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (57,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (58,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (59,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (60,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (61,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (62,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (63,mtef_visitor_source,0,aif_start_alarmed,1,[]),
     ],
    [

      coop_server_check_polls,
      coop_server_reduce_damage,
      coop_respawn_as_bot,
      coop_store_respawn_as_bot,
	  lance_breaking_multiplayer,
	  ai_kick_enhancement,
	  remove_duplicated_item_types,
#mordr does not work in MP = SCRIPT ERROR ON OPCODE 1785: Invalid Group ID: 1;
#      common_battle_order_panel,
#      common_battle_order_panel_tick,


      (ti_server_player_joined, 0, 0, [],
       [
        (store_trigger_param_1, ":player_no"),
       # (call_script, "script_multiplayer_server_player_joined_common", ":player_no"), #dont clear slots

        (call_script, "script_multiplayer_send_initial_information", ":player_no"),
        (call_script, "script_coop_server_player_joined_common", ":player_no"),    #need to call every round
       ]),

      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_multiplayer_game_type", multiplayer_game_type_coop_siege),
     #    (call_script, "script_multiplayer_server_before_mission_start_common"), #dont set time of day, reset commanded troops
     #    (call_script, "script_multiplayer_init_mission_variables"), #dont reset commanded troop type


          (call_script, "script_initialize_banner_info"),
          (call_script, "script_coop_init_mission_variables"),

         (assign, "$g_waiting_for_confirmation_to_terminate", 0),
         (assign, "$g_round_ended", 0),
         (assign, "$coop_winner_team", -1),
         (assign, "$coop_battle_started", 0),
         (assign, "$coop_use_belfry", 0),
         (assign, "$coop_attacker_is_on_wall", 0),
         (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),

          #set_weather
         (scene_set_day_time, "$coop_time_of_day"),
	       (set_global_cloud_amount, "$coop_cloud"),
	       (set_global_haze_amount, "$coop_haze"),
          #removed set_fog_distance needs correct color in 1.143
         # (try_begin),
           # (gt, "$coop_cloud", 65), #if cloud cover
           # (lt,  "$coop_haze", 91), #not heavy fog
           # (set_global_haze_amount, 95), #remove sunlight
         # (try_end),

         (assign, ":rain_amount", "$coop_cloud"),
         (assign, ":rain_type", "$coop_rain"),
         (try_begin),
           (lt, ":rain_amount", 75), #less than = no rain
           (assign, ":rain_amount", 0),
           (assign, ":rain_type", 0),
         (try_end),
         (set_rain, ":rain_type" , ":rain_amount"), #1=rain 2=snow

#common_battle_mission_start = 
         (try_begin),
           (gt, "$coop_castle_banner", 0),
           (replace_scene_props, banner_scene_props_begin, "$coop_castle_banner"),
         (else_try),
           (replace_scene_props, banner_scene_props_begin, "spr_empty"),
         (try_end),

         ]),

      (ti_after_mission_start, 0, 0, [], 
       [

        (call_script, "script_initialize_all_scene_prop_slots"),
        (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),
        (assign, "$g_multiplayer_bot_type_1_wanted", 1),#set player wants all troops in party (host will override clients)#this should be optional

       #removed set_fog_distance needs correct color in 1.143
         # (try_begin),#limit fog
           # (gt, "$coop_cloud", 65), #if cloud cover
           # (lt,  "$coop_haze", 91), #not heavy fog
           # (try_begin),
             # (eq,  "$coop_rain", 2), #if snow
             # (set_fog_distance, 200), #set fog closer
           # (else_try),
             # (set_fog_distance, 600),
           # (try_end),
         # (try_end),

        (try_begin),
          (neg|multiplayer_is_server),
          #these lines are done in only clients at start of each new round.
          (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),
          (call_script, "script_initialize_objects_clients"),
		  (call_script,"script_siege_move_archers_to_archer_positions"),
        (try_end),  

        (try_begin),
          (multiplayer_is_server),
          (start_presentation, "prsnt_coop_start_battle"),
        (else_try),
          (multiplayer_get_my_player, ":my_player_no"),
          (ge, ":my_player_no", 0),
          (player_is_admin, ":my_player_no"),
          (start_presentation, "prsnt_coop_start_battle"),
        (try_end),

        (try_begin),
          (multiplayer_is_server),
          (assign, "$coop_reinforce_size", 25), #size of reinforcement wave # was 10
          (assign, "$coop_reinforce", 1),
          (assign, "$coop_alive_team1", 0),#store count for reinforcement spawn
          (assign, "$coop_alive_team2", 0),



          (entry_point_get_position, pos26, 10),
          (entry_point_get_position, pos31, 0),

          (try_begin),
            (this_or_next|eq, "$coop_round", coop_round_battle),
            (eq, "$coop_round", coop_round_town_street),

            (assign, ":attacker", 0),
            (try_begin),
              (eq, "$coop_round", coop_round_town_street),
              (assign, ":defender", 23),
            (else_try),
              (assign, ":defender", 15),
            (try_end),
 
            (entry_point_get_position, pos2, ":attacker"),
            (entry_point_get_position, pos3, ":defender"),
            (position_set_z_to_ground_level, pos2),
            (position_set_z_to_ground_level, pos3),

            (set_spawn_position, pos2),
            (spawn_scene_prop, "spr_coop_inventory", 0),   
            (try_begin),
              (eq, "$coop_battle_type", coop_battle_type_siege_player_attack),
              (assign, "$coop_inventory_box", reg0),
            (try_end),

            (set_spawn_position, pos3),
            (spawn_scene_prop, "spr_coop_inventory", 0),
            (try_begin),
              (eq, "$coop_battle_type", coop_battle_type_siege_player_defend),
              (assign, "$coop_inventory_box", reg0),
            (try_end),
          (try_end),
        (try_end),

            #mod begin
            (call_script,"script_coop_read_eq_from_file_to_troops"),
          ]),

      #in later rounds delay so clients can join (can use start battle option to skip)
      (5, 10, ti_once,[
       (multiplayer_is_server),
        (this_or_next|eq, "$coop_round", coop_round_town_street),
        (eq, "$coop_round", coop_round_castle_hall),
        ], 
       [
        (eq, "$coop_battle_started", 0),
        (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
        ]),


#multiplayer_server_spawn_bots
      (0, 0, 0, [], 
       [
        (multiplayer_is_server),
        (eq, "$g_multiplayer_ready_for_spawning_agent", 1),


        #get battle size
        (assign, ":battle_size", "$coop_battle_size"),
        (try_begin), 
          (eq, "$coop_round", coop_round_castle_hall),
          (val_div, ":battle_size", 4),
          (val_max, ":battle_size", coop_min_battle_size),
          (assign, "$coop_reinforce_size",10),	# was 4
        (try_end),

        #regulate troop spawn
        (store_add, ":total_bots", "$coop_alive_team1", "$coop_alive_team2"),
        (store_sub, ":reinforce_bots", ":battle_size", "$coop_reinforce_size"),#when less troops than battle size
        (try_begin),
          (this_or_next|eq, "$coop_round", coop_round_castle_hall),
          (le, ":total_bots", ":reinforce_bots"), 
          (assign, "$coop_reinforce", 1), #need global var so not cleared
        (try_end),
        (try_begin),
          (ge, ":total_bots", ":battle_size"), 
          (assign, "$coop_reinforce", 0),
        (try_end),


        (try_begin),
          #pick team by size
          (store_add, ":total_req", "$coop_num_bots_team_1", "$coop_num_bots_team_2"),
          (gt, ":total_req", 0),

          (assign, ":alive_team1", "$coop_alive_team1"),
          (assign, ":alive_team2", "$coop_alive_team2"),
          (val_max, ":alive_team1", 1),
          (val_mul, ":alive_team2", 1000),
          (store_div, ":ratio_current", ":alive_team2", ":alive_team1"), 


          (try_begin),
            (this_or_next|eq, "$coop_num_bots_team_2", 0), #skip ratio if other team has no reinforcements
            (ge, ":ratio_current", "$coop_team_ratio"),
            (gt, "$coop_num_bots_team_1", 0),
            (assign, ":selected_team", 0),#add to team 1
          (else_try),
            (gt, "$coop_num_bots_team_2", 0),
            (assign, ":selected_team", 1),#add to team 2
          (try_end),


          #if one team is almost out of troops, choose that team
          (try_begin),
            (le, "$coop_alive_team1", "$coop_reinforce_size"),
            (gt, "$coop_num_bots_team_1", 0),
            (assign, ":selected_team", 0),
          (else_try),
            (le, "$coop_alive_team2", "$coop_reinforce_size"),
            (gt, "$coop_num_bots_team_2", 0),
            (assign, ":selected_team", 1),
          (try_end),

          (try_begin), #server stop reinforcing and be ready for next scene
            (this_or_next|eq, "$coop_round", coop_round_battle),
            (eq, "$coop_round", coop_round_town_street),


            (try_begin),
              (eq, "$defender_team", 0),
              (assign, ":defender_reserves", "$coop_num_bots_team_1"), 
              (assign, ":defender_original_size", "$coop_team_1_troop_num"), 
            (else_try),
              (eq, "$defender_team", 1),
              (assign, ":defender_reserves", "$coop_num_bots_team_2"),
              (assign, ":defender_original_size", "$coop_team_2_troop_num"),  
            (try_end),

            (assign, ":reserves", coop_reserves_hall), #number to reserve for hall battle
            (try_begin),
              (gt, "$coop_street_scene", 0),
              (eq, "$coop_round", coop_round_battle),
              (assign, ":reserves", coop_reserves_street), #if street battle is comming
            (try_end),
            (ge, ":defender_original_size", ":reserves"),
            (le, ":defender_reserves", ":reserves"),
            (val_add, "$coop_round", 1),

          (try_end), 

          #if defenders withdraw, finish spawning attackers
          (try_begin),
            (this_or_next|eq, "$coop_round", coop_round_stop_reinforcing_wall),
            (eq, "$coop_round", coop_round_stop_reinforcing_street),
            (try_begin),
              (eq, "$attacker_team", 0),
              (gt, "$coop_num_bots_team_1", 0),
              (assign, ":selected_team", 0),
            (else_try),
              (eq, "$attacker_team", 1),
              (gt, "$coop_num_bots_team_2", 0),
              (assign, ":selected_team", 1),
            (try_end),

            (try_begin),
              (eq, "$defender_team", 0),
              (eq, "$coop_alive_team1", 0),
              (assign, "$coop_reinforce", 0),
            (else_try),
              (eq, "$defender_team", 1),
              (eq, "$coop_alive_team2", 0),
              (assign, "$coop_reinforce", 0),
            (try_end),
            (eq, "$defender_team", ":selected_team"),
            (assign, "$coop_reinforce", 0),
          (try_end),


          (eq, "$coop_reinforce", 1), #ready for reinforcements
          (call_script, "script_coop_find_bot_troop_for_spawn", ":selected_team"),
          (assign, ":selected_troop", reg0),
#SPAWN POINTS #######################################

          (try_begin),
            (eq, ":selected_team", "$defender_team"),
            (try_begin),#defender spawn points
              (eq, "$coop_round", coop_round_town_street),
              (store_random_in_range, ":random_point", 23, 29),
              (assign, reg0, ":random_point"),
            (else_try),
              (eq, "$coop_round", coop_round_castle_hall),
              (store_random_in_range, ":random_point", 16, 32),
              (assign, reg0, ":random_point"),
            (else_try),
              (assign, reg0, 15), #defenders are moved to other points after spawning
            (try_end),
          (else_try),#attacker spawn point
            (assign, reg0, 0),
          (try_end),
#############################################
          (store_current_scene, ":cur_scene"),
          (modify_visitors_at_site, ":cur_scene"),
		  ##################			Fix for troops spawning in weird places in Multiplayer
		  (set_spawn_radius,1),
		  
		  ##################
          (add_visitors_to_current_scene, reg0, ":selected_troop", 1, ":selected_team", -1),#don't assign group at spawn
          (assign, "$g_multiplayer_ready_for_spawning_agent", 0),

          (try_begin),
            (eq, ":selected_team", 0),
            (val_sub, "$coop_num_bots_team_1", 1),
          (else_try),
            (eq, ":selected_team", 1),
            (val_sub, "$coop_num_bots_team_2", 1),
          (try_end),

        (try_end),   
        ]),
 

      (ti_on_agent_spawn, 0, 0, [],
       [
        (store_trigger_param_1, ":agent_no"),
        (try_begin),
          (eq, "$coop_battle_started", 0),
          (assign, "$coop_battle_started", 1),
        (try_end),

          (try_begin), #add alive team counts for server and client
            (agent_is_human, ":agent_no"),
            (agent_get_team, ":agent_team", ":agent_no"),
            (try_begin),
              (eq, ":agent_team", 0),
              (val_add, "$coop_alive_team1", 1),
            (else_try),
              (eq, ":agent_team", 1),
              (val_add, "$coop_alive_team2", 1),
            (try_end),
          (try_end),

        (try_begin), #move attackers closer to spawn point
          (multiplayer_is_server),
            (agent_is_human, ":agent_no"),
            (agent_get_team, ":agent_team", ":agent_no"),
            (agent_get_class, ":agent_class", ":agent_no"),
        #    (agent_get_troop_id, ":troop_no", ":agent_no"),

            (try_begin),
              (eq, ":agent_team", "$attacker_team"),
              (try_begin),
                (try_begin),
                  (eq, "$coop_round", coop_round_castle_hall),
                  (assign, ":num_row", 2), #2 per row in castle
                (else_try),
                  (eq, "$coop_round", coop_round_town_street),
                  (assign, ":num_row", 4), #4 per row in street
                (else_try),
                  (assign, ":num_row", 20), #20 per row otherwise
                (try_end),
                (val_mul, ":num_row", 50),

                (entry_point_get_position, pos30, 0),
                (get_distance_between_positions, ":dist",pos31,pos30),
                (ge, ":dist", ":num_row"),
                (entry_point_get_position, pos31, 0),
              (try_end),
              # (position_set_z_to_ground_level, pos31),
              (agent_set_position, ":agent_no", pos31),
              (position_move_x, pos31, 50),
            (else_try),
              (eq, ":agent_team", "$defender_team"),
              (eq, "$coop_round", coop_round_battle),

              (try_begin),
          #      (troop_is_guarantee_ranged, ":troop_no"),
                (eq, ":agent_class", grc_archers),
                (store_random_in_range, ":random_point", 40, 47),
                (entry_point_get_position, pos27, ":random_point"),
                 (try_begin),
                  (eq, "$coop_attacker_is_on_wall", 0), 
                  (agent_set_scripted_destination, ":agent_no", pos27, 0), 
                (try_end),
                (try_begin),
                  (eq, "$coop_battle_spawn_formation", 1),#when spawn formation is on, 
                  (position_move_x, pos27, 200),
                  (agent_set_position, ":agent_no", pos27),
                (try_end),

              (else_try),
                (eq, "$coop_attacker_is_on_wall", 0), #before attackers reach wall, move half of defenders to wall
                (entry_point_get_position, pos25, 10),
                (try_begin),
                  # (eq, "$coop_battle_spawn_formation", 1), #when spawn formation is on, 
                  (store_random_in_range, ":random", 0, 2),
                  (eq, ":random", 0),
                  (try_begin),
                    (get_distance_between_positions, ":dist",pos26,pos25),
                    (ge, ":dist", 600), #12 x 50 per row 
                    (entry_point_get_position, pos26, 10),
                  (try_end),
                  (agent_set_position, ":agent_no", pos26),
                  (position_move_x, pos26, 50),
                (try_end),

                (position_move_y, pos25, 100),
                (agent_set_scripted_destination, ":agent_no", pos25, 0),  #keep defenders in castle until attackers reach wall
              (try_end),
            (try_end),

           #check this script for changes, currently only sets g_multiplayer_ready_for_spawning_agent
          # (call_script, "script_multiplayer_server_on_agent_spawn_common", ":agent_no"),
          (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
          (agent_set_slot, ":agent_no", slot_agent_coop_spawn_party, "$coop_agent_party"), #store party of agent
          (call_script, "script_coop_equip_player_agent", ":agent_no"), #ITEM BUG WORKAROUND
        (try_end),
        (agent_set_slot, ":agent_no", slot_agent_coop_banner, "$coop_agent_banner"), #store banner of agent for clients too

        (try_begin),
          (agent_is_human, ":agent_no"),
          (agent_get_troop_id,":troop_no", ":agent_no"),

      #common_battle_init_banner 
        (call_script, "script_troop_agent_set_banner", "tableau_game_troop_label_banner", ":agent_no", ":troop_no"),

        #when client's chosen troop spawns, request control of it
          (eq, ":troop_no", "$coop_my_troop_no"),

          (multiplayer_get_my_player, ":my_player_no"),
          (ge, ":my_player_no", 0),
          # (player_get_team_no, ":my_team_no", ":my_player_no"),
          (agent_get_team, ":agent_team", ":agent_no"),
          (eq, ":agent_team","$coop_my_team"),

          #change team
          (player_set_team_no, ":my_player_no", "$coop_my_team"),
          (multiplayer_send_int_to_server, multiplayer_event_change_team_no, "$coop_my_team"),
          (multiplayer_send_int_to_server, multiplayer_event_change_troop_id, "$coop_my_troop_no"),
        (try_end),
      
	  
		#### MOD begin		10.12.2021
		##### 	- UNEQUIPING SPAWNING AGENTS ITEMS FOR CLIENTS	( WITHOUT IT IT CREATES CONFLICTS LIKE AGENTS HAS ITEMS THAT CAN ONLY BE ACCESSED BY NUMERIC KEYBOARD 1-4 AND NOT BY THE NEXT WEAPON BTN)
		#####   - ADDING ITEMS FOR AGENTS AFTER THEY SPAWN
		#####   - SERVER UPDATES ITEMS FOR AGENTS 
		
		# (try_for_range,reg50,0,4),
			# (agent_get_item_slot,":item_som",":agent_no",reg50),
			# (gt,":item_som",-1),
			# (agent_unequip_item, ":agent_no", ":item_som", reg50),
		# (try_end),
	  

         ]),


	  (ti_on_agent_spawn,0,0,[],
	  [
		(multiplayer_is_dedicated_server),
		(store_trigger_param_1, ":agent_no"),

 
 ###### spawning troops trigger # MOD BEGIN

		(agent_get_troop_id,":troop_no", ":agent_no"),

		(str_store_troop_name,s1,":troop_no"),
		
			(try_begin),
			(is_between,":troop_no",player_troops_begin, player_troops_end),
				(call_script,"script_coop_read_eq_from_file",":troop_no"),
			(else_try),
				(call_script,"script_coop_read_eq_from_troop",":troop_no"),	
			(try_end),

		
		# (try_for_range,reg50,0,4),
		
			# (agent_get_item_slot,":item_som",":agent_no",reg50),
			


			# (gt,":item_som",-1),
			# (agent_unequip_item, ":agent_no", ":item_som", reg50),
		
		# (try_end),
		############## TO DO : 
		
		# (try_begin),
		# (get_player_agent_no, ":player_agent"),				#this_or_next|
		# (this_or_next|neg|is_between, ":troop_no",troops_not_matching_begin, troops_not_matching_end),
		# (eq, ":agent_no", ":player_agent"),
			# # (display_message,"@lord/lady/gracz/npc"),
			# (call_script,"script_select_items_for_lords",":troop_no"),
			
			# (try_begin),
			# (neg|eq,reg45,-1),
				# (agent_equip_item, ":agent_no", reg45, 1),
			# (try_end),
			
			# (try_begin),
			# (neg|eq,reg46,-1),
				# (agent_equip_item, ":agent_no", reg46, 2),
			# (try_end),
			
			# (try_begin),
			# (neg|eq,reg47,-1),
				# (agent_equip_item, ":agent_no", reg47, 3),
			# (try_end),
			
			# (try_begin),
			# (neg|eq,reg48,-1),
				# (agent_equip_item, ":agent_no", reg48, 4),
			# (try_end),

		# (else_try),	
		# (troop_get_class, ":trp_type",":troop_no"),
		# (eq,":trp_type",1),### Ranged troops	
		# #(neq, ":agent_no", ":player_agent"),
		# #(this_or_next|neg|eq,reg40,0),
		# #(neg|eq,reg41,0),
			# (try_begin),
			# (neg|eq,reg31,0),
				# (call_script,"script_select_items_1h"),	
				# (agent_equip_item, ":agent_no", reg0, 1),	
		# #		(display_message,"@item{reg0}"),
			# (try_end),
			

			
			
			# (try_begin),		
			# (neg|eq,reg40,0),
				# (call_script,"script_select_items_bow",":troop_no"),
				# (agent_equip_item, ":agent_no", reg5, 2),	
				# (try_begin),				
				# (neg|eq,reg42,0),
					# (call_script,"script_select_items_arrows",":troop_no"),
			# #		(display_message,"@item{reg2}"),
			# #		(display_message,"@item{reg3}"),
					# (agent_equip_item, ":agent_no", reg2, 3),					
					# #(agent_equip_item, ":agent_no", reg2, 4),
				# (try_end),	
	# #			(display_message,"@item{reg5}"),
			# (try_end),				
			
			# (try_begin),		
			# (neg|eq,reg41,0),
				# (call_script,"script_select_items_xbow",":troop_no"),
				# (agent_equip_item, ":agent_no", reg10, 2),
				# (try_begin),				
				# (neg|eq,reg43,0),
					# (call_script,"script_select_items_bolts",":troop_no"),
			# #		(display_message,"@item{reg2}"),
			# #		(display_message,"@item{reg3}"),
					# (agent_equip_item, ":agent_no", reg3, 3),					
					# #(agent_equip_item, ":agent_no", reg3, 4),
				# (try_end),						
	# #			(display_message,"@item{reg5}"),
			# (try_end),		

			
			


		# (else_try),
		# #(is_between,":troop_no",player_cav_begin,player_cav_end),### Cavalry
			
			# # (assign,":licznik_1h",0),
			# # (assign,":licznik_2h",0),
			# # (assign,":licznik_polearm",0),

			# (call_script,"script_set_probability_values"),	######################################
			

			# (store_random_in_range,":los",0,1000),	
			# (assign,reg60,":los"),
			
			# (try_begin),
						# ##### TEST begin
			# (troop_has_flag, ":troop_no", tf_guarantee_ranged),
				
				# (try_begin),
				# (neg|eq,reg31,0),
					# (call_script,"script_select_items_1h"),	
					# (agent_equip_item, ":agent_no", reg0, 1),	
			# #		(display_message,"@item{reg0}"),
				# (try_end),
				
				# (try_begin),		
				# (neg|eq,reg40,0),
					# (call_script,"script_select_items_bow",":troop_no"),
					# (agent_equip_item, ":agent_no", reg5, 2),	
					# (try_begin),				
					# (neg|eq,reg42,0),
						# (call_script,"script_select_items_arrows",":troop_no"),
				# #		(display_message,"@item{reg2}"),
				# #		(display_message,"@item{reg3}"),
						# (agent_equip_item, ":agent_no", reg2, 3),					
						# #(agent_equip_item, ":agent_no", reg2, 4),
					# (try_end),	
		# #			(display_message,"@item{reg5}"),
				# (try_end),	
				
				
				# (try_begin),		
				# (neg|eq,reg41,0),
					# (call_script,"script_select_items_xbow",":troop_no"),
					# (agent_equip_item, ":agent_no", reg10, 2),
					# (try_begin),				
					# (neg|eq,reg43,0),
						# (call_script,"script_select_items_bolts",":troop_no"),
				# #		(display_message,"@item{reg2}"),
				# #		(display_message,"@item{reg3}"),
						# (agent_equip_item, ":agent_no", reg3, 3),					
						# #(agent_equip_item, ":agent_no", reg3, 4),
					# (try_end),						
		# #			(display_message,"@item{reg5}"),
				# (try_end),	
				
				# (try_begin),
				# (neg|eq,reg44,0),
					# (call_script,"script_select_items_throwings",":troop_no"),##returns reg9 - throwing weapon
					# (agent_equip_item, ":agent_no", reg9, 2),
				# (try_end),	
			
				# (try_begin),
				# (neg|eq,reg44,0),
					# (call_script,"script_select_items_throwings",":troop_no"),##returns reg9 - throwing weapon
					# (agent_equip_item, ":agent_no", reg9, 3),
				# (try_end),		
				
				# (try_begin),
				# (neg|eq,reg44,0),
					# (call_script,"script_select_items_throwings",":troop_no"),##returns reg9 - throwing weapon
					# (agent_equip_item, ":agent_no", reg9, 4),
				# (try_end),	
			
			# (else_try),
			# #### TEST end
			# (assign,":los2_1",0),
			# (assign,":los2_2",0),
			# (assign,":los2_22",0),
			# (assign,":los2_3",0),
			# (assign,":los2_4",0),
			# (assign,":los3_1",0),
			# (assign,":los4_1",0),
			# (is_between,":los",-1.0,"$los2"),
				# (call_script,"script_select_items_1h"),	##returns reg0 - 1h weapon
				# (agent_equip_item, ":agent_no", reg0, 1),
				
				# (try_begin),
				# (neg|eq,reg34,0),	
					# (store_mul,":los2_1","$los2",9.8),
					# (store_div,":los2_1",":los2_1",10.0),
				# #	(assign,reg51,":los2_1"),
				# #	(display_message,"@ los2_1 : {reg51}"),
					# (try_begin),
					# (is_between,":los",0.0,":los2_1"),				# 70% chance to get shield and 1h		
						# (call_script,"script_select_items_shield",":troop_no"), ##returns reg8 - shield
						# (agent_equip_item, ":agent_no", reg8, 4),
					# (try_end),
				# (try_end),	
				
				# (try_begin),
				# (neg|eq,reg33,0),	
					# (store_mul,":los2_2","$los2",4),
					# (store_div,":los2_2",":los2_2",10),
					# (store_mul,":los2_22","$los2",8),
					# (store_div,":los2_22",":los2_22",10),
					
			# ############### TODO: if weapon has 'cannot be used with shield' dont add it		
				# #	(assign,reg51,":los2_2"),
				# #	(assign,reg52,":los2_22"),
				# #	(display_message,"@ los2_2 : {reg51}"),
				# #	(display_message,"@ los2_22 : {reg52}"),
					# (try_begin),
					# (is_between,":los",":los2_2",":los2_22"),	# 40% chance to get polearm and 1h
						# (call_script,"script_select_items_polearm",":troop_no"),##returns reg7 - polearm weapon
						# (agent_equip_item, ":agent_no", reg7, 3),	
					# (try_end),
				# (else_try),
				# (neg|eq,reg44,0),
					# (store_div,":los2_4","$los2",10),	
					# (store_mul,":los2_3","$los2",4),							
					# (store_div,":los2_3",":los2_3",10),		
				# #	(assign,reg51,":los2_3"),
				# #	(assign,reg52,":los2_4"),
				# #	(display_message,"@ los2_3 : {reg51}, los2_4 {reg52}"),	
					# (try_begin),
					# (is_between,":los",":los2_4",":los2_3"),
						# (call_script,"script_select_items_throwings",":troop_no"),##returns reg9 - throwing weapon
						# (agent_equip_item, ":agent_no", reg9, 3),
					# (try_end),
				# (try_end),		
			# (else_try),
			# (is_between,":los","$los2","$los3"),	
				# (try_begin),
				# (neg|eq,reg32,0),
					# (call_script,"script_select_items_2h",":troop_no"),	##returns reg6	- 2h weapon
					# (agent_equip_item, ":agent_no", reg6, 1),						
					# (try_begin),
					# (neg|eq,reg44,0),
						# (store_mul,":los3_1","$los3",6),		
						# (store_div,":los3_1",":los3_1",10),		
					# #	(assign,reg51,":los3_1"),
					# #	(display_message,"@ los3_1 : {reg51}"),
						# (try_begin),
						# (is_between,":los",":los3_1","$los3"),	# 40% chances to get throwings + 2h
							# (call_script,"script_select_items_throwings",":troop_no"),##returns reg9	- throwing weapon
							# (agent_equip_item, ":agent_no", reg9, 2),
						# (try_end),									
					# (try_end),
				# (try_end),	
			# (else_try),
			# (is_between,":los","$los3","$los4"),	
				# (try_begin),
				# (neg|eq,reg33,0),
					# (call_script,"script_select_items_polearm",":troop_no"),##returns reg7	- polearm weapon
					# (agent_equip_item, ":agent_no", reg7, 1),	
					# (try_begin),
					# (neg|eq,reg44,0),
						# (store_mul,":los4_1","$los4",6),	 
						# (store_div,":los4_1",":los4_1",10),		
					# #	(assign,reg51,":los4_1"),
					# #	(display_message,"@ los4_1 : {reg51}"),
						# (try_begin),
						# (is_between,":los",":los4_1","$los4"),	
							# (call_script,"script_select_items_throwings",":troop_no"),##returns reg9	- throwing weapon
							# (agent_equip_item, ":agent_no", reg9, 2),	
						# (try_end),
					# (try_end),
				# (try_end),
			# (try_end),

		 
 #### mod begin		26.02.2020
 


	     ]),
	
#### MOD END
		 
		 
      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
         (store_trigger_param_1, ":dead_agent_no"),
         (store_trigger_param_2, ":killer_agent_no"),
###
         (call_script, "script_coop_server_on_agent_killed_or_wounded_common", ":dead_agent_no", ":killer_agent_no"),
	       (call_script, "script_multiplayer_server_on_agent_killed_or_wounded_common", ":dead_agent_no", ":killer_agent_no"),
     
         (assign, ":number_of_alive_1", 0),
         (assign, ":number_of_alive_2", 0),
          (try_for_agents, ":cur_agent"),
            (agent_is_human, ":cur_agent"),
            (agent_is_alive, ":cur_agent"),
            (agent_get_team, ":cur_agent_team", ":cur_agent"),
            (try_begin),
              (eq, ":cur_agent_team", 0),
              (val_add, ":number_of_alive_1", 1),
            (else_try),
              (eq, ":cur_agent_team", 1),
              (val_add, ":number_of_alive_2", 1),
            (try_end),
          (try_end),
         (assign, "$coop_alive_team1", ":number_of_alive_1"),
         (assign, "$coop_alive_team2", ":number_of_alive_2"),

        (try_begin), #check round end        
          (this_or_next|eq, ":number_of_alive_1", 0),
          (eq, ":number_of_alive_2", 0),
          (try_begin), #assign my initial team value (only used to set color of multiplayer_message_type_round_result_in_battle_mode)
            (multiplayer_get_my_player, ":my_player_no"),
            (ge, ":my_player_no", 0),
            (player_get_team_no, "$coop_my_team", ":my_player_no"),
            (player_get_team_no, "$my_team_at_start_of_round", ":my_player_no"),
            (player_get_agent_id, ":my_agent_id", ":my_player_no"),
            (ge, ":my_agent_id", 0),
            (agent_get_troop_id, "$coop_my_troop_no", ":my_agent_id"),
          (try_end),     

          (try_begin),
            (eq, "$coop_alive_team1", 0),#if team 1 is dead
            (assign, "$coop_winner_team", 1),
            (try_begin),
              (ge, "$coop_num_bots_team_1", coop_reserves_hall), #if loser has reserves, they retreated
              (display_message, "@The defenders retreat!"),
            (try_end),
          (else_try),
            (eq, "$coop_alive_team2", 0),#if team 2 is dead
            (assign, "$coop_winner_team", 0),
            (try_begin),
              (ge, "$coop_num_bots_team_2", coop_reserves_hall), #if loser has reserves, they retreated
              (display_message, "@The defenders retreat!"),
            (try_end),
          (try_end),

          (call_script, "script_show_multiplayer_message", multiplayer_message_type_round_result_in_battle_mode, "$coop_winner_team"), #team 2 is winner 
          (store_mission_timer_a, "$g_round_finish_time"),
          (assign, "$g_round_ended", 1),
        (try_end),
#END BATTLE ##################	
        ]),




#multiplayer_server_check_end_map =                 
      (1, 0, 0,   #must check this in separate trigger in case no defenders spawn in battle round
       [
        (multiplayer_is_server),
        (this_or_next|eq, "$coop_round", coop_round_stop_reinforcing_wall),
        (eq, "$coop_round", coop_round_stop_reinforcing_street),
        ],
       [
        (try_begin),
          (try_begin),
            (eq, "$attacker_team", 0),
            (this_or_next|gt, "$coop_alive_team1", 0), 
            (gt, "$coop_num_bots_team_1", 0),#if attacker is not dead continue
            (eq, "$coop_alive_team2", 0),
            (val_add, "$coop_round", 1),
          (else_try),
            (eq, "$attacker_team", 1),
            (this_or_next|gt, "$coop_alive_team2", 0),
            (gt, "$coop_num_bots_team_2", 0), #if attacker is not dead continue
            (eq, "$coop_alive_team1", 0),
            (val_add, "$coop_round", 1),
          (try_end),

          (this_or_next|eq, "$coop_round", coop_round_town_street),
          (eq, "$coop_round", coop_round_castle_hall),
          (try_begin), 
            (eq, "$coop_street_scene", 0),
            (assign, "$coop_round", coop_round_castle_hall), #if no street scene, skip to castle hall
          (try_end),

          (assign, "$g_multiplayer_ready_for_spawning_agent", 0),

          (try_for_agents, ":cur_agent"),
            (agent_is_human, ":cur_agent"),
            (agent_is_alive, ":cur_agent"),
            (agent_get_team ,":cur_team", ":cur_agent"),
            (agent_get_troop_id, ":agent_troop_id", ":cur_agent"),
            #replace troop in temp spawn party
            (agent_get_slot, ":agent_party",":cur_agent", slot_agent_coop_spawn_party),
            (party_add_members, ":agent_party", ":agent_troop_id", 1),

            (try_begin), #save health for round 2
              (troop_is_hero, ":agent_troop_id"),
              (store_agent_hit_points, ":agent_hit_points", ":cur_agent"),
              (troop_set_health, ":agent_troop_id", ":agent_hit_points"),

              #store items from agents
              (call_script, "script_coop_player_agent_save_items", ":cur_agent"),
            (try_end),

            (try_begin), #replace reserves count
              (eq, ":cur_team", 0),
              (val_add, "$coop_num_bots_team_1", 1),
            (else_try),
              (eq, ":cur_team", 1),
              (val_add, "$coop_num_bots_team_2", 1),
            (try_end),
          (try_end),

          #sort troops of spawn parties
          (store_add, ":last_party", coop_temp_party_enemy_begin, "$coop_no_enemy_parties"), 
          (try_for_range, ":party_no", coop_temp_party_enemy_begin, ":last_party"),
            (call_script, "script_coop_sort_party", ":party_no"),
          (try_end),

          (store_add, ":last_party", coop_temp_party_ally_begin, "$coop_no_ally_parties"), 
          (try_for_range, ":party_no", coop_temp_party_ally_begin, ":last_party"),
            (call_script, "script_coop_sort_party", ":party_no"),
          (try_end),

          (try_begin), 
            (eq, "$coop_round", coop_round_town_street),
            (assign, ":next_scene", "$coop_street_scene"),
          (else_try),
            (eq, "$coop_round", coop_round_castle_hall),
            (assign, ":next_scene", "$coop_castle_scene"),
          (try_end),
          (call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
          (start_multiplayer_mission, reg0, ":next_scene", 1),
        (try_end),
        ]),



#delay after battle to quit
      (3, 4, ti_once, [(eq, "$g_round_ended", 1)],
       [
        (try_begin),
          (multiplayer_is_server),
          (eq, "$coop_skip_menu", 1), #do this automatically if skip menu is checked
          (eq, "$coop_battle_started", 1),
          (store_add, ":total_team1", "$coop_alive_team1", "$coop_num_bots_team_1"), #if one team is defeated
          (store_add, ":total_team2", "$coop_alive_team2", "$coop_num_bots_team_2"),
          (this_or_next|eq, ":total_team1", 0),
          (eq, ":total_team2", 0),

          (call_script, "script_coop_copy_parties_to_file_mp"),
          (neg|multiplayer_is_dedicated_server),
          (finish_mission),
        (try_end), 
        ]),

       
      (ti_tab_pressed, 0, 0, [],
       [
         (try_begin),
           (assign, "$g_multiplayer_stats_chart_opened_manually", 1),
           (start_presentation, "prsnt_coop_stats_chart"),
         (try_end),
         ]),


      (ti_escape_pressed, 0, 0, [],
       [
         (neg|is_presentation_active, "prsnt_coop_escape_menu"),
         (neg|is_presentation_active, "prsnt_coop_stats_chart"),
         (eq, "$g_waiting_for_confirmation_to_terminate", 0),
         (start_presentation, "prsnt_coop_escape_menu"),
         ]),

#multiplayer_server_manage_bots
      (3, 0, 0, [], 
       [
        (multiplayer_is_server),
        (try_for_agents, ":cur_agent"),
          (agent_is_non_player, ":cur_agent"),
          (agent_is_human, ":cur_agent"),
          (agent_is_alive, ":cur_agent"),
          (agent_get_team, ":agent_team", ":cur_agent"),
          (call_script, "script_coop_change_leader_of_bot", ":cur_agent"),

          (try_begin),
            (eq, ":agent_team", "$attacker_team"),
            (eq, "$coop_attacker_is_on_wall", 0),
            (agent_get_position, pos2, ":cur_agent"),
            (entry_point_get_position, pos25, 10),
            (get_distance_between_positions, ":dist",pos2,pos25),
            (lt, ":dist", 500),
            (assign, "$coop_attacker_is_on_wall", 1),
            (display_message, "@The attackers have reached the wall"),
          (try_end),

          (agent_get_group, ":agent_group", ":cur_agent"),
          (try_begin),
            (this_or_next|eq, "$belfry_positioned", 3),#if belfry is positioned
            (eq, "$coop_attacker_is_on_wall", 1),
            (agent_clear_scripted_mode, ":cur_agent"),
          (else_try),
            (this_or_next|eq, "$belfry_positioned", 2),#if belfry is almost positioned
            (ge, ":agent_group", 0),#player commanded
            (eq, ":agent_team", "$attacker_team"),
            (agent_slot_eq,":cur_agent",slot_agent_target_x_pos, 0),
            (agent_clear_scripted_mode, ":cur_agent"),
          (try_end),

#common_siege_attacker_do_not_stall,
          (try_begin),
            (eq, ":agent_team", "$attacker_team"),
            (agent_ai_set_always_attack_in_melee, ":cur_agent", 1),
          (try_end),
        (try_end),

        (get_max_players, ":num_players"),
        (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
          (player_is_active, ":player_no"),
          (multiplayer_send_3_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_num_reserves, 1,  "$coop_num_bots_team_1"),
          (multiplayer_send_3_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_num_reserves, 2,  "$coop_num_bots_team_2"),
        (try_end),

        ]),



#common_siege_refill_ammo = 
      (120, 0, 0, [(multiplayer_is_server)],
      [#refill ammo of defenders every two minutes.
        (try_for_agents,":cur_agent"),
          (agent_is_alive, ":cur_agent"),
          (agent_get_team, ":agent_team", ":cur_agent"),
          (eq, ":agent_team", "$defender_team"),
          (agent_is_non_player, ":cur_agent"),
          (agent_is_human, ":cur_agent"),
          (agent_refill_ammo, ":cur_agent"),
        (try_end),
      ]),



#line up attacking archers (not working) hard to find good position
#      (3, 0, 0,[        
#        (eq, "$coop_round", coop_round_battle),
#        ], 
#        [ 
#        (entry_point_get_position, pos4, 15), #top of ladder
#        (position_move_y, pos4, 5000), 
#        (position_move_x, pos4, -2000), 
#        (call_script, "script_coop_form_line", pos4, "$attacker_team", grc_archers, 200, 100, 3, 0), #(pos, team, dist to row, dist to troop, rows)
#      ]),


#common_siege_init_ai_and_belfry,
      (0, 0, ti_once, [], 
       [
         (try_begin),
           (multiplayer_is_server),
         
           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_a"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_a", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 1),
           (try_end),
         
           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_b"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_b", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 1),
           (try_end),
          #call coop script
           (call_script, "script_coop_move_belfries_to_their_first_entry_point", "spr_belfry_a"),
           (call_script, "script_coop_move_belfries_to_their_first_entry_point", "spr_belfry_b"),
         
           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_a"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_a", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing, 0),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_next_entry_point_id, 0),
           (try_end),
         
           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_b"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_b", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing, 0),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_next_entry_point_id, 0),
           (try_end),

           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_a"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_a", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 0),
             (assign, "$coop_use_belfry", 1), #
           (try_end),

           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_b"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_b", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 0),
             (assign, "$coop_use_belfry", 1), #
           (try_end),
           (assign, "$belfry_positioned", 0),

         (try_end),
        ]),


#multiplayer_server_check_belfry_movement
      (0, 0, 0, [ ],
       [
    (multiplayer_is_server),
    (eq, "$coop_use_belfry", 1),
    (set_fixed_point_multiplier, 100),

    (try_for_range, ":belfry_kind", 0, 2),
      (try_begin),
        (eq, ":belfry_kind", 0),
        (assign, ":belfry_body_scene_prop", "spr_belfry_a"),
      (else_try),
        (assign, ":belfry_body_scene_prop", "spr_belfry_b"),
      (try_end),
    
      (scene_prop_get_num_instances, ":num_belfries", ":belfry_body_scene_prop"),

      (try_for_range, ":belfry_no", 0, ":num_belfries"),
        (scene_prop_get_instance, ":belfry_scene_prop_id", ":belfry_body_scene_prop", ":belfry_no"),
        (prop_instance_get_position, pos1, ":belfry_scene_prop_id"), #pos1 holds position of current belfry 
        (prop_instance_get_starting_position, pos11, ":belfry_scene_prop_id"),

#common_siege_assign_men_to_belfry = 
        (call_script, "script_cf_coop_siege_assign_men_to_belfry",  pos1),

#        (store_add, ":belfry_first_entry_point_id", 11, ":belfry_no"), #belfry entry points are 110..119 and 120..129 and 130..139
        (store_add, ":belfry_first_entry_point_id", 5, ":belfry_no"), #belfry entry points are 50..55 and 60..65 and 70..75
        (try_begin),
          (eq, ":belfry_kind", 1),
          (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),
          (val_add, ":belfry_first_entry_point_id", ":number_of_belfry_a"),
        (try_end),        
                
        (val_mul, ":belfry_first_entry_point_id", 10),
#        (store_add, ":belfry_last_entry_point_id", ":belfry_first_entry_point_id", 10),#number points for each belfry
        (store_add, ":belfry_last_entry_point_id", ":belfry_first_entry_point_id", 5),#number points for each belfry
    
        (try_for_range, ":entry_point_id", ":belfry_first_entry_point_id", ":belfry_last_entry_point_id"),
          (entry_point_is_auto_generated, ":entry_point_id"),
          (assign, ":belfry_last_entry_point_id", ":entry_point_id"),
        (try_end),
        
        (assign, ":belfry_last_entry_point_id_plus_one", ":belfry_last_entry_point_id"),
        (val_sub, ":belfry_last_entry_point_id", 1),
        (assign, reg0, ":belfry_last_entry_point_id"),
        (neg|entry_point_is_auto_generated, ":belfry_last_entry_point_id"),

        (try_begin),
          (get_sq_distance_between_positions, ":dist_between_belfry_and_its_destination", pos1, pos11),

          (ge, ":dist_between_belfry_and_its_destination", 4), #0.2 * 0.2 * 100 = 4 (if distance between belfry and its destination already less than 20cm no need to move it anymore)

          # coop check when belfry is close
          (try_begin),
            (lt, ":dist_between_belfry_and_its_destination", 1000),
            (assign, "$belfry_positioned", 2), 
          (try_end),

          (try_begin),
            (lt, "$belfry_positioned", 2), 
            (copy_position, pos4, pos1),
            (position_move_y, pos4, -2400),
            (position_move_x, pos4, -800),
            (call_script, "script_coop_form_line", pos4, "$attacker_team", grc_everyone, 200, 100, 3, 0), #(pos, team, dist to row, dist to troop, rows)
          (try_end),


          (assign, ":max_dist_between_entry_point_and_belfry_destination", -1), #should be lower than 0 to allow belfry to go last entry point
          (assign, ":belfry_next_entry_point_id", -1),
          (try_for_range, ":entry_point_id", ":belfry_first_entry_point_id", ":belfry_last_entry_point_id_plus_one"),
            (entry_point_get_position, pos4, ":entry_point_id"),
            (get_sq_distance_between_positions, ":dist_between_entry_point_and_belfry_destination", pos11, pos4),
            (lt, ":dist_between_entry_point_and_belfry_destination", ":dist_between_belfry_and_its_destination"),
            (gt, ":dist_between_entry_point_and_belfry_destination", ":max_dist_between_entry_point_and_belfry_destination"),
            (assign, ":max_dist_between_entry_point_and_belfry_destination", ":dist_between_entry_point_and_belfry_destination"),
            (assign, ":belfry_next_entry_point_id", ":entry_point_id"),
          (try_end),

          (try_begin),
            (ge, ":belfry_next_entry_point_id", 0),
            (entry_point_get_position, pos5, ":belfry_next_entry_point_id"), #pos5 holds belfry next entry point target during its path
          (else_try),
            (copy_position, pos5, pos11),    
          (try_end),
        
          (get_distance_between_positions, ":belfry_next_entry_point_distance", pos1, pos5),
        
          #collecting scene prop ids of belfry parts
          (try_begin),
            (eq, ":belfry_kind", 0),
            #belfry platform_a
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_platform_a", ":belfry_no"),
            #belfry platform_b
            (scene_prop_get_instance, ":belfry_platform_b_scene_prop_id", "spr_belfry_platform_b", ":belfry_no"),
          (else_try),
            #belfry platform_a
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_b_platform_a", ":belfry_no"),
          (try_end),
    
          #belfry wheel_1
          (store_mul, ":wheel_no", ":belfry_no", 3),
          (try_begin),
            (eq, ":belfry_body_scene_prop", "spr_belfry_b"),
            (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),    
            (store_mul, ":number_of_belfry_a_wheels", ":number_of_belfry_a", 3),
            (val_add, ":wheel_no", ":number_of_belfry_a_wheels"),
          (try_end),
          (scene_prop_get_instance, ":belfry_wheel_1_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
          #belfry wheel_2
          (val_add, ":wheel_no", 1),
          (scene_prop_get_instance, ":belfry_wheel_2_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
          #belfry wheel_3
          (val_add, ":wheel_no", 1),
          (scene_prop_get_instance, ":belfry_wheel_3_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),

          (init_position, pos17),
          (position_move_y, pos17, -225),
          (position_transform_position_to_parent, pos18, pos1, pos17),
          (position_move_y, pos17, -225),
          (position_transform_position_to_parent, pos19, pos1, pos17),

          (assign, ":number_of_agents_around_belfry", 0),
#
#          (get_max_players, ":num_players"),
#          (try_for_range, ":player_no", 0, ":num_players"),
#            (player_is_active, ":player_no"),
#            (player_get_agent_id, ":agent_id", ":player_no"),
#            (ge, ":agent_id", 0),
          (try_for_agents, ":agent_id"),
            (agent_is_human, ":agent_id"),
            (agent_is_alive, ":agent_id"),

            (agent_get_team, ":agent_team", ":agent_id"),
            (eq, ":agent_team", "$attacker_team"),
 
            (agent_get_position, pos2, ":agent_id"),
            (get_sq_distance_between_positions_in_meters, ":dist_between_agent_and_belfry", pos18, pos2),

#            (lt, ":dist_between_agent_and_belfry", multi_distance_sq_to_use_belfry), #must be at most 10m * 10m = 100m away from the player
            (lt, ":dist_between_agent_and_belfry", 140), #must be at most 10m * 10m = 100m away from the player
            (neg|scene_prop_has_agent_on_it, ":belfry_scene_prop_id", ":agent_id"),
            (neg|scene_prop_has_agent_on_it, ":belfry_platform_a_scene_prop_id", ":agent_id"),

            (this_or_next|eq, ":belfry_kind", 1), #there is this_or_next here because belfry_b has no platform_b
            (neg|scene_prop_has_agent_on_it, ":belfry_platform_b_scene_prop_id", ":agent_id"),
    
            (neg|scene_prop_has_agent_on_it, ":belfry_wheel_1_scene_prop_id", ":agent_id"),#can be removed to make faster
            (neg|scene_prop_has_agent_on_it, ":belfry_wheel_2_scene_prop_id", ":agent_id"),#can be removed to make faster
            (neg|scene_prop_has_agent_on_it, ":belfry_wheel_3_scene_prop_id", ":agent_id"),#can be removed to make faster
            (neg|position_is_behind_position, pos2, pos19),
            (position_is_behind_position, pos2, pos1),
            (val_add, ":number_of_agents_around_belfry", 1),        
          (try_end),

          (val_min, ":number_of_agents_around_belfry", 16),

          (try_begin),
            (scene_prop_get_slot, ":pre_number_of_agents_around_belfry", ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing),
            (scene_prop_get_slot, ":next_entry_point_id", ":belfry_scene_prop_id", scene_prop_next_entry_point_id),
            (this_or_next|neq, ":pre_number_of_agents_around_belfry", ":number_of_agents_around_belfry"),
            (neq, ":next_entry_point_id", ":belfry_next_entry_point_id"),

            (try_begin),
              (eq, ":next_entry_point_id", ":belfry_next_entry_point_id"), #if we are still targetting same entry point subtract 
              (prop_instance_is_animating, ":is_animating", ":belfry_scene_prop_id"),
              (eq, ":is_animating", 1),

              (store_mul, ":sqrt_number_of_agents_around_belfry", "$g_last_number_of_agents_around_belfry", 100),
              (store_sqrt, ":sqrt_number_of_agents_around_belfry", ":sqrt_number_of_agents_around_belfry"),
              (val_min, ":sqrt_number_of_agents_around_belfry", 300),
              (assign, ":distance", ":belfry_next_entry_point_distance"),
              (val_mul, ":distance", ":sqrt_number_of_agents_around_belfry"),
              (val_div, ":distance", 100), #100 is because of fixed_point_multiplier
              (val_mul, ":distance", 8), #multiplying with 4 to make belfry pushing process slower, 
                                                                 #with 16 agents belfry will go with 4 / 4 = 1 speed (max), with 1 agent belfry will go with 1 / 4 = 0.25 speed (min)    
            (try_end),

            (try_begin),
              (ge, ":belfry_next_entry_point_id", 0),

              #up down rotation of belfry's next entry point
              (init_position, pos9),
              (position_set_y, pos9, -500), #go 5.0 meters back
              (position_set_x, pos9, -300), #go 3.0 meters left
              (position_transform_position_to_parent, pos10, pos5, pos9), 
              (position_get_distance_to_terrain, ":height_to_terrain_1", pos10), #learn distance between 5 meters back of entry point(pos10) and ground level at left part of belfry
      
              (init_position, pos9),
              (position_set_y, pos9, -500), #go 5.0 meters back
              (position_set_x, pos9, 300), #go 3.0 meters right
              (position_transform_position_to_parent, pos10, pos5, pos9), 
              (position_get_distance_to_terrain, ":height_to_terrain_2", pos10), #learn distance between 5 meters back of entry point(pos10) and ground level at right part of belfry

              (store_add, ":height_to_terrain", ":height_to_terrain_1", ":height_to_terrain_2"),
              (val_mul, ":height_to_terrain", 100), #because of fixed point multiplier

              (store_div, ":rotate_angle_of_next_entry_point", ":height_to_terrain", 24), #if there is 1 meters of distance (100cm) then next target position will rotate by 2 degrees. #ac sonra
              (init_position, pos20),    
              (position_rotate_x_floating, pos20, ":rotate_angle_of_next_entry_point"),
              (position_transform_position_to_parent, pos23, pos5, pos20),

              #right left rotation of belfry's next entry point
              (init_position, pos9),
              (position_set_x, pos9, -300), #go 3.0 meters left
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in -x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_left", pos10), #learn distance between 3.0 meters left of entry point(pos10) and ground level
              (init_position, pos9),
              (position_set_x, pos9, 300), #go 3.0 meters left
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_right", pos10), #learn distance between 3.0 meters right of entry point(pos10) and ground level
              (store_sub, ":height_to_terrain_1", ":height_to_terrain_at_left", ":height_to_terrain_at_right"),

              (init_position, pos9),
              (position_set_x, pos9, -300), #go 3.0 meters left
              (position_set_y, pos9, -500), #go 5.0 meters forward
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in -x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_left", pos10), #learn distance between 3.0 meters left of entry point(pos10) and ground level
              (init_position, pos9),
              (position_set_x, pos9, 300), #go 3.0 meters left
              (position_set_y, pos9, -500), #go 5.0 meters forward
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_right", pos10), #learn distance between 3.0 meters right of entry point(pos10) and ground level
              (store_sub, ":height_to_terrain_2", ":height_to_terrain_at_left", ":height_to_terrain_at_right"),

              (store_add, ":height_to_terrain", ":height_to_terrain_1", ":height_to_terrain_2"),    
              (val_mul, ":height_to_terrain", 100), #100 is because of fixed_point_multiplier
              (store_div, ":rotate_angle_of_next_entry_point", ":height_to_terrain", 24), #if there is 1 meters of distance (100cm) then next target position will rotate by 25 degrees. 
              (val_mul, ":rotate_angle_of_next_entry_point", -1),

              (init_position, pos20),
              (position_rotate_y_floating, pos20, ":rotate_angle_of_next_entry_point"),
              (position_transform_position_to_parent, pos22, pos23, pos20),
            (else_try),
              (copy_position, pos22, pos5),      
            (try_end),
              
            (try_begin),
              (ge, ":number_of_agents_around_belfry", 1), #if there is any agents pushing belfry

              (store_mul, ":sqrt_number_of_agents_around_belfry", ":number_of_agents_around_belfry", 100),
              (store_sqrt, ":sqrt_number_of_agents_around_belfry", ":sqrt_number_of_agents_around_belfry"),
              (val_min, ":sqrt_number_of_agents_around_belfry", 300),
              (val_mul, ":belfry_next_entry_point_distance", 100), #100 is because of fixed_point_multiplier
              (val_mul, ":belfry_next_entry_point_distance", 8), #multiplying with 3 to make belfry pushing process slower, 
                                                                 #with 9 agents belfry will go with 3 / 3 = 1 speed (max), with 1 agent belfry will go with 1 / 3 = 0.33 speed (min)    
              (val_div, ":belfry_next_entry_point_distance", ":sqrt_number_of_agents_around_belfry"),
              #calculating destination coordinates of belfry parts
              #belfry platform_a
              (prop_instance_get_position, pos6, ":belfry_platform_a_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos1, pos6),
              (position_transform_position_to_parent, pos8, pos22, pos7),
              (prop_instance_animate_to_position, ":belfry_platform_a_scene_prop_id", pos8, ":belfry_next_entry_point_distance"),    
              #belfry platform_b
              (try_begin),
                (eq, ":belfry_kind", 0),
                (prop_instance_get_position, pos6, ":belfry_platform_b_scene_prop_id"),
                (position_transform_position_to_local, pos7, pos1, pos6),
                (position_transform_position_to_parent, pos8, pos22, pos7),
                (prop_instance_animate_to_position, ":belfry_platform_b_scene_prop_id", pos8, ":belfry_next_entry_point_distance"),
              (try_end),
              #wheel rotation
              (store_mul, ":belfry_wheel_rotation", ":belfry_next_entry_point_distance", 25), #-25 fixed bug rotation was reversed
              #(val_add, "$g_belfry_wheel_rotation", ":belfry_wheel_rotation"),
              (assign, "$g_last_number_of_agents_around_belfry", ":number_of_agents_around_belfry"),

              #belfry wheel_1
              #(prop_instance_get_starting_position, pos13, ":belfry_wheel_1_scene_prop_id"),
              (prop_instance_get_position, pos13, ":belfry_wheel_1_scene_prop_id"),
              (prop_instance_get_position, pos20, ":belfry_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos20, pos13),
              (position_transform_position_to_parent, pos21, pos22, pos7),
              (prop_instance_rotate_to_position, ":belfry_wheel_1_scene_prop_id", pos21, ":belfry_next_entry_point_distance", ":belfry_wheel_rotation"),
      
              #belfry wheel_2
              #(prop_instance_get_starting_position, pos13, ":belfry_wheel_2_scene_prop_id"),
              (prop_instance_get_position, pos13, ":belfry_wheel_2_scene_prop_id"),
              (prop_instance_get_position, pos20, ":belfry_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos20, pos13),
              (position_transform_position_to_parent, pos21, pos22, pos7),
              (prop_instance_rotate_to_position, ":belfry_wheel_2_scene_prop_id", pos21, ":belfry_next_entry_point_distance", ":belfry_wheel_rotation"),
      
              #belfry wheel_3
              (prop_instance_get_position, pos13, ":belfry_wheel_3_scene_prop_id"),
              (prop_instance_get_position, pos20, ":belfry_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos20, pos13),
              (position_transform_position_to_parent, pos21, pos22, pos7),
              (prop_instance_rotate_to_position, ":belfry_wheel_3_scene_prop_id", pos21, ":belfry_next_entry_point_distance", ":belfry_wheel_rotation"),

              #belfry main body
              (prop_instance_animate_to_position, ":belfry_scene_prop_id", pos22, ":belfry_next_entry_point_distance"),    
            (else_try),
              (prop_instance_is_animating, ":is_animating", ":belfry_scene_prop_id"),
              (eq, ":is_animating", 1),

              #belfry platform_a
              (prop_instance_stop_animating, ":belfry_platform_a_scene_prop_id"),
              #belfry platform_b
              (try_begin),
                (eq, ":belfry_kind", 0),
                (prop_instance_stop_animating, ":belfry_platform_b_scene_prop_id"),
              (try_end),
              #belfry wheel_1
              (prop_instance_stop_animating, ":belfry_wheel_1_scene_prop_id"),
              #belfry wheel_2
              (prop_instance_stop_animating, ":belfry_wheel_2_scene_prop_id"),
              #belfry wheel_3
              (prop_instance_stop_animating, ":belfry_wheel_3_scene_prop_id"),
              #belfry main body
              (prop_instance_stop_animating, ":belfry_scene_prop_id"),
            (try_end),
        
            (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing, ":number_of_agents_around_belfry"),    
            (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_next_entry_point_id, ":belfry_next_entry_point_id"),
          (try_end),
        (else_try),
          (le, ":dist_between_belfry_and_its_destination", 4),
          (scene_prop_slot_eq, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 0),
      
          (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 1),    

          (try_begin),
            (eq, ":belfry_kind", 0),
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_platform_a", ":belfry_no"),
          (else_try),
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_b_platform_a", ":belfry_no"),
          (try_end),
          (assign, "$belfry_positioned", 3),   #
          (prop_instance_get_starting_position, pos0, ":belfry_platform_a_scene_prop_id"),
          (prop_instance_animate_to_position, ":belfry_platform_a_scene_prop_id", pos0, 1000),  #400

        (try_end),
      (try_end),
    (try_end),
    ]),

    ],
  ),

]