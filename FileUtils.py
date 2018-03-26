class FileUtils():
    def formatFileSize(sizeBytes):
        sizeBytes = float(sizeBytes)
        result = float(abs(sizeBytes))
        suffix = "B";
        if(result>1024):
            suffix = "KB"
            mult = 1024
            result = result / 1024

        if(result > 1024):
            suffix = "MB"
            mult *= 1024
            result = result / 1024

        if (result > 1024) :
            suffix = "GB"
            mult *= 1024
            result = result / 1024

        if (result > 1024) :
            suffix = "TB"
            mult *= 1024
            result = result / 1000

        if (result > 1024) :
            suffix = "PB"
            mult *= 1024
            result = result / 1024

        return format(result,'.2f')+" "+suffix
