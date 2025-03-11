from bingx_sign_header_generator import BingxSignHeader


def test_request_payload_is_sorted():
    unsorted_payload = {
        "b_key": "value_b",
        "a_key": "value_a",
        "c_key": "value_c",
    }

    sign_header = BingxSignHeader(
        timestamp=1234567890, trace_id="trace123", device_id="device123", request_payload=unsorted_payload
    )

    sorted_keys = sorted(unsorted_payload.keys())
    payload_keys = list(sign_header.request_payload.keys())
    assert payload_keys == sorted_keys, f"Expected keys {sorted_keys} but got {payload_keys}"
