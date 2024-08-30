from PIL import Image
import csv

LOGO_IMAGE_DARK = "images/gm-dark.png"
image_dark = Image.open(LOGO_IMAGE_DARK)

LOGO_IMAGE_LIGHT = "images/gm-light.png"
image_light = Image.open(LOGO_IMAGE_LIGHT)

PAGE_IMAGE = "images/gmsitelogo.png"
image_home = Image.open(PAGE_IMAGE)

SQL_IMAGE = "images/SQL_Layout.png"
image_sql = Image.open(SQL_IMAGE)

custom_css = {
    ".ag-header-cell-label": {"justify-content": "center"},
    ".ag-header-group-cell-label": {"justify-content": "center"},
    ".ag-root-wrapper": {"border-radius": "10px"},
    "#gridToolBar": {"padding-bottom": "0px !important"}
}

conversion = {
    'N':('lb',0.224809),
    'm':('in',39.3701),
    'rad':('deg',57.2958),
    'Nm':('ft/lb',0.7376),
    'm/s':('mph',2.23694),
    'W':('hp',0.001341),
    'Pa':('psi',0.000145),
    'K':('F',-459.67),
    'm/s^2':('ft/s^2',3.2808399)
    }

lookup = {
    'HybridMGUCurrent':'Amp',
    'DCHeadErrorAngleLookAhead1':'Degrees',
    'DCHeadErrorAngleLookAhead2':'Degrees',
    'AirMixingRatioWorld':'g/kg',
    'EngineFuelFlowMassRate':'grams/sec',
    'TireEnergyTotalLF':'J',
    'TireEnergyTotalLR':'J',
    'TireEnergyTotalRF':'J',
    'TireEnergyTotalRR':'J',
    'HybridESSDeployLapEnergy':'Joule',
    'HybridESSHarvestLapEnergy':'Joule',
    'HybridESSStoredEnergy':'Joule',
    'AirTempWorld':'K',
    'BrakeRotorSurfaceTempLF':'K',
    'BrakeRotorSurfaceTempLR':'K',
    'BrakeRotorSurfaceTempRF':'K',
    'BrakeRotorSurfaceTempRR':'K',
    'EnginePlenumTemp':'K',
    'RoadTemp':'K',
    'TireCoreTempLF':'K',
    'TireCoreTempLR':'K',
    'TireCoreTempRF':'K',
    'TireCoreTempRR':'K',
    'TireSurfaceTempLF':'K',
    'TireSurfaceTempLR':'K',
    'TireSurfaceTempRF':'K',
    'TireSurfaceTempRR':'K',
    'EngineFuelUsedMass':'Kg',
    'AirDensityWorld':'kg/m^3',
    'AeroHeightFront':'m',
    'AeroHeightRear':'m',
    'ChassisBottom1Height':'m',
    'ChassisBottom2Height':'m',
    'ChassisBottom3Height':'m',
    'ChassisBottom4Height':'m',
    'ChassisBottom5Height':'m',
    'ChassisBottom6Height':'m',
    'ChassisLaserHeightLF':'m',
    'ChassisLaserHeightRear':'m',
    'ChassisLaserHeightRF':'m',
    'ChassisPositionWorldXVehFrame':'m',
    'ChassisPositionWorldXWorldFrame':'m',
    'ChassisPositionWorldYVehFrame':'m',
    'ChassisPositionWorldYWorldFrame':'m',
    'ChassisPositionWorldZVehFrame':'m',
    'ChassisPositionWorldZWorldFrame':'m',
    'ChassisRideHeightLF':'m',
    'ChassisRideHeightRear':'m',
    'ChassisRideHeightRF':'m',
    'DamperDispLF':'m',
    'DamperDispLR':'m',
    'DamperDispRF':'m',
    'DamperDispRR':'m',
    'DamperLengthLF':'m',
    'DamperLengthLR':'m',
    'DamperLengthRF':'m',
    'DamperLengthRR':'m',
    'DCLatErrorDistLookAhead1':'m',
    'DCLatErrorDistLookAhead2':'m',
    'DCLatLookAhead1Distance':'m',
    'DCLatLookAhead2Distance':'m',
    'DCLongLookAhead1Distance':'m',
    'DCLongLookAhead2Distance':'m',
    'Distance':'m',
    'RoadPlaneLocationDistX':'m',
    'RoadPlaneLocationDistY':'m',
    'RoadPlaneLocationDistZ':'m',
    'RoadPositionWorldZLF':'m',
    'RoadPositionWorldZLR':'m',
    'RoadPositionWorldZRF':'m',
    'RoadPositionWorldZRR':'m',
    'SpringDispLF':'m',
    'SpringDispLR':'m',
    'SpringDispRF':'m',
    'SpringDispRR':'m',
    'SteeringRackDisp':'m',
    'SuspFVICHeightLF':'m',
    'SuspFVICHeightLR':'m',
    'SuspFVICHeightRF':'m',
    'SuspFVICHeightRR':'m',
    'SuspFVICLengthLF':'m',
    'SuspFVICLengthLR':'m',
    'SuspFVICLengthRF':'m',
    'SuspFVICLengthRR':'m',
    'SuspRCGroundYFront':'m',
    'SuspRCGroundYRear':'m',
    'SuspRCGroundZFront':'m',
    'SuspRCGroundZRear':'m',
    'SuspSVICHeightLF':'m',
    'SuspSVICHeightLR':'m',
    'SuspSVICHeightRF':'m',
    'SuspSVICHeightRR':'m',
    'SuspSVICLengthLF':'m',
    'SuspSVICLengthLR':'m',
    'SuspSVICLengthRF':'m',
    'SuspSVICLengthRR':'m',
    'ThirdSpringDispFront':'m',
    'ThirdSpringDispRear':'m',
    'TireDeflectionZLF':'m',
    'TireDeflectionZLR':'m',
    'TIreDeflectionZRF':'m',
    'TireDeflectionZRR':'m',
    'TireEffectiveRadiusLF':'m',
    'TireEffectiveRadiusLR':'m',
    'TireEffectiveRadiusRF':'m',
    'TireEffectiveRadiusRR':'m',
    'TireLoadedRadiusLF':'m',
    'TireLoadedRadiusLR':'m',
    'TireLoadedRadiusRF':'m',
    'TireLoadedRadiusRR':'m',
    'TirePositionWorldXLF':'m',
    'TirePositionWorldXLR':'m',
    'TirePositionWorldXRF':'m',
    'TirePositionWorldXRR':'m',
    'TirePositionWorldYLF':'m',
    'TirePositionWorldYLR':'m',
    'TirePositionWorldYRF':'m',
    'TirePositionWorldYRR':'m',
    'TirePositionWorldZLF':'m',
    'TirePositionWorldZLR':'m',
    'TirePositionWorldZRF':'m',
    'TirePositionWorldZRR':'m',
    'WeightJackerDispLR':'m',
    'WeightJackerDispRR':'m',
    'WheelPositionGroundZLF':'m',
    'WheelPositionGroundZLR':'m',
    'WheelPositionGroundZRF':'m',
    'WheelPositionGroundZRR':'m',
    'WheelPositionVehXLF':'m',
    'WheelPositionVehXLR':'m',
    'WheelPositionVehXRF':'m',
    'WheelPositionVehXRR':'m',
    'WheelPositionVehYLF':'m',
    'WheelPositionVehYLR':'m',
    'WheelPositionVehYRF':'m',
    'WheelPositionVehYRR':'m',
    'WheelPositionVehZLF':'m',
    'WheelPositionVehZLR':'m',
    'WheelPositionVehZRF':'m',
    'WheelPositionVehZRR':'m',
    'AeroRelVelX':'m/s',
    'AeroRelVelY':'m/s',
    'AeroRelVelZ':'m/s',
    'AirVelWorldMag':'m/s',
    'AirVelWorldX':'m/s',
    'AirVelWorldY':'m/s',
    'ChassisVelSlipSensor':'m/s',
    'ChassisVelXCG':'m/s',
    'ChassisVelXSlipSensor':'m/s',
    'ChassisVelYCG':'m/s',
    'ChassisVelYSlipSensor':'m/s',
    'ChassisVelZCG':'m/s',
    'DamperVelLF':'m/s',
    'DamperVelLR':'m/s',
    'DamperVelRF':'m/s',
    'DamperVelRR':'m/s',
    'DCLongCtrlErrorVelLookAhead1':'m/s',
    'DCLongCtrlErrorVelLookAhead2':'m/s',
    'TireDeflectionVelZLF':'m/s',
    'TireDeflectionVelZLR':'m/s',
    'TireDeflectionVelZRF':'m/s',
    'TireDeflectionVelZRR':'m/s',
    'TireVelXLF':'m/s',
    'TireVelXLR':'m/s',
    'TireVelXRF':'m/s',
    'TireVelXRR':'m/s',
    'TireVelYLF':'m/s',
    'TireVelYLR':'m/s',
    'TireVelYRF':'m/s',
    'TireVelYRR':'m/s',
    'VehicleCalcSpeed':'m/s',
    'VehicleSpeed':'m/s',
    'WheelCalcVelLF':'m/s',
    'WheelCalcVelLR':'m/s',
    'WheelCalcVelRF':'m/s',
    'WheelCalcVelRR':'m/s',
    'ChassisAccelXCG':'m/s^2',
    'ChassisAccelXFrtAxle':'m/s^2',
    'ChassisAccelXRrAxle':'m/s^2',
    'ChassisAccelYCG':'m/s^2',
    'ChassisAccelYFrtAxle':'m/s^2',
    'ChassisAccelYRrAxle':'m/s^2',
    'ChassisAccelZCG':'m/s^2',
    'ChassisAccelZFrtAxle':'m/s^2',
    'ChassisAccelZRrAxle':'m/s^2',
    'InerterAccelLF':'m/s^2',
    'InerterAccelLR':'m/s^2',
    'InerterAccelRF':'m/s^2',
    'InerterAccelRR':'m/s^2',
    'UprightAccelZLF':'m/s^2',
    'UprightAccelZLR':'m/s^2',
    'UprightAccelZRF':'m/s^2',
    'UprightAccelZRR':'m/s^2',
    'EnginePlenumPressure':'mBar',
    'AeroDragForce':'N',
    'AeroDragForceISO':'N',
    'AeroLiftForce':'N',
    'AeroLiftForceFront':'N',
    'AeroLiftForceISO':'N',
    'AeroLiftForceRear':'N',
    'AeroSideForce':'N',
    'AeroSideForceISO':'N',
    'ARBDroplinkForceLF':'N',
    'ARBDroplinkForceLR':'N',
    'ARBDroplinkForceRF':'N',
    'ARBDroplinkForceRR':'N',
    'BrakePedalForce':'N',
    'BrakePedalOutputForce':'N',
    'BrakePushrodForceFront':'N',
    'BrakePushrodForceRear':'N',
    'BumpstopForceLF':'N',
    'BumpstopForceLR':'N',
    'BumpstopForceRF':'N',
    'BumpstopForceRR':'N',
    'ChassisBottom1ForceX':'N',
    'ChassisBottom1ForceZ':'N',
    'ChassisBottom2ForceX':'N',
    'ChassisBottom2ForceZ':'N',
    'ChassisBottom3ForceX':'N',
    'ChassisBottom3ForceZ':'N',
    'ChassisBottom4ForceX':'N',
    'ChassisBottom4ForceZ':'N',
    'ChassisBottom5ForceX':'N',
    'ChassisBottom5ForceZ':'N',
    'ChassisBottom6ForceX':'N',
    'ChassisBottom6ForceZ':'N',
    'DamperForceLF':'N',
    'DamperForceLR':'N',
    'DamperForceRF':'N',
    'DamperForceRR':'N',
    'InerterForceLF':'N',
    'InerterForceLR':'N',
    'InerterForceRF':'N',
    'InerterForceRR':'N',
    'LatLoadTransferFront':'N',
    'LatLoadTransferRear':'N',
    'LatLoadTransferTotal':'N',
    'PushrodForceLF':'N',
    'PushrodForceLR':'N',
    'PushrodForceRF':'N',
    'PushrodForceRR':'N',
    'PushrodZeroedForceLF':'N',
    'PushrodZeroedForceLR':'N',
    'PushrodZeroedForceRF':'N',
    'PushrodZeroedForceRR':'N',
    'SpringForceLF':'N',
    'SpringForceLR':'N',
    'SpringForceRF':'N',
    'SpringForceRR':'N',
    'SteeringRackForce':'N',
    'SuspLateralJackingForceZLF':'N',
    'SuspLateralJackingForceZLR':'N',
    'SuspLateralJackingForceZRF':'N',
    'SuspLateralJackingForceZRR':'N',
    'SuspLongitudinalJackingForceZLF':'N',
    'SuspLongitudinalJackingForceZLR':'N',
    'SuspLongitudinalJackingForceZRF':'N',
    'SuspLongitudinalJackingForceZRR':'N',
    'ThirdSpringForceFront':'N',
    'ThirdSpringForceRear':'N',
    'TieRodForceLF':'N',
    'TieRodForceRF':'N',
    'TireDampingForceZLF':'N',
    'TireDampingForceZLR':'N',
    'TireDampingForceZRF':'N',
    'TireDampingForceZRR':'N',
    'TireForceAvailableXLF':'N',
    'TireForceAvailableXLR':'N',
    'TireForceAvailableXRF':'N',
    'TireForceAvailableXRR':'N',
    'TireForceAvailableYLF':'N',
    'TireForceAvailableYLR':'N',
    'TireForceAvailableYRF':'N',
    'TireForceAvailableYRR':'N',
    'TireForceXLF':'N',
    'TireForceXLR':'N',
    'TireForceXRF':'N',
    'TireForceXRR':'N',
    'TireForceYLF':'N',
    'TireForceYLR':'N',
    'TireForceYRF':'N',
    'TireForceYRR':'N',
    'TireForceZLF':'N',
    'TireForceZLR':'N',
    'TireForceZRF':'N',
    'TireForceZRR':'N',
    'TireZeroedForceZLF':'N',
    'TireZeroedForceZLR':'N',
    'TireZeroedForceZRF':'N',
    'TireZeroedForceZRR':'N',
    'ToeLinkForceLR':'N',
    'ToeLinkForceRR':'N',
    'WheelForceXLF':'N',
    'WheelForceXLR':'N',
    'WheelForceXRF':'N',
    'WheelForceXRR':'N',
    'WheelForceYLF':'N',
    'WheelForceYLR':'N',
    'WheelForceYRF':'N',
    'WheelForceYRR':'N',
    'WheelForceZLF':'N',
    'WheelForceZLR':'N',
    'WheelForceZRF':'N',
    'WheelForceZRR':'N',
    'TireSlipStiffnessYLF':'N/rad',
    'TireSlipStiffnessYLR':'N/rad',
    'TireSlipStiffnessYRF':'N/rad',
    'TireSlipStiffnessYRR':'N/rad',
    'AeroPitchMoment':'Nm',
    'AeroPitchMomentISO':'Nm',
    'AeroRollMoment':'Nm',
    'AeroRollMomentISO':'Nm',
    'AeroYawMoment':'Nm',
    'AeroYawMomentISO':'Nm',
    'ARBTorqueFront':'Nm',
    'ARBTorqueRear':'Nm',
    'BrakeRotorTorqueLF':'Nm',
    'BrakeRotorTorqueLR':'Nm',
    'BrakeRotorTorqueRF':'Nm',
    'BrakeRotorTorqueRR':'Nm',
    'EngineDriveabilityTorqueScaling':'Nm',
    'HalfshaftTorqueLR':'Nm',
    'HalfshaftTorqueRR':'Nm',
    'HybridMGUAppliedTorque':'Nm',
    'HybridMGUDemandTorque':'Nm',
    'HybridMGUTorque':'Nm',
    'LatYawMomentCG':'Nm',
    'LatYawMomentPotentialCG':'Nm',
    'LongYawMomentCG':'Nm',
    'NormLatYawMomentCG':'Nm',
    'NormLatYawMomentPotentialCG':'Nm',
    'NormLongYawMomentCG':'Nm',
    'NormTotalYawMomentCG':'Nm',
    'SteeringWheelTorque':'Nm',
    'TireMomentXLF':'Nm',
    'TireMomentXLR':'Nm',
    'TireMomentXRF':'Nm',
    'TireMomentXRR':'Nm',
    'TireMomentYLF':'Nm',
    'TireMomentYLR':'Nm',
    'TireMomentYRF':'Nm',
    'TireMomentYRR':'Nm',
    'TireMomentZLF':'Nm',
    'TireMomentZLR':'Nm',
    'TireMomentZRF':'Nm',
    'TireMomentZRR':'Nm',
    'TotalYawMomentCG':'Nm',
    'WheelMomentXLF':'Nm',
    'WheelMomentXLR':'Nm',
    'WheelMomentXRF':'Nm',
    'WheelMomentXRR':'Nm',
    'WheelMomentYLF':'Nm',
    'WheelMomentYLR':'Nm',
    'WheelMomentYRF':'Nm',
    'WheelMomentYRR':'Nm',
    'WheelMomentZLF':'Nm',
    'WheelMomentZLR':'Nm',
    'WheelMomentZRF':'Nm',
    'WheelMomentZRR':'Nm',
    'AirBaroPressWorld':'Pa',
    'BrakeCaliperPressLF':'Pa',
    'BrakeCaliperPressLR':'Pa',
    'BrakeCaliperPressRF':'Pa',
    'BrakeCaliperPressRR':'Pa',
    'BrakePressFront':'Pa',
    'BrakePressRear':'Pa',
    'TirePressLF':'Pa',
    'TirePressLR':'Pa',
    'TirePressRF':'Pa',
    'TirePressRR':'Pa',
    'AeroPitchAngle':'rad',
    'AeroPitchAngleISO':'rad',
    'AeroRollAngle':'rad',
    'AeroRollAngleISO':'rad',
    'AeroSteerAngle':'rad',
    'AeroSteerAngleISO':'rad',
    'AeroYawAngle':'rad',
    'AeroYawAngleISO':'rad',
    'ARBTwistAngleFront':'rad',
    'ARBTwistAngleRear':'rad',
    'AxleToeAngleFront':'rad',
    'AxleToeAngleRear':'rad',
    'ChassisAngleWorldXVehFrame':'rad',
    'ChassisAngleWorldXWorldFrame':'rad',
    'ChassisAngleWorldYVehFrame':'rad',
    'ChassisAngleWorldYWorldFrame':'rad',
    'ChassisAngleWorldZVehFrame':'rad',
    'ChassisAngleWorldZWorldFrame':'rad',
    'ChassisSlipAngleSlipSensor':'rad',
    'ChassisSlipAngleSprungCG':'rad',
    'SteeringWheelAngle':'rad',
    'SuspCasterAngleLF':'rad',
    'SuspCasterAngleLR':'rad',
    'SuspCasterAngleRF':'rad',
    'SuspCasterAngleRR':'rad',
    'SuspFVIAAngleGroundLF':'rad',
    'SuspFVIAAngleGroundLR':'rad',
    'SuspFVIAAngleGroundRF':'rad',
    'SuspFVIAAngleGroundRR':'rad',
    'SuspSVIAAngleGroundLF':'rad',
    'SuspSVIAAngleGroundLR':'rad',
    'SuspSVIAAngleGroundRF':'rad',
    'SuspSVIAAngleGroundRR':'rad',
    'TireBankAngleRoadLF':'rad',
    'TireBankAngleRoadLR':'rad',
    'TireBankAngleRoadRF':'rad',
    'TireBankAngleRoadRR':'rad',
    'TireSlipAngleLF':'rad',
    'TireSlipAngleLR':'rad',
    'TireSlipAngleRF':'rad',
    'TireSlipAngleRR':'rad',
    'WheelCamberAngleRoadLF':'rad',
    'WheelCamberAngleRoadLR':'rad',
    'WheelCamberAngleRoadRF':'rad',
    'WheelCamberAngleRoadRR':'rad',
    'WheelCamberAngleVehLF':'rad',
    'WheelCamberAngleVehLR':'rad',
    'WheelCamberAngleVehRF':'rad',
    'WheelCamberAngleVehRR':'rad',
    'WheelInclinationAngleRoadLF':'rad',
    'WheelInclinationAngleRoadLR':'rad',
    'WheelInclinationAngleRoadRF':'rad',
    'WheelInclinationAngleRoadRR':'rad',
    'WheelSteerAngleLF':'rad',
    'WheelSteerAngleRF':'rad',
    'WheelToeAngleLF':'rad',
    'WheelToeAngleLR':'rad',
    'WheelToeAngleRF':'rad',
    'WheelToeAngleRR':'rad',
    'WheelCamberKinGainLF':'rad/m',
    'WheelCamberKinGainLR':'rad/m',
    'WheelCamberKinGainRF':'rad/m',
    'WheelCamberKinGainRR':'rad/m',
    'ChassisRotAccelPitchCG':'rad/s^2',
    'ChassisRotAccelRollCG':'rad/s^2',
    'ChassisRotAccelYawCG':'rad/s^2',
    'ChassisRotVelPitchCG':'rad/sec',
    'ChassisRotVelRollCG':'rad/sec',
    'ChassisRotVelYawCG':'rad/sec',
    'EngineRotVel':'rad/sec',
    'EngineRotVelFiltered':'rad/sec',
    'TransOutputRotVel':'rad/sec',
    'WheelRotVelLF':'rad/sec',
    'WheelRotVelLR':'rad/sec',
    'WheelRotVelRF':'rad/sec',
    'WheelRotVelRR':'rad/sec',
    'EngineRotAccelFiltered':'rad/sec^2',
    'EngineRevHardLimiterCounterLap':'sec',
    'EngineRevSoftLimiterCounterLap':'sec',
    'HybridESSVoltageOC':'Volt',
    'HybridMGUVoltage':'Volt',
    'BrakePowerLF':'W',
    'BrakePowerLR':'W',
    'BrakePowerRF':'W',
    'BrakePowerRR':'W',
    'HybridMGUElectricalPower':'W',
    'HybridMGUMechanicalPower':'W',
    'HybridMGUPower':'W',
    'TirePowerTotalLF':'W',
    'TirePowerTotalLR':'W',
    'TirePowerTotalRF':'W',
    'TirePowerTotalRR':'W',
    'TirePowerXLF':'W',
    'TirePowerXLR':'W',
    'TirePowerXRF':'W',
    'TirePowerXRR':'W',
    'TirePowerYLF':'W',
    'TirePowerYLR':'W',
    'TirePowerYRF':'W',
    'TirePowerYRR':'W'
    }

