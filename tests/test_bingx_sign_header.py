from bingx_sign_header_generator import BingxSignHeader


def test_generate_sign_header_value_for_perpetual():
    sign_header = BingxSignHeader(
        timestamp=1741703230359,
        trace_id="f87ddc80584841cba0422b9a902993b9",
        device_id="dc3143feb93e4dedaea5d5e795ed21ef",
        request_payload={
            "copyTradeLabelType": "2",
            "apiIdentity": "1347851488071426053",
            "pageId": "0",
            "uid": "1339191395874545671",
            "pageSize": "10",
        },
    )

    expected_encryption_content = (
        "95d65c73dc5c4370ae9018fb7f2eab69"
        "1741703230359"
        "f87ddc80584841cba0422b9a902993b9"
        "dc3143feb93e4dedaea5d5e795ed21ef"
        "30"
        "4.78.45"
        '{"apiIdentity":"1347851488071426053",'
        '"copyTradeLabelType":"2",'
        '"pageId":"0",'
        '"pageSize":"10",'
        '"uid":"1339191395874545671"}'
    )

    expected_sign = "F025A836122A28953D67DDF9A0DB7BA4A6E303332F8E15BD2E1D76939CD8091E"

    encryption_content = sign_header._generate_encryption_content()
    sign = sign_header.generate_sign_header_value()

    assert encryption_content == expected_encryption_content, (
        f"Expected {expected_encryption_content} but got {encryption_content}"
    )
    assert sign == expected_sign, f"Expected {expected_sign} but got {sign}"


def test_generate_sign_header_value_for_standard():
    sign_header = BingxSignHeader(
        timestamp=1741706523722,
        trace_id="84b7e565cf71475e8dc1e5734da91ece",
        device_id="dc3143feb93e4dedaea5d5e795ed21ef",
        request_payload={
            "pageSize": "10",
            "trader": "1016279174200614920",
            "pageId": "0",
        },
    )

    expected_encryption_content = (
        "95d65c73dc5c4370ae9018fb7f2eab69"
        "1741706523722"
        "84b7e565cf71475e8dc1e5734da91ece"
        "dc3143feb93e4dedaea5d5e795ed21ef"
        "30"
        "4.78.45"
        '{"pageId":"0",'
        '"pageSize":"10",'
        '"trader":"1016279174200614920"}'
    )

    expected_sign = "029AAD2A2FDA095355699329A36928E6986504D96283F0EC4D255F1559F37692"

    encryption_content = sign_header._generate_encryption_content()
    sign = sign_header.generate_sign_header_value()

    assert encryption_content == expected_encryption_content, (
        f"Expected {expected_encryption_content} but got {encryption_content}"
    )
    assert sign == expected_sign, f"Expected {expected_sign} but got {sign}"
