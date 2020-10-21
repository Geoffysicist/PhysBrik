EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "PhysBryk Power Supply "
Date "2020-10-21"
Rev "0.0.1"
Comp ""
Comment1 "9V Regulated"
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:R R1
U 1 1 5F8FC534
P 6850 2750
F 0 "R1" H 6780 2704 50  0000 R CNN
F 1 "240" H 6780 2795 50  0000 R CNN
F 2 "" V 6780 2750 50  0001 C CNN
F 3 "~" H 6850 2750 50  0001 C CNN
	1    6850 2750
	-1   0    0    1   
$EndComp
$Comp
L Regulator_Linear:LM317_TO-220 U1
U 1 1 5F8FD283
P 6450 2600
F 0 "U1" H 6450 2842 50  0000 C CNN
F 1 "LM317_TO-220" H 6450 2751 50  0000 C CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 6450 2850 50  0001 C CIN
F 3 "http://www.ti.com/lit/ds/symlink/lm317.pdf" H 6450 2600 50  0001 C CNN
	1    6450 2600
	1    0    0    -1  
$EndComp
$Comp
L Device:Battery_Cell BT1
U 1 1 5F9008E3
P 6150 3200
F 0 "BT1" H 6268 3296 50  0000 L CNN
F 1 "9V" H 6268 3205 50  0000 L CNN
F 2 "Connector_Wire:SolderWire-0.5sqmm_1x02_P4.8mm_D0.9mm_OD2.3mm" V 6150 3260 50  0001 C CNN
F 3 "~" V 6150 3260 50  0001 C CNN
	1    6150 3200
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole_Pad H1
U 1 1 5F9025E3
P 7250 2600
F 0 "H1" V 7204 2750 50  0000 L CNN
F 1 "Banana Plug Vout" V 7295 2750 50  0000 L CNN
F 2 "Connector:Banana_Jack_1Pin" H 7250 2600 50  0001 C CNN
F 3 "~" H 7250 2600 50  0001 C CNN
	1    7250 2600
	0    1    1    0   
$EndComp
$Comp
L Mechanical:MountingHole_Pad H2
U 1 1 5F90361B
P 7300 2900
F 0 "H2" H 7400 2949 50  0000 L CNN
F 1 "Banana Plug Gnd" H 7400 2858 50  0000 L CNN
F 2 "Connector:Banana_Jack_1Pin" H 7300 2900 50  0001 C CNN
F 3 "~" H 7300 2900 50  0001 C CNN
	1    7300 2900
	1    0    0    -1  
$EndComp
Wire Wire Line
	7300 3300 7300 3000
Wire Wire Line
	6450 2900 6850 2900
Connection ~ 6850 2900
Wire Wire Line
	6750 2600 6850 2600
Connection ~ 6850 2600
Wire Wire Line
	6850 2600 7150 2600
Wire Wire Line
	6150 3000 6150 2600
$Comp
L Device:R_POT RV1
U 1 1 5F90178B
P 7000 3150
F 0 "RV1" V 6793 3150 50  0000 C CNN
F 1 "2.5K" V 6884 3150 50  0000 C CNN
F 2 "Connector_Wire:SolderWire-0.5sqmm_1x02_P4.8mm_D0.9mm_OD2.3mm" H 7000 3150 50  0001 C CNN
F 3 "~" H 7000 3150 50  0001 C CNN
	1    7000 3150
	0    1    1    0   
$EndComp
Wire Wire Line
	6150 3300 7000 3300
Connection ~ 7000 3300
Wire Wire Line
	7000 3300 7300 3300
Wire Wire Line
	6850 2900 6850 3150
$EndSCHEMATC
