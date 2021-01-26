import pyoscx   

### create catalogs
catalog = pyoscx.Catalog()


### create road
road = pyoscx.RoadNetwork(roadfile='Town01',scenegraph=" ")


### create parameters
paramdec = pyoscx.ParameterDeclarations()

paramdec.add_parameter(pyoscx.Parameter('leadingSpeed',pyoscx.ParameterType.double,'2.0'))

###create properties

prop= pyoscx.Properties()
#prop.add_property


### create vehicles

bb = pyoscx.BoundingBox(2,5,1.8,2.0,0,0.9)
fa = pyoscx.Axle(0.5,0.8,1.8,3.1,0.4)
ba = pyoscx.Axle(0.5,0.8,1.8,0,0.4)
ego_veh = pyoscx.Vehicle('vehicle.volkswagen.t2',pyoscx.VehicleCategory.car,bb,fa,ba,69,100,10)
ego_veh.add_property(name='type',value='ego_vehicle')
ego_veh.add_property(name='color',value='255,0,0')
bb = pyoscx.BoundingBox(1.8,4.5,1.5,1.3,0,0.8)
fa = pyoscx.Axle(0.5,0.8,1.8,3.1,0.4)
ba = pyoscx.Axle(0.5,0.8,1.8,0,0.4)
other_veh = pyoscx.Vehicle('vehicle.tesla.model3',pyoscx.VehicleCategory.car,bb,fa,ba,69,100,10)
other_veh.add_property(name='type',value='simulation')
other_veh.add_property(name='color',value='0,0,255')

## create entities

egoname = 'hero'
targetname = 'adversary'

entities = pyoscx.Entities()

entities.add_scenario_object(egoname,ego_veh)

entities.add_scenario_object(targetname,other_veh)


### create init
init = pyoscx.Init()

#environment
timeofday=pyoscx.TimeOfDay(True,2020,12,11,21,52,10)
roadcond=pyoscx.RoadCondition(1.0)
weather=pyoscx.Weather(pyoscx.CloudState.free,1,0,1,pyoscx.PrecipitationType.dry,0,100000)
env=pyoscx.Environment("Environment1", timeofday,weather,roadcond)
envAct= pyoscx.EnvironmentAction("Environment1", env)

#controller
prop= pyoscx.Properties()
prop.add_property(name='module',value='external_control')
contr = pyoscx.Controller('HeroAgent',prop)
controllerAct = pyoscx.AssignControllerAction(contr)

#step_time = pyoscx.TransitionDynamics(pyoscx.DynamicsShapes.step,pyoscx.DynamicsDimension.time,1)

#targetspeed = pyoscx.AbsoluteSpeedAction(15,step_time)
targetstart = pyoscx.TeleportAction(pyoscx.WorldPosition(-9.4,-71,0.5,1.57079632679))
#targetstart = pyoscx.TeleportAction(pyoscx.WorldPosition(190,133,0.5,0))

#egostart = pyoscx.TeleportAction(pyoscx.WorldPosition(-9.4,-152.8,0.5,1.57079632679))
egostart = pyoscx.TeleportAction(pyoscx.LanePosition(48.58,1.0,-1,4))
#egospeed = pyoscx.AbsoluteSpeedAction(25,pyoscx.TransitionDynamics(pyoscx.DynamicsShapes.sinusoidal,pyoscx.DynamicsDimension.time,8))


init.add_global_action(envAct)
#init.add_init_action(egoname,egospeed)
init.add_init_action(egoname,egostart)
init.add_init_action(egoname,controllerAct)
#init.add_init_action(targetname,targetspeed)
init.add_init_action(targetname,targetstart)


### create an event

#event1
trigcond1 = pyoscx.RelativeDistanceCondition(40,pyoscx.Rule.lessThan, pyoscx.RelativeDistanceType.cartesianDistance,targetname,freespace=False)
trigger1 = pyoscx.EntityTrigger('StartConditionLeadingVehicleKeepsVelocity',0,pyoscx.ConditionEdge.rising,trigcond1,egoname)

event1 = pyoscx.Event('LeadingVehicleKeepsVelocity',pyoscx.Priority.overwrite)
event1.add_trigger(trigger1)

step = pyoscx.TransitionDynamics(pyoscx.DynamicsShapes.step,pyoscx.DynamicsDimension.distance,20)
action1 = pyoscx.AbsoluteSpeedAction('$leadingSpeed',step)
event1.add_action('LeadingVehicleKeepsVelocity',action1)

#event2  
trigcond2 = pyoscx.StoryboardElementStateCondition(pyoscx.StoryboardElementType.action, event1.name , pyoscx.StoryboardElementState.endTransition)
trigger2 = pyoscx.ValueTrigger('AfterLeadingVehicleKeepsVelocity',0,pyoscx.ConditionEdge.rising,trigcond2)

