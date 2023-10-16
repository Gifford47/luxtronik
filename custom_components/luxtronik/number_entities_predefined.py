"""Luxtronik number sensors definitions."""
# region Imports
from homeassistant.components.number import NumberMode
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import (
    PERCENTAGE,
    UnitOfElectricPotential,
    UnitOfTemperature,
    UnitOfTime,
)
from homeassistant.helpers.entity import EntityCategory

from .const import (
    DeviceKey,
    LuxCalculation as LC,
    LuxParameter as LP,
    LuxVisibility as LV,
    SensorAttrFormat,
    SensorAttrKey as SA,
    SensorKey,
)
from .model import (
    LuxtronikEntityAttributeDescription as attr,
    LuxtronikNumberDescription,
)

# endregion Imports

# TODO:
# ID_Einst_HysHzExEn_akt TEE Heizung    2 1-15
# ID_Einst_HysBwExEn_akt TEE Warmw.     5 1-15
# T-Diff. Speicher max 70 20-95
# T-Diff. Koll. max 110 90-120

NUMBER_SENSORS: list[LuxtronikNumberDescription] = [
    # region Main heatpump
    LuxtronikNumberDescription(
        key=SensorKey.RELEASE_SECOND_HEAT_GENERATOR,
        luxtronik_key=LP.P0090_RELEASE_SECOND_HEAT_GENERATOR,
        icon="mdi:download-lock",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=-20.0,
        native_max_value=20.0,
        native_step=0.1,
        mode=NumberMode.BOX,
        entity_category=EntityCategory.CONFIG,
        factor=0.1,
        visibility=LV.V0061_SECOND_HEAT_GENERATOR,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.RELEASE_TIME_SECOND_HEAT_GENERATOR,
        luxtronik_key=LP.P0992_RELEASE_TIME_SECOND_HEAT_GENERATOR,
        translation_key_name="release_second_heat_generator",
        icon="mdi:timer-play",
        device_class=SensorDeviceClass.DURATION,
        native_unit_of_measurement=UnitOfTime.MINUTES,
        native_min_value=20,
        native_max_value=120,
        native_step=5,
        entity_category=EntityCategory.CONFIG,
        factor=1,
        visibility=LV.V0061_SECOND_HEAT_GENERATOR,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.EFFICIENCY_PUMP_NOMINAL,
        luxtronik_key=LP.P0867_EFFICIENCY_PUMP_NOMINAL,
        translation_key_name=SensorKey.EFFICIENCY_PUMP_NOMINAL,
        icon="mdi:leaf-circle-outline",
        device_class=SensorDeviceClass.VOLTAGE,
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        native_min_value=3.0,
        native_max_value=10.0,
        native_step=0.5,
        entity_category=EntityCategory.CONFIG,
        factor=0.01,
        entity_registry_enabled_default=False,
        visibility=LV.V0239_EFFICIENCY_PUMP_NOMINAL,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.EFFICIENCY_PUMP_MINIMAL,
        luxtronik_key=LP.P0868_EFFICIENCY_PUMP_MINIMAL,
        translation_key_name=SensorKey.EFFICIENCY_PUMP_MINIMAL,
        icon="mdi:leaf",
        device_class=SensorDeviceClass.VOLTAGE,
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        native_min_value=3.0,
        native_max_value=10.0,
        native_step=0.5,
        entity_category=EntityCategory.CONFIG,
        factor=0.01,
        entity_registry_enabled_default=False,
        visibility=LV.V0240_EFFICIENCY_PUMP_MINIMAL,
    ),
    # endregion Main heatpump
    # region Heating
    LuxtronikNumberDescription(
        key=SensorKey.HEATING_TARGET_CORRECTION,
        luxtronik_key=LP.P0001_HEATING_TARGET_CORRECTION,
        device_key=DeviceKey.heating,
        icon="mdi:plus-minus-variant",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=-5.0,
        native_max_value=5.0,
        native_step=0.1,
        mode=NumberMode.BOX,
        update_interval=None,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.PUMP_OPTIMIZATION_TIME,
        luxtronik_key=LP.P0864_PUMP_OPTIMIZATION_TIME,
        translation_key_name="pump_optimization",
        device_key=DeviceKey.heating,
        icon="mdi:timer-settings",
        device_class=SensorDeviceClass.DURATION,
        native_unit_of_measurement=UnitOfTime.MINUTES,
        native_min_value=5,
        native_max_value=180,
        native_step=5,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        factor=1,
        visibility=LV.V0144_PUMP_OPTIMIZATION,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.HEATING_THRESHOLD_TEMPERATURE,
        luxtronik_key=LP.P0700_HEATING_THRESHOLD_TEMPERATURE,
        translation_key_name="heating_threshold",
        device_key=DeviceKey.heating,
        icon="mdi:download-outline",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=5.0,
        native_max_value=30.0,
        native_step=0.5,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.HEATING_MIN_FLOW_OUT_TEMPERATURE,
        luxtronik_key=LP.P0979_HEATING_MIN_FLOW_OUT_TEMPERATURE,
        device_key=DeviceKey.heating,
        icon="mdi:waves-arrow-left",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=5.0,
        native_max_value=30.0,
        native_step=0.5,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        factor=0.1,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.HEATING_CIRCUIT_CURVE1_TEMPERATURE,
        luxtronik_key=LP.P0011_HEATING_CIRCUIT_CURVE1_TEMPERATURE,
        device_key=DeviceKey.heating,
        icon="mdi:chart-bell-curve",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=20.0,
        native_max_value=70.0,
        native_step=0.5,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.HEATING_CIRCUIT_CURVE2_TEMPERATURE,
        luxtronik_key=LP.P0012_HEATING_CIRCUIT_CURVE2_TEMPERATURE,
        device_key=DeviceKey.heating,
        icon="mdi:chart-bell-curve",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=5.0,
        native_max_value=35.0,
        native_step=0.5,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.HEATING_CIRCUIT_CURVE_NIGHT_TEMPERATURE,
        luxtronik_key=LP.P0013_HEATING_CIRCUIT_CURVE_NIGHT_TEMPERATURE,
        device_key=DeviceKey.heating,
        icon="mdi:chart-bell-curve",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=-15.0,
        native_max_value=10.0,
        native_step=0.5,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.HEATING_CIRCUIT2_CURVE1_TEMPERATURE,
        luxtronik_key=LP.P0014_HEATING_CIRCUIT2_CURVE1_TEMPERATURE,
        device_key=DeviceKey.heating,
        icon="mdi:chart-bell-curve",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=20.0,
        native_max_value=70.0,
        native_step=0.5,
        factor=0.1,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        visibility=LV.V0008_MK2,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.HEATING_CIRCUIT2_CURVE2_TEMPERATURE,
        luxtronik_key=LP.P0015_HEATING_CIRCUIT2_CURVE2_TEMPERATURE,
        device_key=DeviceKey.heating,
        icon="mdi:chart-bell-curve",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=5.0,
        native_max_value=35.0,
        native_step=0.5,
        factor=0.1,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        visibility=LV.V0008_MK2,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.HEATING_CIRCUIT2_CURVE_NIGHT_TEMPERATURE,
        luxtronik_key=LP.P0016_HEATING_CIRCUIT2_CURVE_NIGHT_TEMPERATURE,
        device_key=DeviceKey.heating,
        icon="mdi:chart-bell-curve",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=-15.0,
        native_max_value=10.0,
        native_step=0.5,
        factor=0.1,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        visibility=LV.V0008_MK2,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.HEATING_CIRCUIT3_CURVE1_TEMPERATURE,
        luxtronik_key=LP.P0774_HEATING_CIRCUIT3_CURVE1_TEMPERATURE,
        device_key=DeviceKey.heating,
        icon="mdi:chart-bell-curve",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=20.0,
        native_max_value=70.0,
        native_step=0.5,
        factor=0.1,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        visibility=LV.V0211_MK3,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.HEATING_CIRCUIT3_CURVE2_TEMPERATURE,
        luxtronik_key=LP.P0775_HEATING_CIRCUIT3_CURVE2_TEMPERATURE,
        device_key=DeviceKey.heating,
        icon="mdi:chart-bell-curve",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=5.0,
        native_max_value=35.0,
        native_step=0.5,
        factor=0.1,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        visibility=LV.V0211_MK3,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.HEATING_CIRCUIT3_CURVE_NIGHT_TEMPERATURE,
        luxtronik_key=LP.P0776_HEATING_CIRCUIT3_CURVE_NIGHT_TEMPERATURE,
        device_key=DeviceKey.heating,
        icon="mdi:chart-bell-curve",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=-15.0,
        native_max_value=10.0,
        native_step=0.5,
        factor=0.1,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        visibility=LV.V0211_MK3,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.HEATING_NIGHT_LOWERING_TO_TEMPERATURE,
        luxtronik_key=LP.P0111_HEATING_NIGHT_LOWERING_TO_TEMPERATURE,
        device_key=DeviceKey.heating,
        icon="mdi:thermometer-low",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=-20.0,
        native_max_value=10.0,
        native_step=0.5,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        factor=0.1,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.HEATING_HYSTERESIS,
        luxtronik_key=LP.P0088_HEATING_HYSTERESIS,
        device_key=DeviceKey.heating,
        icon="mdi:thermometer",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.KELVIN,
        native_min_value=0.5,
        native_max_value=6.0,
        native_step=0.1,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        factor=0.1,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.HEATING_MAX_FLOW_OUT_INCREASE_TEMPERATURE,
        luxtronik_key=LP.P0089_HEATING_MAX_FLOW_OUT_INCREASE_TEMPERATURE,
        device_key=DeviceKey.heating,
        icon="mdi:thermometer",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.KELVIN,
        native_min_value=1.0,
        native_max_value=7.0,
        native_step=0.1,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        factor=0.1,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.HEATING_MAXIMUM_CIRCULATION_PUMP_SPEED,
        luxtronik_key=LP.P1032_HEATING_MAXIMUM_CIRCULATION_PUMP_SPEED,
        device_key=DeviceKey.heating,
        icon="mdi:speedometer",
        device_class=SensorDeviceClass.SPEED,
        native_unit_of_measurement=PERCENTAGE,
        native_min_value=0,
        native_max_value=100,
        native_step=10,
        entity_category=EntityCategory.CONFIG,
        entity_registry_enabled_default=False,
    ),
    # 0% Regelung nur nach Außenemperatur
    # 100% 1K Temperaturdifferenz im Raum führt zu 1K Anpassung der Rücklauf-Solltemperatur <-- empf. Fussbodenheizung
    # 200% 1K Temperaturdifferenz im Raum führt zu 2K Anpassung der Rücklauf-Solltemperatur <-- empf. Radiatoren / Gebläsekonvektoren
    LuxtronikNumberDescription(
        key=SensorKey.HEATING_ROOM_TEMPERATURE_IMPACT_FACTOR,
        luxtronik_key=LP.P0980_HEATING_ROOM_TEMPERATURE_IMPACT_FACTOR,
        device_key=DeviceKey.heating,
        icon="mdi:thermometer-chevron-up",
        device_class=None,
        native_unit_of_measurement=PERCENTAGE,
        native_min_value=0,
        native_max_value=200,
        native_step=10,
        mode=NumberMode.BOX,
        entity_category=EntityCategory.CONFIG,
        entity_registry_enabled_default=False,
        visibility=LV.V0122_ROOM_THERMOSTAT,
    ),
    # endregion Heating
    # region Domestic water
    LuxtronikNumberDescription(
        key=SensorKey.DHW_TARGET_TEMPERATURE,
        luxtronik_key=LP.P0002_DHW_TARGET_TEMPERATURE,
        device_key=DeviceKey.domestic_water,
        mode=NumberMode.BOX,
        icon="mdi:thermometer-water",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=-40.0,
        native_max_value=60.0,
        native_step=1.0,
        update_interval=None,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.DHW_HYSTERESIS,
        luxtronik_key=LP.P0074_DHW_HYSTERESIS,
        device_key=DeviceKey.domestic_water,
        icon="mdi:thermometer",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.KELVIN,
        native_min_value=1.0,
        native_max_value=30.0,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        native_step=0.1,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.DHW_THERMAL_DESINFECTION_TARGET,
        luxtronik_key=LP.P0047_DHW_THERMAL_DESINFECTION_TARGET,
        device_key=DeviceKey.domestic_water,
        icon="mdi:thermometer-high",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=50.0,
        native_max_value=70.0,
        native_step=1.0,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        factor=0.1,
        extra_attributes=[
            attr(
                SA.LAST_THERMAL_DESINFECTION,
                LC.C0017_DHW_TEMPERATURE,
                SensorAttrFormat.TIMESTAMP_LAST_OVER,
                True,
            ),
        ],
    ),
    # region Solar
    LuxtronikNumberDescription(
        key=SensorKey.SOLAR_PUMP_ON_DIFFERENCE_TEMPERATURE,
        luxtronik_key=LP.P0122_SOLAR_PUMP_ON_DIFFERENCE_TEMPERATURE,
        device_key=DeviceKey.domestic_water,
        icon="mdi:pump",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.KELVIN,
        native_min_value=2.0,
        native_max_value=15.0,
        native_step=0.5,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        visibility=LV.V0250_SOLAR,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.SOLAR_PUMP_OFF_DIFFERENCE_TEMPERATURE,
        luxtronik_key=LP.P0123_SOLAR_PUMP_OFF_DIFFERENCE_TEMPERATURE,
        device_key=DeviceKey.domestic_water,
        icon="mdi:pump-off",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.KELVIN,
        native_min_value=0.5,
        native_max_value=10.0,
        native_step=0.5,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        visibility=LV.V0250_SOLAR,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.SOLAR_PUMP_OFF_MAX_DIFFERENCE_TEMPERATURE_BOILER,
        luxtronik_key=LP.P0289_SOLAR_PUMP_OFF_MAX_DIFFERENCE_TEMPERATURE_BOILER,
        device_key=DeviceKey.domestic_water,
        icon="mdi:water-boiler-alert",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=20,
        native_max_value=95,
        native_step=1,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        visibility=LV.V0250_SOLAR,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.SOLAR_PUMP_MAX_TEMPERATURE_COLLECTOR,
        luxtronik_key=LP.P0883_SOLAR_PUMP_MAX_TEMPERATURE_COLLECTOR,
        device_key=DeviceKey.domestic_water,
        icon="mdi:solar-panel-large",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=90,
        native_max_value=120,
        native_step=1,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        visibility=LV.V0038_SOLAR_COLLECTOR,
    ),
    # endregion Solar
    # endregion Domestic water
    # region Cooling
    LuxtronikNumberDescription(
        key=SensorKey.COOLING_OUTDOOR_TEMP_THRESHOLD,
        luxtronik_key=LP.P0110_COOLING_OUTDOOR_TEMP_THRESHOLD,
        device_key=DeviceKey.cooling,
        icon='mdi:sun-thermometer',
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=18.0,
        native_max_value=30.0,
        native_step=0.5,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        visibility=LV.V0005_COOLING,
    ),    
    LuxtronikNumberDescription(
        key=SensorKey.COOLING_START_DELAY_HOURS,
        luxtronik_key=LP.P0850_COOLING_START_DELAY_HOURS,
        device_key=DeviceKey.cooling,
        icon='mdi:clock-start',
        native_unit_of_measurement=UnitOfTime.HOURS,
        native_min_value=0.0,
        native_max_value=12.0,
        native_step=0.5,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        visibility=LV.V0005_COOLING,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.COOLING_STOP_DELAY_HOURS,
        luxtronik_key=LP.P0851_COOLING_STOP_DELAY_HOURS,
        device_key=DeviceKey.cooling,
        icon='mdi:clock-end',
        native_unit_of_measurement=UnitOfTime.HOURS,
        native_min_value=0.0,
        native_max_value=12.0,
        native_step=0.5,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        visibility=LV.V0005_COOLING,
    ),
    LuxtronikNumberDescription(
        key=SensorKey.COOLING_TARGET_TEMPERATURE_MK1,
        luxtronik_key=LP.P0132_COOLING_TARGET_TEMPERATURE_MK1,
        device_key=DeviceKey.cooling,
        icon='mdi:sun-thermometer',
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=18.0,
        native_max_value=30.0,
        native_step=0.5,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        visibility=LP.P0042_MK1_TYPE,
    ), 
    LuxtronikNumberDescription(
        key=SensorKey.COOLING_TARGET_TEMPERATURE_MK2,
        luxtronik_key=LP.P0133_COOLING_TARGET_TEMPERATURE_MK2,
        device_key=DeviceKey.cooling,
        icon='mdi:sun-thermometer',
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=18.0,
        native_max_value=30.0,
        native_step=0.5,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        visibility=LP.P0130_MK2_TYPE,
    ), 
    LuxtronikNumberDescription(
        key=SensorKey.COOLING_TARGET_TEMPERATURE_MK3,
        luxtronik_key=LP.P0966_COOLING_TARGET_TEMPERATURE_MK3,
        device_key=DeviceKey.cooling,
        icon='mdi:sun-thermometer',
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_min_value=18.0,
        native_max_value=30.0,
        native_step=0.5,
        entity_category=EntityCategory.CONFIG,
        mode=NumberMode.BOX,
        visibility=LP.P0780_MK3_TYPE,
    ), 
    # endregion Cooling
]

