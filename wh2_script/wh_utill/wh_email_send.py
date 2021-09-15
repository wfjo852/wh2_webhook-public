#-*- coding:utf-8 -*-

import wh_html
import wh_email , infomation
import wh_info




null = ""
version_read = {
        "version": {
            "idx": "1",
            "name": "big_s0010_c0010_anim_v001",
            "description": "Confirm_check",
            "kind": "shot",
            "project": {
                "idx": "1",
                "name": "Demo_Bigbuck_Bunny",
                "description": "Demo_Bigbuck_Bunny",
                "start_date": "2018-12-11",
                "end_date": "2019-04-12"
            },
            "episode": {
                "idx": "1",
                "name": "Ep01",
                "description": "Demo_Bigbuck_Bunny_First"
            },
            "sequence": {
                "idx": "1",
                "name": "s0010",
                "description": "Opening Sequence",
                "sequence_order": "1"
            },
            "shot": {
                "idx": "1",
                "name": "s0010_c0010"
            },
            "task": {
                "idx": "4",
                "start_date": "2019-04-05",
                "end_date": "2019-04-11"
            },
            "user": {
                "idx": "2",
                "name": "Artist",
                "id": "c3m",
                "email": "artist@c2monster.com",
                "thumbnail": "http:\/\/localhost:81\/2019\/04\/08\/dc3295a0a38e89e9.png"
            },
            "main_reviewer": {
                "idx": "4",
                "name": "Supervisor",
                "id": "c4m",
                "email": "",
                "thumbnail": "http:\/\/localhost:81\/2019\/04\/08\/d63b00a6934f6b55.png"
            },
            "cc_reviewers": [
                {
                    "idx": "1",
                    "name": "C2Monster",
                    "id": "c2m",
                    "email": "contact@c2monster.com",
                    "thumbnail": "http:\/\/localhost:81\/2019\/04\/08\/c1f855a779d0543e.png"
                },
                {
                    "idx": "2",
                    "name": "Artist",
                    "id": "c3m",
                    "email": "artist@c2monster.com",
                    "thumbnail": "http:\/\/localhost:81\/2019\/04\/08\/dc3295a0a38e89e9.png"
                }
            ],
            "url": "http:\/\/localhost\/project\/1\/version\/1\/detail",
            "attachments": [
                {
                    "idx": "1",
                    "name": "D:\\wormhole\\wh2_test_Big_buck\\Animation\\big_s0010_c0010_anim_v001.mp4",
                    "url": "http:\/\/localhost:81\/2019\/04\/08\/816982d46b930845.mp4",
                    "mime_type": [
                        "video",
                        "mp4"
                    ],
                    "is_main": "1"
                }
            ]
        }
    }

shot_task_read = {
    "task": {
        "kind": "shot",
        "idx": "1",
        "url": "http:\/\/localhost\/project\/1\/shot\/task\/1\/detail",
        "tasktype": {
            "idx": "3",
            "name": "Comp"
        },
        "description": "test description",
        "user": {
            "idx": "1",
            "name": "C2Monster",
            "id": "c2m",
            "email": "contact@c2monster.com",
            "thumbnail": "http:\/\/localhost:81\/2019\/04\/08\/c1f855a779d0543e.png"
        },
        "start_date": null,
        "end_date": null,
        "status": {
            "idx": "1",
            "name": "wip"
        },
        "duration": "0",
        "project": {
            "idx": "1",
            "name": "Demo_Bigbuck_Bunny"
        },
        "episode": {
            "idx": "1",
            "name": "Ep01"
        },
        "sequence": {
            "idx": "1",
            "name": "s0010"
        },
        "shot": {
            "idx": "1",
            "name": "s0010_c0010",
            "thumbnail": "http:\/\/localhost:81\/2019\/04\/08\/24591d492b5b4b16.jpg",
            "shot_order": "1",
            "location": "Jungle_A",
            "description": "Opening_sequence",
            "direction_note": "",
            "length": "285",
            "handle_in": "0",
            "handle_out": "0",
            "frame_in": "0",
            "frame_out": "284",
            "timecode_in": "00:00:00:00",
            "timecode_out": "",
            "importance": "0",
            "difficulty": "",
            "original_path": "D:\\wormhole\\wh2_test_Big_buck\\Animation\\big_s0010_c0010_anim_v001.mp4",
            "camera_clip": null,
            "camera_name": null,
            "lens_type": null,
            "focal_length": null,
            "grip": null,
            "camera_filter": null,
            "iso": null,
            "shutter_speed": null,
            "f_stop": null,
            "stereo_type": null,
            "stereo_iod": null,
            "stereo_converged_point": null,
            "stereo_rig": null,
            "stereo_dof": null,
            "camera_note": null
        },
        "pubs": null
    },
    "tasks_in_progress": [
        {
            "idx": "4",
            "tasktype": {
                "idx": "1",
                "name": "Animation"
            },
            "start_date": "2019-04-05",
            "end_date": "2019-04-11",
            "duration": "4",
            "user": {
                "idx": "2",
                "id": "c3m",
                "name": "Artist"
            },
            "status": {
                "idx": "2",
                "name": "confirm"
            },
            "description": "Detail Animation",
            "publish": {
                "last_name": null
            }
        },
        {
            "idx": "1",
            "tasktype": {
                "idx": "3",
                "name": "Comp"
            },
            "start_date": null,
            "end_date": null,
            "duration": "0",
            "user": {
                "idx": "1",
                "id": "c2m",
                "name": "C2Monster"
            },
            "status": {
                "idx": "1",
                "name": "wip"
            },
            "description": "",
            "publish": {
                "last_name": null
            }
        }
    ]
}

