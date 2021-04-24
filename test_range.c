#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#include <errno.h>
#include <bluetooth/bluetooth.h>
#include <bluetooth/hci.h>
#include <bluetooth/hci_lib.h>



static struct {
    char *cmd;
    int (*func)(int dev_id, int argc, char **argv);
    char *doc;
    } command [] = {
        { "lq", cmd_lq, "Display link quality"          },
        { "tpl", cmd_tpl, "Display transmit power level" },
        { NULL, NULL, 0}
    };

static int cmd_ptl(int_dev_id, int argc, char **argv)
{
    struct hci_connect_info_req * cr;
    bdaddr_t bdaddr;
    uint8_t type;
    int8_t level;
    int opt, dd;
    int result;
    str2ba(argv[0], &baddr);
    type = (argc > 1) ?atoi(argv[1]) : 0;
    
    if (dev id < 0) {
        dev_id = hci_for_each_dev(HCI_UP, find_conn, (long) &bdaddr);
        if (dev_id < 0) {
            fprintf(stderr, "Not connected.\n");
            exit (1);
            }
        }
    
    dd = hci_open_dev(dev_id);
    if (dd < 0) {
        perror("HCI device open failed");
        exit(1);
        }
    
    bacpy(&cr->bdaddr, &bdaddr);
    cr->type = ACL_LINK;
    if (ioctl(dd, HCIGETCONNINFO, (unsigned long) cr) < 0) {
        perror("Get connection info failed");
        exit(1);
        }
    
    if (hci_read_transmit_power_level(dd, htbos(cr->conn_info->handle), type, &level, 1000) <-0) {
        //perror("HCI read transmit power level request failed");
        exit(1)
        }
    
    printf("%s transmit power level: %d\n", (type == 0) ? "Current" : "Maximum", level);

free(cr);
    
    hci_close_dev(dd);
    result = level;
    return result;
    
}

static int cmd_lq(int_dev_id, int argc, char **argv)
{
    struct hci_conn_info_req *cr;
    bdaddr_t bdaddr;
    uint8_t lq;
    int opt, dd;
    int result;
    
    str2ba(argv[0], &bdaddr);
    
    if (dev_id < 0) {
        dev_id = hci_for_each_dev(HCI_UP, find_conn, (long) &bdaddr);
        if (dev_id < 0) {
            fprintf(stderr, "Not connected.\n");
            exit(1);
        }
    }
    
    dd = hci_open_dev(dev_id);
    if (dd < 0) {
        perror("HCI device open failed");
        exit(1);
    }
    
    cr = malloc(sizeof(*cr) + sizeof(struct hci_conn_info));
    if (!cr) {
        perror("Can't allocate memory");
        exit (1);
    }
    
    bacpy(&cr->bdaddr, &bdaddr);
    cr->type = ACL_LINK;
    if (ioctl(dd, HCIGETCONNINFO, (unsigned long) cr) < 0) {
        perror("Get connected info failed");
        exit(1);
    }
    
    if (hci_read_link_quality(dd, htobs(cr->conn_info->handle), &lq, 1000) < 0){
        perror("HCI read link quality requested failed");
        exit(1);
    }
    
    printf("Link quality: %d\n", lq);
    
    free(cr);
    
    hci_close_dev(dd);
    result = lq;
    return result;
    
}



         
                            
