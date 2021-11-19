# #!/usr/bin/env python3
# import argparse
# import grpc
# import os
# import sys
# from time import sleep

# import utils.p4runtime_lib.bmv2 as bmv2
# from utils.p4runtime_lib.error_utils import printGrpcError
# from utils.p4runtime_lib.switch import ShutdownAllSwitchConnections
# import utils.p4runtime_lib.helper as helper

# from scapy.all import sniff


# def writeRules(p4info_helper, ingress_sw):

#     table_entry = p4info_helper.buildTableEntry(
#         table_name="IngressImpl.mac_lookup",
#         match_fields={
#             "hdr.ethernet.dstAddr": "FF:FF:FF:FF:FF:FF"
#         },
#         action_name="IngressImpl.multicast",
#         action_params={})
#     ingress_sw.WriteTableEntry(table_entry)
#     print("Installed ingress tunnel rule on %s" % ingress_sw.name)

#     table_entry = p4info_helper.buildTableEntry(
#         table_name="IngressImpl.mac_lookup",
#         match_fields={
#             "hdr.ethernet.dstAddr": "08:00:00:00:01:01"
#         },
#         action_name="IngressImpl.mac_forward",
#         action_params={
#             "port": 1,
#         })
#     ingress_sw.WriteTableEntry(table_entry)
#     print("Installed ingress rule on %s" % ingress_sw.name)

#     table_entry = p4info_helper.buildTableEntry(
#         table_name="IngressImpl.mac_lookup",
#         match_fields={
#             "hdr.ethernet.dstAddr": "08:00:00:00:02:02"
#         },
#         action_name="IngressImpl.mac_forward",
#         action_params={
#             "port": 2,
#         })
#     ingress_sw.WriteTableEntry(table_entry)
#     print("Installed ingress rule on %s" % ingress_sw.name)


# def readTableRules(p4info_helper, sw):
#     print('\n----- Reading tables rules for %s -----' % sw.name)
#     for response in sw.ReadTableEntries():
#         for entity in response.entities:
#             entry = entity.table_entry
#             table_name = p4info_helper.get_tables_name(entry.table_id)
#             print('%s: ' % table_name, end=' ')
#             for m in entry.match:
#                 print(p4info_helper.get_match_field_name(
#                     table_name, m.field_id), end=' ')
#                 print('%r' % (p4info_helper.get_match_field_value(m),), end=' ')
#             action = entry.action.action
#             action_name = p4info_helper.get_actions_name(action.action_id)
#             print('->', action_name, end=' ')
#             for p in action.params:
#                 print(p4info_helper.get_action_param_name(
#                     action_name, p.param_id), end=' ')
#                 print('%r' % p.value, end=' ')
#             print()


# def main(p4info_file_path, bmv2_file_path):
#     p4info_helper = helper.P4InfoHelper(p4info_file_path)
#     try:
#         s1 = bmv2.Bmv2SwitchConnection(
#             name='s1',
#             address='127.0.0.1:50051',
#             device_id=0,
#             proto_dump_file='logs/s1-p4runtime-requests.txt')
#         s2 = bmv2.Bmv2SwitchConnection(
#             name='s2',
#             address='127.0.0.1:50052',
#             device_id=1,
#             proto_dump_file='logs/s2-p4runtime-requests.txt')
#         s3 = bmv2.Bmv2SwitchConnection(
#             name='s3',
#             address='127.0.0.1:50053',
#             device_id=2,
#             proto_dump_file='logs/s3-p4runtime-requests.txt')

#         s1.MasterArbitrationUpdate()
#         s2.MasterArbitrationUpdate()
#         s3.MasterArbitrationUpdate()

#         writeRules(p4info_helper, s1)
#         readTableRules(p4info_helper, s1)
#         writeRules(p4info_helper, s2)
#         readTableRules(p4info_helper, s2)
#         writeRules(p4info_helper, s3)
#         readTableRules(p4info_helper, s3)
#     except KeyboardInterrupt:
#         print(" Shutting down.")
#     except grpc.RpcError as e:
#         printGrpcError(e)


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='P4Runtime Controller')
#     parser.add          default='./build/main.p4.p4info.txt')
#     parser.add_argument('--bmv2-json', help='BMv2 JSON file from p4c',
#                         type=str, action="store", required=False,
#                         default='./build/main.json')
#     args = parser.parse_args()

#     if not os.path.exists(args.p4info):
#         parser.print_help()
#         print("\np4info file not found: %s\nHave you run 'make'?" % args.p4info)
#         parser.exit(1)
#     if not os.path.exists(args.bmv2_json):
#         parser.print_help()
#         print("\nBMv2 JSON file not found: %s\nHave you run 'make'?" %
#               args.bmv2_json)
#         parser.exit(1)
#     main(args.p4info, args.bmv2_json)
#           default='./build/main.p4.p4info.txt')
#     parser.add_argument('--bmv2-json', help='BMv2 JSON file from p4c',
#                         type=str, action="store", required=False,
#                         default='./build/main.json')
#     args = parser.parse_args()

#     if not os.path.exists(args.p4info):
#         parser.print_help()
#         print("\np4info file not found: %s\nHave you run 'make'?" % args.p4info)
#         parser.exit(1)
#     if not os.path.exists(args.bmv2_json):
#         parser.print_help()
#         print("\nBMv2 JSON file not found: %s\nHave you run 'make'?" %
#               args.bmv2_json)
#         parser.exit(1)
#     main(args.p4info, args.bmv2_json)
