# MottaBonora-CarlaSim

Links:
Carla github                    https://github.com/carla-simulator/carla
Carca documentation             https://carla.readthedocs.io/en/latest/
Scenario Runner github          https://github.com/carla-simulator/scenario_runner
Scenario Runner documentation   https://carla-scenariorunner.readthedocs.io/en/latest/

Downloads:
Carla 0.9.9                     https://github.com/carla-simulator/carla/releases/tag/0.9.9
Scenario Runner 0.9.9           https://github.com/carla-simulator/scenario_runner/releases/tag/v0.9.9

Installation:
- extract Carla and Scenario runner 
- update system environment variables:
       add a variable named PYTHONPATH with the following paths changing the path according 
       to the arrangement of your folders: 
       
     ![PYTHONPATH](https://github.com/mottajacopo/MottaBonora-CarlaSim/blob/main/PYTHONPATH.PNG)
     
     
     
# Carla guide

1- Aprire il cmd nella cartella di Carla (sul desktop)
	Lanciare il server con il seguente comando:
	CarlaUE4.exe -quality-level=Epic

2- Aprire il cmd nella cartella PythonAPI/util
	Lanciare il seguente comando per scegliere la mappa (la milgiore è town05):
	python config.py --map Town05

3- Aprire il cmd nella cartella PythonAPI/examples
	Lanciare il seguente comando per polopare la mappa:
	python spawn_npc.py -n 80    #spawna 80 agenti

3- Aprire il cmd nella cartella PythonAPI/examples
	Lanciare il seguente comando per abilitare il meteo e l'ora del giorno dinamica:
	python dynamic_weather.py

4- Aprire il cmd nella cartella PythonAPI/examples
	Lanciare il seguente comando per avviare il client in guida manuale
	python manual_control.py

5- Una volta nel client:
	 P            : toggle autopilot
 	 TAB          : change sensor position (mettere camera frontale)
        C            : change weather (funziona se dynamic weather è disabilitato)
        F1           : toggle HUD

6- Con OBS registrare una volta che si verifica uno scenario