asset_task_read = {
    "task": {
        "kind": "asset",
        "idx": "1",
        "url": "http:\/\/localhost\/project\/1\/asset\/task\/1\/detail",
        "tasktype": {
            "idx": "15",
            "name": "Texture"
        },
        "description": "테스크 디스크립션테스트 중입니다.ㅓㅇ",
        "user": {
            "idx": "2",
            "name": "Artist",
            "id": "c3m",
            "email": "artist@c2monster.com",
            "thumbnail": "http:\/\/localhost:81\/2019\/04\/08\/dc3295a0a38e89e9.png"
        },
        "start_date": null,
        "end_date": null,
        "status": {
            "idx": "1",
            "name": "wip"
        },
        "duration": "0",
        "project": {
            "idx": "1",
            "name": "Demo_Bigbuck_Bunny"
        },
        "asset_category": {
            "idx": "1",
            "name": "char"
        },
        "asset": {
            "idx": "1",
            "name": "ch_bunny",
            "thumbnail": "http:\/\/localhost:81\/2019\/04\/08\/78b9d804eb4a7f53.jpg",
            "asset_order": "1",
            "description": "Hero character",
            "used": null,
            "reference_path": null,
            "hdri_path": null,
            "source_path": null
        },
        "pubs": null
    },
    "tasks_in_progress": [
        {
            "idx": "2",
            "tasktype": {
                "idx": "14",
                "name": "Modeling"
            },
            "start_date": null,
            "end_date": null,
            "duration": "0",
            "user": {
                "idx": "2",
                "id": "c3m",
                "name": "Artist"
            },
            "status": {
                "idx": "1",
                "name": "wip"
            },
            "description": "",
            "publish": {
                "last_name": null
            }
        },
        {
            "idx": "1",
            "tasktype": {
                "idx": "15",
                "name": "Texture"
            },
            "start_date": null,
            "end_date": null,
            "duration": "0",
            "user": {
                "idx": "2",
                "id": "c3m",
                "name": "Artist"
            },
            "status": {
                "idx": "1",
                "name": "wip"
            },
            "description": "",
            "publish": {
                "last_name": null
            }
        },
        {
            "idx": "6",
            "tasktype": {
                "idx": "16",
                "name": "Concept"
            },
            "start_date": null,
            "end_date": null,
            "duration": "0",
            "user": {
                "idx": "1",
                "id": "c2m",
                "name": "C2Monster"
            },
            "status": {
                "idx": "2",
                "name": "confirm"
            },
            "description": "",
            "publish": {
                "last_name": null
            }
        }
    ]
}

asset_task_html = wh_html.task(asset_task_read)
shot_task_html = wh_html.task(shot_task_read)
version_html = wh_html.version(version_read)

def task_assign(data):
    task_kind = data['kind']
    task_idx = data['idx']

    #TASK DATA 얻어 오
    if task_kind == "shot":
        tasK_read_data = wh_info.wh2api.shot_task.read(task_idx)
    elif task_kind == "asset":
        tasK_read_data = wh_info.wh2api.asset_task.read(task_idx)

    task_html = wh_html.task(tasK_read_data)
    to = tasK_read_data['']


    wh_email.mail_send(infomation.mail_token_jongho,
                       to="wfjo852@gmail.com",
                       sub_text=asset_task_read['task']['tasktype']['name']+' Task Assign',
                       html_return = wh_email.html_text(str(task_html)))



data = {'task': {'kind': 'shot', 'idx': '71'}}

task_assign(data)
