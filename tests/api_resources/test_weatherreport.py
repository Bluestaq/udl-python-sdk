# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    WeatherreportListResponse,
    WeatherreportTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.types.weatherreport import WeatherReportFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWeatherreport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        weatherreport = client.weatherreport.create(
            classification_marking="U",
            data_mode="TEST",
            lat=56.12,
            lon=-156.6,
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            report_type="FORECAST",
            source="Bluestaq",
        )
        assert weatherreport is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        weatherreport = client.weatherreport.create(
            classification_marking="U",
            data_mode="TEST",
            lat=56.12,
            lon=-156.6,
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            report_type="FORECAST",
            source="Bluestaq",
            id="WEATHER-REPORT-ID",
            act_weather="NO STATEMENT",
            agjson='{"type":"Polygon","coordinates":[ [ [ 67.3291113966927, 26.156175339112 ], [ 67.2580009640721, 26.091022064271 ], [ 67.1795862381682, 26.6637992964562 ], [ 67.2501237475598, 26.730115808233 ], [ 67.3291113966927, 26.156175339112 ] ] ] }',
            alt=123.12,
            andims=2,
            area="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            asrid=4326,
            atext="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            atype="ST_Polygon",
            bar_press=101.2,
            cc_event=True,
            cloud_cover=["OVERCAST", "BROKEN"],
            cloud_hght=[1.2, 2.2],
            contrail_hght_lower=123.123,
            contrail_hght_upper=123.123,
            data_level="MANDATORY",
            dew_point=15.6,
            dif_rad=234.5,
            dir_dev=9.1,
            en_route_weather="THUNDERSTORMS",
            external_id="GDSSMB022408301601304517",
            external_location_id="TMDS060AD4OG03CC",
            forecast_end_time=parse_datetime("2024-01-01T18:00:00.123Z"),
            forecast_start_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            geo_potential_alt=1000,
            hshear=3.8,
            icao="KAFF",
            icing_lower_limit=123.123,
            icing_upper_limit=123.123,
            id_airfield="8fb38d6d-a3de-45dd-8974-4e3ed73e9449",
            id_ground_imagery="GROUND-IMAGERY-ID",
            id_sensor="0129f577-e04c-441e-65ca-0a04a750bed9",
            id_site="AIRFIELD-ID",
            index_refraction=1.1,
            origin="THIRD_PARTY_DATASOURCE",
            orig_sensor_id="ORIGSENSOR-ID",
            precip_rate=3.4,
            qnh=1234.456,
            rad_vel=-0.04,
            rad_vel_beam1=4.4,
            rad_vel_beam2=-0.2,
            rad_vel_beam3=-0.2,
            rad_vel_beam4=11.4,
            rad_vel_beam5=4.1,
            rain_hour=1.2,
            raw_metar="KXYZ 241456Z 19012G20KT 10SM FEW120 SCT200 BKN250 26/M04 A2981 RMK AO2 PK WND 19026/1420 SLP068 T02611039 51015",
            raw_taf="KXYZ 051730Z 0518/0624 31008KT 3SM -SHRA BKN020 FM052300 30006KT 5SM -SHRA OVC030 PROB30 0604/0606 VRB20G35KT 1SM TSRA BKN015CB FM060600 25010KT 4SM -SHRA OVC050 TEMPO 0608/0611 2SM -SHRA OVC030 RMK NXT FCST BY 00Z=",
            ref_rad=56.7,
            rel_humidity=34.456,
            senalt=1.23,
            senlat=12.456,
            senlon=123.456,
            soil_moisture=3.5,
            soil_temp=22.4,
            solar_rad=1234.456,
            src_ids=["e609a90d-4059-4043-9f1a-fd7b49a3e1d0", "c739fcdb-c0c9-43c0-97b6-bfc80d0ffd52"],
            src_typs=["SENSOR", "WEATHERDATA"],
            surrounding_weather="NO STATEMENT",
            temperature=23.45,
            visibility=1234.456,
            vshear=3.8,
            weather_amp="NO STATEMENT",
            weather_desc="NO STATEMENT",
            weather_id="WEATHER-ID",
            weather_int="NO STATEMENT",
            wind_chill=15.6,
            wind_cov=[1.1, 2.2],
            wind_dir=75.1234,
            wind_dir_avg=57.1,
            wind_dir_peak=78.4,
            wind_dir_peak10=44.5,
            wind_gust=10.23,
            wind_gust10=13.2,
            wind_spd=1.23,
            wind_spd_avg=12.1,
            wind_var=False,
        )
        assert weatherreport is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.weatherreport.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            lat=56.12,
            lon=-156.6,
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            report_type="FORECAST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        weatherreport = response.parse()
        assert weatherreport is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.weatherreport.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            lat=56.12,
            lon=-156.6,
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            report_type="FORECAST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            weatherreport = response.parse()
            assert weatherreport is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        weatherreport = client.weatherreport.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(WeatherreportListResponse, weatherreport, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.weatherreport.with_raw_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        weatherreport = response.parse()
        assert_matches_type(WeatherreportListResponse, weatherreport, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.weatherreport.with_streaming_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            weatherreport = response.parse()
            assert_matches_type(WeatherreportListResponse, weatherreport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        weatherreport = client.weatherreport.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, weatherreport, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.weatherreport.with_raw_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        weatherreport = response.parse()
        assert_matches_type(str, weatherreport, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.weatherreport.with_streaming_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            weatherreport = response.parse()
            assert_matches_type(str, weatherreport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        weatherreport = client.weatherreport.get(
            "id",
        )
        assert_matches_type(WeatherReportFull, weatherreport, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.weatherreport.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        weatherreport = response.parse()
        assert_matches_type(WeatherReportFull, weatherreport, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.weatherreport.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            weatherreport = response.parse()
            assert_matches_type(WeatherReportFull, weatherreport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.weatherreport.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        weatherreport = client.weatherreport.queryhelp()
        assert weatherreport is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.weatherreport.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        weatherreport = response.parse()
        assert weatherreport is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.weatherreport.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            weatherreport = response.parse()
            assert weatherreport is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        weatherreport = client.weatherreport.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(WeatherreportTupleResponse, weatherreport, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.weatherreport.with_raw_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        weatherreport = response.parse()
        assert_matches_type(WeatherreportTupleResponse, weatherreport, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.weatherreport.with_streaming_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            weatherreport = response.parse()
            assert_matches_type(WeatherreportTupleResponse, weatherreport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        weatherreport = client.weatherreport.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 56.12,
                    "lon": -156.6,
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "report_type": "FORECAST",
                    "source": "Bluestaq",
                }
            ],
        )
        assert weatherreport is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.weatherreport.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 56.12,
                    "lon": -156.6,
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "report_type": "FORECAST",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        weatherreport = response.parse()
        assert weatherreport is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.weatherreport.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 56.12,
                    "lon": -156.6,
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "report_type": "FORECAST",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            weatherreport = response.parse()
            assert weatherreport is None

        assert cast(Any, response.is_closed) is True


class TestAsyncWeatherreport:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        weatherreport = await async_client.weatherreport.create(
            classification_marking="U",
            data_mode="TEST",
            lat=56.12,
            lon=-156.6,
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            report_type="FORECAST",
            source="Bluestaq",
        )
        assert weatherreport is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        weatherreport = await async_client.weatherreport.create(
            classification_marking="U",
            data_mode="TEST",
            lat=56.12,
            lon=-156.6,
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            report_type="FORECAST",
            source="Bluestaq",
            id="WEATHER-REPORT-ID",
            act_weather="NO STATEMENT",
            agjson='{"type":"Polygon","coordinates":[ [ [ 67.3291113966927, 26.156175339112 ], [ 67.2580009640721, 26.091022064271 ], [ 67.1795862381682, 26.6637992964562 ], [ 67.2501237475598, 26.730115808233 ], [ 67.3291113966927, 26.156175339112 ] ] ] }',
            alt=123.12,
            andims=2,
            area="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            asrid=4326,
            atext="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            atype="ST_Polygon",
            bar_press=101.2,
            cc_event=True,
            cloud_cover=["OVERCAST", "BROKEN"],
            cloud_hght=[1.2, 2.2],
            contrail_hght_lower=123.123,
            contrail_hght_upper=123.123,
            data_level="MANDATORY",
            dew_point=15.6,
            dif_rad=234.5,
            dir_dev=9.1,
            en_route_weather="THUNDERSTORMS",
            external_id="GDSSMB022408301601304517",
            external_location_id="TMDS060AD4OG03CC",
            forecast_end_time=parse_datetime("2024-01-01T18:00:00.123Z"),
            forecast_start_time=parse_datetime("2024-01-01T16:00:00.123Z"),
            geo_potential_alt=1000,
            hshear=3.8,
            icao="KAFF",
            icing_lower_limit=123.123,
            icing_upper_limit=123.123,
            id_airfield="8fb38d6d-a3de-45dd-8974-4e3ed73e9449",
            id_ground_imagery="GROUND-IMAGERY-ID",
            id_sensor="0129f577-e04c-441e-65ca-0a04a750bed9",
            id_site="AIRFIELD-ID",
            index_refraction=1.1,
            origin="THIRD_PARTY_DATASOURCE",
            orig_sensor_id="ORIGSENSOR-ID",
            precip_rate=3.4,
            qnh=1234.456,
            rad_vel=-0.04,
            rad_vel_beam1=4.4,
            rad_vel_beam2=-0.2,
            rad_vel_beam3=-0.2,
            rad_vel_beam4=11.4,
            rad_vel_beam5=4.1,
            rain_hour=1.2,
            raw_metar="KXYZ 241456Z 19012G20KT 10SM FEW120 SCT200 BKN250 26/M04 A2981 RMK AO2 PK WND 19026/1420 SLP068 T02611039 51015",
            raw_taf="KXYZ 051730Z 0518/0624 31008KT 3SM -SHRA BKN020 FM052300 30006KT 5SM -SHRA OVC030 PROB30 0604/0606 VRB20G35KT 1SM TSRA BKN015CB FM060600 25010KT 4SM -SHRA OVC050 TEMPO 0608/0611 2SM -SHRA OVC030 RMK NXT FCST BY 00Z=",
            ref_rad=56.7,
            rel_humidity=34.456,
            senalt=1.23,
            senlat=12.456,
            senlon=123.456,
            soil_moisture=3.5,
            soil_temp=22.4,
            solar_rad=1234.456,
            src_ids=["e609a90d-4059-4043-9f1a-fd7b49a3e1d0", "c739fcdb-c0c9-43c0-97b6-bfc80d0ffd52"],
            src_typs=["SENSOR", "WEATHERDATA"],
            surrounding_weather="NO STATEMENT",
            temperature=23.45,
            visibility=1234.456,
            vshear=3.8,
            weather_amp="NO STATEMENT",
            weather_desc="NO STATEMENT",
            weather_id="WEATHER-ID",
            weather_int="NO STATEMENT",
            wind_chill=15.6,
            wind_cov=[1.1, 2.2],
            wind_dir=75.1234,
            wind_dir_avg=57.1,
            wind_dir_peak=78.4,
            wind_dir_peak10=44.5,
            wind_gust=10.23,
            wind_gust10=13.2,
            wind_spd=1.23,
            wind_spd_avg=12.1,
            wind_var=False,
        )
        assert weatherreport is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.weatherreport.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            lat=56.12,
            lon=-156.6,
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            report_type="FORECAST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        weatherreport = await response.parse()
        assert weatherreport is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.weatherreport.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            lat=56.12,
            lon=-156.6,
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            report_type="FORECAST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            weatherreport = await response.parse()
            assert weatherreport is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        weatherreport = await async_client.weatherreport.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(WeatherreportListResponse, weatherreport, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.weatherreport.with_raw_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        weatherreport = await response.parse()
        assert_matches_type(WeatherreportListResponse, weatherreport, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.weatherreport.with_streaming_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            weatherreport = await response.parse()
            assert_matches_type(WeatherreportListResponse, weatherreport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        weatherreport = await async_client.weatherreport.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, weatherreport, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.weatherreport.with_raw_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        weatherreport = await response.parse()
        assert_matches_type(str, weatherreport, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.weatherreport.with_streaming_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            weatherreport = await response.parse()
            assert_matches_type(str, weatherreport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        weatherreport = await async_client.weatherreport.get(
            "id",
        )
        assert_matches_type(WeatherReportFull, weatherreport, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.weatherreport.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        weatherreport = await response.parse()
        assert_matches_type(WeatherReportFull, weatherreport, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.weatherreport.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            weatherreport = await response.parse()
            assert_matches_type(WeatherReportFull, weatherreport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.weatherreport.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        weatherreport = await async_client.weatherreport.queryhelp()
        assert weatherreport is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.weatherreport.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        weatherreport = await response.parse()
        assert weatherreport is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.weatherreport.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            weatherreport = await response.parse()
            assert weatherreport is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        weatherreport = await async_client.weatherreport.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(WeatherreportTupleResponse, weatherreport, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.weatherreport.with_raw_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        weatherreport = await response.parse()
        assert_matches_type(WeatherreportTupleResponse, weatherreport, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.weatherreport.with_streaming_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            weatherreport = await response.parse()
            assert_matches_type(WeatherreportTupleResponse, weatherreport, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        weatherreport = await async_client.weatherreport.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 56.12,
                    "lon": -156.6,
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "report_type": "FORECAST",
                    "source": "Bluestaq",
                }
            ],
        )
        assert weatherreport is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.weatherreport.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 56.12,
                    "lon": -156.6,
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "report_type": "FORECAST",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        weatherreport = await response.parse()
        assert weatherreport is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.weatherreport.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 56.12,
                    "lon": -156.6,
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "report_type": "FORECAST",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            weatherreport = await response.parse()
            assert weatherreport is None

        assert cast(Any, response.is_closed) is True
