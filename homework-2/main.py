from src.channel import Channel


if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    # �������� �������� ���������
    print(moscowpython.title)  # MoscowPython
    print(moscowpython.video_count)  # 685 (����� ��� ������)
    print(moscowpython.url)  # https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A

    # ������ �� �����
    moscowpython.channel_id = '����� ��������'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # ����� �������� ������ ��� ������ � API ��� ������
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # ������� ���� 'moscowpython.json' � ������� �� ������
    moscowpython.to_json('moscowpython.json')
