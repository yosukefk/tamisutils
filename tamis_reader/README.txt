
autogc_2019_bpa_338120240528180751696.txt
autogc_2020_bpa_338120240528180101145.txt
autogc_2021_bpa_338120240528175747253.txt
autogc_2022_bpa_338120240528175440496.txt
autogc_2023_bpa_338120240528175131246.txt
canister_2019_bpa_338120240528181326514.txt
canister_2020_bpa_338120240528181504554.txt
canister_2021_bpa_338120240528181600152.txt
canister_2022_bpa_338120240528181651451.txt
canister_2023_bpa_338120240528181742488.txt
met_2019_bpa_338120240528212647856.txt
met_2020_bpa_338120240528212104328.txt
met_2021_bpa_338120240528211559912.txt
met_2022_bpa_338120240528210850771.txt
met_2023_bpa_338120240528210422183.txt


	downloaded from here:
	https://www17.tceq.texas.gov/tamis/index.cfm

	see tamis.png for screenshot of what field to specify to grab data we
	need.  they are data range, duration, target parameter list, and
	region. one file for a year, for a set of parameters

	i used "AMCV AutoGC Parameters (48 params)", "AMCV Canister Parameters
	(85 params)", and "Meteorological Parameters (16 params)" for "Target
	List", and Durations are 1hour for met and austogc, 24 hour for
	canister.

alternatives/*


	in TAMIS used "Canister Parameters (101 params)", then changed
	duration to 1 hour or 24 hours.  
	
	For autogc, i got ~40 extra species see extra_autogc_species.csv

	For canister, i am getting exactly same set of species.  in any case,
	the approach i took should be fine.

	so, the appr

        
	see alternatives/target_parametrers.csv for which species are included
	as target



Parms.txt
Units.txt
Site.txt


	meta data for above, available from "Refernce" and "Site List" of the
	navigator bar in the TAMIS page above.

	Parameter Cd, Unit Cd in the data file can be linked to these to read
	the meaning. for example. Parameter Cd = 43202 is Ethane., Unit Cd 6
	is ppbv.  For Meth Cd, you have to see/use "methoad_all.csv", but 128
	is for Auto GC.  To use Site.txt, you have to catenate "State Cd",
	"COunty Cd" adn "Site ID" to come up with 10 digit number which is AQS
	Code in Site.tx.  so , e.g. 48245009 is "Beaumont Downtown" site.

methods_all.csv

	TCEQ does not have equivalent file for Meth Cd, and they said i can
	substitue with EPA's,
	https://aqs.epa.gov/aqsweb/documents/codetables/methods_all.html
	dont overuse this file, just use it to interpret method being used for
	measurment

reader.py
parameters_found.csv
sites_found.csv

	sample python code to read the data
	i also dumped what paramters are read, and which site has data.

tamis.png

	screen shot of TCEQ's tamis tool