event2 = pyoscx.Event('LeadingVehicleWaits',pyoscx.Priority.overwrite)
event2.add_trigger(trigger2)

step = pyoscx.TransitionDynamics(pyoscx.DynamicsShapes.step,pyoscx.DynamicsDimension.time,10)
action2 = pyoscx.AbsoluteSpeedAction(0.0,step)
event2.add_action('LeadingVehicleWaits',action2)

## create the maneuver 
man = pyoscx.Maneuver('FollowLeadingVehicleManeuver')
man.add_event(event1)
man.add_event(event2)

mangr = pyoscx.ManeuverGroup('mangroup')
mangr.add_actor('adversary')
mangr.add_maneuver(man)

#starttrigger
starttrigcond = pyoscx.TraveledDistanceCondition(1.0)
starttrigger = pyoscx.EntityTrigger('OverallStartCondition',0,pyoscx.ConditionEdge.rising,starttrigcond,egoname)
starttrigcond2 = pyoscx.SimulationTimeCondition(0,pyoscx.Rule.equalTo)
starttrigger2 = pyoscx.ValueTrigger('StartTime',0,pyoscx.ConditionEdge.rising,starttrigcond2)

startcondgroup = pyoscx.ConditionGroup()
startcondgroup.add_condition(starttrigger)
startcondgroup.add_condition(starttrigger2)

#stoptrigger
stoptrigcond = pyoscx.TraveledDistanceCondition(200.0)
stoptrigger = pyoscx.EntityTrigger('EndCondition',0,pyoscx.ConditionEdge.rising,stoptrigcond,egoname, triggeringpoint='stop')

act = pyoscx.Act('Behavior',startcondgroup, stoptrigger)
act.add_maneuver_group(mangr)


## create the story
#storyparam = pyoscx.ParameterDeclarations()
#storyparam.add_parameter(pyoscx.Parameter('$owner',pyoscx.ParameterType.string,targetname))
story = pyoscx.Story('Mystory')
story.add_act(act)


## create the storyboard
stoptriggroup = pyoscx.ConditionGroup(triggeringpoint='stop')

stoptrigcond1 = pyoscx.ParameterCondition('', 0, pyoscx.Rule.lessThan)
stoptrigger1 = pyoscx.ValueTrigger('criteria_RunningStopTest',0,pyoscx.ConditionEdge.rising,stoptrigcond1)

stoptrigcond2 = pyoscx.ParameterCondition('', 0, pyoscx.Rule.lessThan)
stoptrigger2 = pyoscx.ValueTrigger('criteria_RunningRedLightTest',0,pyoscx.ConditionEdge.rising,stoptrigcond2)

stoptrigcond3 = pyoscx.ParameterCondition('', 0, pyoscx.Rule.lessThan)
stoptrigger3 = pyoscx.ValueTrigger('criteria_WrongLaneTes',0,pyoscx.ConditionEdge.rising,stoptrigcond3)

stoptrigcond4 = pyoscx.ParameterCondition('', 0, pyoscx.Rule.lessThan)
stoptrigger4 = pyoscx.ValueTrigger('criteria_OnSidewalkTest',0,pyoscx.ConditionEdge.rising,stoptrigcond4)

stoptrigcond5 = pyoscx.ParameterCondition('', 0, pyoscx.Rule.lessThan)
stoptrigger5 = pyoscx.ValueTrigger('criteria_KeepLaneTest',0,pyoscx.ConditionEdge.rising,stoptrigcond5)

stoptrigcond6 = pyoscx.ParameterCondition('', 0, pyoscx.Rule.lessThan)
stoptrigger6 = pyoscx.ValueTrigger('criteria_CollisionTest',0,pyoscx.ConditionEdge.rising,stoptrigcond6)

stoptrigcond7 = pyoscx.ParameterCondition('distance_success', 0, pyoscx.Rule.lessThan)
stoptrigger7 = pyoscx.ValueTrigger('criteria_DrivenDistanceTest',100,pyoscx.ConditionEdge.rising,stoptrigcond7)

stoptriggroup.add_condition(stoptrigger1)
stoptriggroup.add_condition(stoptrigger2)
stoptriggroup.add_condition(stoptrigger3)
stoptriggroup.add_condition(stoptrigger4)
stoptriggroup.add_condition(stoptrigger5)
stoptriggroup.add_condition(stoptrigger6)
stoptriggroup.add_condition(stoptrigger7)

sb = pyoscx.StoryBoard(init, stoptriggroup)
sb.add_story(story)

## create the scenario
sce = pyoscx.Scenario('CARLA:FollowLeadingVehicle','MottaBonora',paramdec,entities=entities,storyboard = sb,roadnetwork=road,catalog=catalog)

# display the scenario
pyoscx.prettyprint(sce.get_element())

# if you want to save it
sce.write_xml('Follow.xosc',True)