def convert_columns(df, lookup, conversion_factors):
    for col in df.columns:
        # Find if any lookup key is in the column name
        for key, unit in lookup.items():
            if key in col:
                # Lookup the conversion factor
                if unit in conversion_factors:
                    new_unit, factor = conversion_factors[unit]
                    # Convert the column by the conversion factor
                    df[col] = df[col] * factor
                    # Rename the column to reflect the new unit
                    new_col_name = f"{col}_{new_unit}"
                    df.rename(columns={col: new_col_name}, inplace=True)
                break  # Stop after finding the first match
    return df

# Function to convert the dictionary to the desired format
def convert_to_nodes_format(data):
    nodes = []
    
    for main_key, sub_dict in data.items():
        # Create a node for the main key
        main_node = {"label": main_key, "value": main_key, "children": []}
        
        for sub_key, min_max_dict in sub_dict.items():
            # Create a node for the sub key with its children
            sub_node = {
                "label": sub_key, 
                "value": f"{main_key}_{sub_key}",  # Ensure value is unique
                "children": [
                    {
                        "label": min_max_key, 
                        "value": f"{main_key}_{sub_key}_{min_max_key}"
                    } 
                    for min_max_key in min_max_dict
                ]
            }
            main_node["children"].append(sub_node)
        
        nodes.append(main_node)
    
    return nodes

