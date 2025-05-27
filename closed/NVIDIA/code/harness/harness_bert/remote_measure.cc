// remote_measure.cc
#include "remote_measure.h"
#include <libssh/libssh.h>
#include <iostream>
#include <cstdlib>

RemoteJtopMeasure::RemoteJtopMeasure(const std::string& hostname, const std::string& username, const std::string& password, const std::string& script_dir)
    : hostname(hostname), username(username), password(password), script_dir(script_dir) {}

void RemoteJtopMeasure::start() {
    ssh_session session = ssh_new();
    if (session == nullptr) {
        std::cerr << "Error creating SSH session" << std::endl;
        return;
    }

    ssh_options_set(session, SSH_OPTIONS_HOST, hostname.c_str());
    ssh_options_set(session, SSH_OPTIONS_USER, username.c_str());

    int rc = ssh_connect(session);
    if (rc != SSH_OK) {
        std::cerr << "Error connecting to " << hostname << ": " << ssh_get_error(session) << std::endl;
        ssh_free(session);
        return;
    }

    rc = ssh_userauth_password(session, nullptr, password.c_str());
    if (rc != SSH_AUTH_SUCCESS) {
        std::cerr << "Error authenticating with password: " << ssh_get_error(session) << std::endl;
        ssh_disconnect(session);
        ssh_free(session);
        return;
    }

    std::string command = "nohup sudo " + script_dir + "/script_start_t.sh > /dev/null 2>&1 &";
    executeCommand(session, command);
    ssh_disconnect(session);
    ssh_free(session);
}

void RemoteJtopMeasure::stop() {
    ssh_session session = ssh_new();
    if (session == nullptr) {
        std::cerr << "Error creating SSH session" << std::endl;
        return;
    }

    ssh_options_set(session, SSH_OPTIONS_HOST, hostname.c_str());
    ssh_options_set(session, SSH_OPTIONS_USER, username.c_str());

    int rc = ssh_connect(session);
    if (rc != SSH_OK) {
        std::cerr << "Error connecting to " << hostname << ": " << ssh_get_error(session) << std::endl;
        ssh_free(session);
        return;
    }

    rc = ssh_userauth_password(session, nullptr, password.c_str());
    if (rc != SSH_AUTH_SUCCESS) {
        std::cerr << "Error authenticating with password: " << ssh_get_error(session) << std::endl;
        ssh_disconnect(session);
        ssh_free(session);
        return;
    }

    std::string command = "sudo " + script_dir + "/script_stop_t.sh";
    executeCommand(session, command);
    ssh_disconnect(session);
    ssh_free(session);
}

void RemoteJtopMeasure::executeCommand(ssh_session session, const std::string& command) {
    ssh_channel channel = ssh_channel_new(session);
    if (channel == nullptr) {
        std::cerr << "Error creating SSH channel: " << ssh_get_error(session) << std::endl;
        return;
    }

    int rc = ssh_channel_open_session(channel);
    if (rc != SSH_OK) {
        std::cerr << "Error opening channel: " << ssh_get_error(session) << std::endl;
        ssh_channel_free(channel);
        return;
    }

    rc = ssh_channel_request_exec(channel, command.c_str());
    if (rc != SSH_OK) {
        std::cerr << "Error executing command: " << ssh_get_error(session) << std::endl;
        ssh_channel_close(channel);
        ssh_channel_free(channel);
        return;
    }

    char buffer[256];
    int nbytes;
    nbytes = ssh_channel_read(channel, buffer, sizeof(buffer), 0);
    while (nbytes > 0) {
        std::cout.write(buffer, nbytes);
        nbytes = ssh_channel_read(channel, buffer, sizeof(buffer), 0);
    }

    if (nbytes < 0) {
        std::cerr << "Error reading channel: " << ssh_get_error(session) << std::endl;
    }

    ssh_channel_send_eof(channel);
    ssh_channel_close(channel);
    ssh_channel_free(channel);
}
