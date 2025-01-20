# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.types.onorbit import (
    AntennaDetailsFull,
    AntennaDetailListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAntennaDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        antenna_detail = client.onorbit.antenna_details.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_antenna="idAntenna",
            source="source",
        )
        assert antenna_detail is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        antenna_detail = client.onorbit.antenna_details.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_antenna="idAntenna",
            source="source",
            id="id",
            beam_forming=True,
            beamwidth=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            description="description",
            diameter=0,
            end_frequency=0,
            gain=0,
            gain_tolerance=0,
            manufacturer_org_id="manufacturerOrgId",
            mode="mode",
            origin="origin",
            orig_network="origNetwork",
            polarization=0,
            position="position",
            size=[0],
            start_frequency=0,
            steerable=True,
            tags=["string"],
            type="type",
        )
        assert antenna_detail is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.antenna_details.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_antenna="idAntenna",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = response.parse()
        assert antenna_detail is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.antenna_details.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_antenna="idAntenna",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = response.parse()
            assert antenna_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        antenna_detail = client.onorbit.antenna_details.retrieve(
            "id",
        )
        assert_matches_type(AntennaDetailsFull, antenna_detail, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.antenna_details.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = response.parse()
        assert_matches_type(AntennaDetailsFull, antenna_detail, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.antenna_details.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = response.parse()
            assert_matches_type(AntennaDetailsFull, antenna_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbit.antenna_details.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        antenna_detail = client.onorbit.antenna_details.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_antenna="idAntenna",
            source="source",
        )
        assert antenna_detail is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        antenna_detail = client.onorbit.antenna_details.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_antenna="idAntenna",
            source="source",
            id_2="id",
            beam_forming=True,
            beamwidth=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            description="description",
            diameter=0,
            end_frequency=0,
            gain=0,
            gain_tolerance=0,
            manufacturer_org_id="manufacturerOrgId",
            mode="mode",
            origin="origin",
            orig_network="origNetwork",
            polarization=0,
            position="position",
            size=[0],
            start_frequency=0,
            steerable=True,
            tags=["string"],
            type="type",
        )
        assert antenna_detail is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.antenna_details.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_antenna="idAntenna",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = response.parse()
        assert antenna_detail is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.antenna_details.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_antenna="idAntenna",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = response.parse()
            assert antenna_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            client.onorbit.antenna_details.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                id_antenna="idAntenna",
                source="source",
                id_2="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        antenna_detail = client.onorbit.antenna_details.list()
        assert_matches_type(AntennaDetailListResponse, antenna_detail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.antenna_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = response.parse()
        assert_matches_type(AntennaDetailListResponse, antenna_detail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.antenna_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = response.parse()
            assert_matches_type(AntennaDetailListResponse, antenna_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        antenna_detail = client.onorbit.antenna_details.delete(
            "id",
        )
        assert antenna_detail is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.onorbit.antenna_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = response.parse()
        assert antenna_detail is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.onorbit.antenna_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = response.parse()
            assert antenna_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbit.antenna_details.with_raw_response.delete(
                "",
            )


class TestAsyncAntennaDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        antenna_detail = await async_client.onorbit.antenna_details.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_antenna="idAntenna",
            source="source",
        )
        assert antenna_detail is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        antenna_detail = await async_client.onorbit.antenna_details.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_antenna="idAntenna",
            source="source",
            id="id",
            beam_forming=True,
            beamwidth=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            description="description",
            diameter=0,
            end_frequency=0,
            gain=0,
            gain_tolerance=0,
            manufacturer_org_id="manufacturerOrgId",
            mode="mode",
            origin="origin",
            orig_network="origNetwork",
            polarization=0,
            position="position",
            size=[0],
            start_frequency=0,
            steerable=True,
            tags=["string"],
            type="type",
        )
        assert antenna_detail is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.antenna_details.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_antenna="idAntenna",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = await response.parse()
        assert antenna_detail is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.antenna_details.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_antenna="idAntenna",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = await response.parse()
            assert antenna_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        antenna_detail = await async_client.onorbit.antenna_details.retrieve(
            "id",
        )
        assert_matches_type(AntennaDetailsFull, antenna_detail, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.antenna_details.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = await response.parse()
        assert_matches_type(AntennaDetailsFull, antenna_detail, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.antenna_details.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = await response.parse()
            assert_matches_type(AntennaDetailsFull, antenna_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbit.antenna_details.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        antenna_detail = await async_client.onorbit.antenna_details.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_antenna="idAntenna",
            source="source",
        )
        assert antenna_detail is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        antenna_detail = await async_client.onorbit.antenna_details.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_antenna="idAntenna",
            source="source",
            id_2="id",
            beam_forming=True,
            beamwidth=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            description="description",
            diameter=0,
            end_frequency=0,
            gain=0,
            gain_tolerance=0,
            manufacturer_org_id="manufacturerOrgId",
            mode="mode",
            origin="origin",
            orig_network="origNetwork",
            polarization=0,
            position="position",
            size=[0],
            start_frequency=0,
            steerable=True,
            tags=["string"],
            type="type",
        )
        assert antenna_detail is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.antenna_details.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_antenna="idAntenna",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = await response.parse()
        assert antenna_detail is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.antenna_details.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_antenna="idAntenna",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = await response.parse()
            assert antenna_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            await async_client.onorbit.antenna_details.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                id_antenna="idAntenna",
                source="source",
                id_2="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        antenna_detail = await async_client.onorbit.antenna_details.list()
        assert_matches_type(AntennaDetailListResponse, antenna_detail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.antenna_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = await response.parse()
        assert_matches_type(AntennaDetailListResponse, antenna_detail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.antenna_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = await response.parse()
            assert_matches_type(AntennaDetailListResponse, antenna_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        antenna_detail = await async_client.onorbit.antenna_details.delete(
            "id",
        )
        assert antenna_detail is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbit.antenna_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        antenna_detail = await response.parse()
        assert antenna_detail is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbit.antenna_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            antenna_detail = await response.parse()
            assert antenna_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbit.antenna_details.with_raw_response.delete(
                "",
            )
