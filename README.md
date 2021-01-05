# MottaBonora-CarlaSim

**Links:**  
	Carla github                    https://github.com/carla-simulator/carla  
	Carca documentation             https://carla.readthedocs.io/en/latest/  
	Scenario Runner github          https://github.com/carla-simulator/scenario_runner  
	Scenario Runner documentation   https://carla-scenariorunner.readthedocs.io/en/latest/  

**Downloads:**  
	Carla 0.9.9                     https://github.com/carla-simulator/carla/releases/tag/0.9.9  
	Scenario Runner 0.9.9           https://github.com/carla-simulator/scenario_runner/releases/tag/v0.9.9  
	Carla 0.9.11                    https://github.com/carla-simulator/carla/releases/tag/0.9.11  
	Scenario Runner repo  		https://github.com/carla-simulator/scenario_runner  

**Installation:**  
- extract Carla release and Scenario runner (release or cloned repo)
- update system environment variables:
       add a variable named PYTHONPATH with the following paths changing the path according 
       to the arrangement of your folders and the version of carla you want to use: 
       
     ![PYTHONPATH](https://github.com/mottajacopo/MottaBonora-CarlaSim/blob/main/PYTHONPATH.PNG)
     
     
     
# Carla guide

**1-** Aprire il cmd nella cartella di Carla (sul desktop)
	Lanciare il server con il seguente comando:
	
	CarlaUE4.exe -quality-level=High

**2-** Aprire il cmd nella cartella PythonAPI/util
	Lanciare il seguente comando per scegliere la mappa (la milgiore è town05):
	
	python config.py --map Town05

**3-** Aprire il cmd nella cartella PythonAPI/examples
	Lanciare il seguente comando per polopare la mappa:
	
	python spawn_npc.py -n 50 -w 15    #spawna 50 vehicles and 15 pedestrians

**4-** Aprire il cmd nella cartella PythonAPI/examples
	Lanciare il seguente comando per abilitare il meteo e l'ora del giorno dinamica:
	
	python dynamic_weather.py

**5-** Aprire il cmd nella cartella PythonAPI/examples
	Lanciare il seguente comando per avviare il client in guida manuale
	
	python manual_control.py 

**6-** Una volta nel client:

	 P            : toggle autopilot
 	 TAB          : change sensor position (mettere camera frontale)
     C            : change weather (funziona se dynamic weather è disabilitato)
     F1           : toggle HUD


# Scenario Runner guide

**1-**  Lanciare il server cliccando su CarlaUE4.exe della cartella di Carla

**2-**  Aprire il cmd nella cartella scneraio_runner 0.9.9
		Lanciare il seguente comando:
		
		python scenario_runner.py --scenario NomeScenario_numero --reloadWorld	
		es : python scenario_runner.py --scenario FollowLeadingVehicle_1 --reloadWorld
					     
	Lista scenari:
		FollowLeadingVehicle
		FollowLeadingVehicleWithObstacle
		VehicleTurningRight
		VehicleTurningLeft
		OppositeVehicleRunningRedLight
		StationaryObjectCrossing
		DynamicObjectCrossing
		NoSignalJunctionCrossing
		ControlLoss
		ManeuverOppositeDirection
		OtherLeadingVehicle
		SignalizedJunctionRightTurn
		SignalizedJunctionLeftTurn
			
 Si possono lanciare anche tutti gli scenari di una specifica classe con questo comendo
 
 		python scenario_runner.py --scenario group:NomeScenario
		es : python scenario_runner.py --scenario group:FollowLeadingVehicle
		
 Invece per lanciare uno scenario in formato openscenario si utilizza il seguente comando (specificando il path del file .xosc)
 		
		python scenario_runner.py --openscenario path_al_file_xosc
		es : python scenario_runner.py --openscenario C:\Users\studente1\Downloads\scenario_runner-master\srunner\examples\FollowLeadingVehicle_1 --reloadWorld

**3-** Dalla cartella di scenario runner avviare il client eseguendo manual_controll.py

		 python manual_controll.py --autopilot si può far partire l'auto in autopilota da subito
	
**4-** Una volta nel client:

	P            : toggle autopilot
 	TAB          : change sensor position (mettere camera frontale)
    C            : change weather (funziona se dynamic weather è disabilitato)
    F1           : toggle HUD