def filter_keys_with_multiple_sub_keys(data):
    """
    Separates the top-level keys in the dictionary into two dictionaries:
    - One with keys that have multiple sub-keys at any level.
    - One with all other items.
    
    :param data: The dictionary to process.
    :return: A tuple of two dictionaries: (filtered_keys_dict, other_items_dict)
    """
    filtered_keys_dict = {}
    other_items_dict = {}
    
    def has_multiple_sub_keys(d):
        """
        Recursively checks if any sub-dictionary has multiple sub-keys.
        """
        for key, value in d.items():
            if isinstance(value, dict):
                if len(value) > 1:
                    return True
                # Recursive check
                if has_multiple_sub_keys(value):
                    return True
        return False
    
    for key, value in data.items():
        if isinstance(value, dict):
            if has_multiple_sub_keys(value):
                filtered_keys_dict[key] = value
            else:
                other_items_dict[key] = value
    
    return filtered_keys_dict, other_items_dict

def combine_dictionaries(dict1, dict2):
    """
    Combines two dictionaries into one.
    
    :param dict1: The first dictionary.
    :param dict2: The second dictionary.
    :return: A dictionary containing all items from both dictionaries.
    """
    combined_dict = {**dict1, **dict2}
    return combined_dict

def flatten_dict_to_list(d, parent_key=''):
    """
    Flattens a nested dictionary into a list of concatenated key names.

    :param d: The dictionary to flatten.
    :param parent_key: The base key string to prepend to child keys.
    :return: A list of concatenated key names.
    """
    items = []
    
    for k, v in d.items():
        new_key = f"{parent_key}_{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict_to_list(v, new_key))
        else:
            items.append(new_key)
    
    return items