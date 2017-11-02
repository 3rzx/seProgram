int main(int argc, char *argv[])
{
    system("zip -rP 1234 EncryptedFile file");
    system("rm file");
    return 0;
}
