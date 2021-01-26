import pytest


import pyoscx as OSC


TD = OSC.TransitionDynamics(OSC.DynamicsShapes.step,OSC.DynamicsDimension.rate,1)


def test_speedaction_abs():
    speedaction = OSC.AbsoluteSpeedAction(50,TD)
    OSC.prettyprint(speedaction.get_element())

def test_speedaction_rel():
    speedaction = OSC.RelativeSpeedAction(1,'Ego',TD)

    OSC.prettyprint(speedaction.get_element())

def test_longdistaction_dist():
    longdist = OSC.LongitudinalDistanceAction(1,'Ego')
    OSC.prettyprint(longdist.get_element())

def test_longdistaction_time():
    longdist = OSC.LongitudinalTimegapAction(2,'Ego',max_acceleration=1)
    OSC.prettyprint(longdist.get_element())

def test_lanechange_abs():
    lanechange = OSC.AbsoluteLaneChangeAction(1,TD)
    OSC.prettyprint(lanechange.get_element())

def test_lanechange_rel():
    lanechange = OSC.RelativeLaneChangeAction(1,'Ego',TD,0.2)
    OSC.prettyprint(lanechange.get_element())

def test_laneoffset_abs():
    laneoffset = OSC.AbsoluteLaneOffsetAction(1,OSC.DynamicsShapes.step,3,False)
    OSC.prettyprint(laneoffset.get_element())

def test_laneoffset_rel():
    laneoffset = OSC.RelativeLaneOffsetAction(1,'Ego',OSC.DynamicsShapes.step,3,False)
    OSC.prettyprint(laneoffset.get_element())

def test_lateraldistance_noconst():
    latdist = OSC.LateralDistanceAction('Ego')
    OSC.prettyprint(latdist.get_element())

def test_lateraldistance_const():
    latdist = OSC.LateralDistanceAction('Ego',3,max_speed=50)
    OSC.prettyprint(latdist.get_element())

def test_teleport():
    teleport = OSC.TeleportAction(OSC.WorldPosition())
    OSC.prettyprint(teleport.get_element())

def test_assign_route():
    route = OSC.Route('myroute')
    route.add_waypoint(OSC.WorldPosition(0,0,0,0,0,0),OSC.RouteStrategy.shortest)
    route.add_waypoint(OSC.WorldPosition(1,1,0,0,0,0),OSC.RouteStrategy.shortest)
    OSC.AssignRouteAction(route)

def test_aqcuire_position_route():
    ara = OSC.AcquirePositionAction(OSC.WorldPosition(1,1,0,0,0,0))
    OSC.prettyprint(ara.get_element())

def test_activate_controller_action():
    aca = OSC.ActivateControllerAction(True,True)
    OSC.prettyprint(aca.get_element())


def test_assign_controller_action():
    prop = OSC.Properties()
    prop.add_property('mything','2')
    prop.add_property('theotherthing','true')

    cnt = OSC.Controller('mycontroller',prop)
    
    
    aca = OSC.AssignControllerAction(cnt)
    OSC.prettyprint(aca.get_element())

def test_overide_brake():
    oa = OSC.OverrideBrakeAction(0.4,True)
    OSC.prettyprint(oa.get_element())

def test_overide_clutch():
    oa = OSC.OverrideClutchAction(0.4,True)
    OSC.prettyprint(oa.get_element())

def test_overide_parking():
    oa = OSC.OverrideParkingBrakeAction(0.4,True)
    OSC.prettyprint(oa.get_element())

def test_overide_gear():
    oa = OSC.OverrideGearAction(0.4,True)
    OSC.prettyprint(oa.get_element())

def test_overide_steering():
    oa = OSC.OverrideSteeringWheelAction(0.4,True)
    OSC.prettyprint(oa.get_element())

def test_overide_throttle():
    oa = OSC.OverrideThrottleAction(0.4,True)
    OSC.prettyprint(oa.get_element())

def test_visual_action():
    va = OSC.VisibilityAction(True,False,True)
    OSC.prettyprint(va.get_element())

def test_abs_sync_action():
    
    asa = OSC.AbsoluteSynchronizeAction('Ego',OSC.WorldPosition(0,0,0,0,0,0),OSC.WorldPosition(10,0,0,0,0,0),20)
    OSC.prettyprint(asa.get_element())

def test_rel_sync_action():
    
    asa = OSC.RelativeSynchronizeAction('Ego',OSC.WorldPosition(0,0,0,0,0,0),OSC.WorldPosition(10,0,0,0,0,0),20,'delta')
    OSC.prettyprint(asa.get_element())


