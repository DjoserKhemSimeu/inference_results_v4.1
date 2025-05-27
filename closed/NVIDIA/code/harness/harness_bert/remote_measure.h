#ifndef REMOTE_MEASURE_H
#define REMOTE_MEASURE_H

#include <string>
#include <libssh/libssh.h>

class RemoteJtopMeasure {
public:
    RemoteJtopMeasure(const std::string& hostname, const std::string& username, const std::string& password, const std::string& script_dir);

    void start();
    void stop();

private:
    std::string hostname;
    std::string username;
    std::string password;
    std::string script_dir;

    void executeCommand(ssh_session session, const std::string& command);
};

#endif // REMOTE_MEASURE_H