def test_follow_traj_action_polyline():

    positionlist = []
    positionlist.append(OSC.RelativeLanePosition(10,0.5,-3,'Ego'))
    positionlist.append(OSC.RelativeLanePosition(10,1,-3,'Ego'))
    positionlist.append(OSC.RelativeLanePosition(10,-1,-3,'Ego'))
    positionlist.append(OSC.RelativeLanePosition(10,0,-3,'Ego'))
    OSC.prettyprint(positionlist[0].get_element())
    polyline = OSC.Polyline([0,0.5,1,1.5],positionlist)


    traj = OSC.Trajectory('my_trajectory',False)
    traj.add_shape(polyline)

    trajact = OSC.FollowTrajectoryAction(traj,OSC.FollowMode.position)
    OSC.prettyprint(trajact.get_element())


def testParameterAddActions():
    OSC.prettyprint(OSC.ParameterAddAction('Myparam',3).get_element())

def testParameterMultiplyActions():
    OSC.prettyprint(OSC.ParameterMultiplyAction('Myparam',3).get_element())

def testParameterSetActions():
    OSC.prettyprint(OSC.ParameterSetAction('Myparam',3).get_element())

def test_trafficsignalstateaction():
    OSC.prettyprint(OSC.TrafficSignalStateAction('my signal','red').get_element())


def test_addEntity():
    OSC.prettyprint(OSC.AddEntityAction('my new thingy',OSC.WorldPosition()).get_element())

def test_deleteEntity():
    OSC.prettyprint(OSC.DeleteEntityAction('my new thingy').get_element())

def test_trafficsourceaction():
    
    prop = OSC.Properties()
    prop.add_file('mycontrollerfile.xml')
    controller = OSC.Controller('mycontroller',prop)

    traffic = OSC.TrafficDefinition('my traffic')
    traffic.add_controller(controller,0.5)
    traffic.add_controller(OSC.CatalogReference('ControllerCatalog','my controller'),0.5)

    traffic.add_vehicle(OSC.VehicleCategory.car,0.9)
    traffic.add_vehicle(OSC.VehicleCategory.bicycle,0.1)

    source_action = OSC.TrafficSourceAction(10,10,OSC.WorldPosition(),traffic,100)

    OSC.prettyprint(source_action.get_element())

    source_action = OSC.TrafficSourceAction(10,10,OSC.WorldPosition(),traffic)
    OSC.prettyprint(source_action.get_element())


def test_trafficsinkaction():
    
    prop = OSC.Properties()
    prop.add_file('mycontrollerfile.xml')
    controller = OSC.Controller('mycontroller',prop)

    traffic = OSC.TrafficDefinition('my traffic')
    traffic.add_controller(controller,0.5)
    traffic.add_controller(OSC.CatalogReference('ControllerCatalog','my controller'),0.5)

    traffic.add_vehicle(OSC.VehicleCategory.car,0.9)
    traffic.add_vehicle(OSC.VehicleCategory.bicycle,0.1)

    sink_action = OSC.TrafficSinkAction(10,10,OSC.WorldPosition(),traffic)
    OSC.prettyprint(sink_action.get_element())


    
def test_trafficswarmaction():
    
    prop = OSC.Properties()
    prop.add_file('mycontrollerfile.xml')
    controller = OSC.Controller('mycontroller',prop)

    traffic = OSC.TrafficDefinition('my traffic')
    traffic.add_controller(controller,0.5)
    traffic.add_controller(OSC.CatalogReference('ControllerCatalog','my controller'),0.5)

    traffic.add_vehicle(OSC.VehicleCategory.car,0.9)
    traffic.add_vehicle(OSC.VehicleCategory.bicycle,0.1)

    source_action = OSC.TrafficSourceAction(10,10,OSC.WorldPosition(),traffic,100)

    OSC.prettyprint(source_action.get_element())

    swarm_action = OSC.TrafficSwarmAction(10,20,10,2,10,'Ego',traffic)
    OSC.prettyprint(swarm_action.get_element())

    swarm_action = OSC.TrafficSwarmAction(10,20,10,2,10,'Ego',traffic,10)
    OSC.prettyprint(swarm_action.get_element())


def test_environmentaction():
    tod = OSC.TimeOfDay(True,2020,10,1,18,30,30)
    weather = OSC.Weather(OSC.CloudState.free,100,0,1,OSC.PrecipitationType.dry,1)
    rc = OSC.RoadCondition(1)

    env = OSC.Environment(tod,weather,rc)
    ea = OSC.EnvironmentAction('myaction',env)
    OSC.prettyprint(ea.get_element())