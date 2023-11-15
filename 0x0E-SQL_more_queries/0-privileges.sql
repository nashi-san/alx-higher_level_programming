-- A script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
SELECT user, host, Grant_priv, Super_priv, Select_priv, Insert_priv, Update_priv, Delete_priv, Create_priv, Drop_priv, Reload_priv, Shutdown_priv, Process_priv, File_priv, Grant_priv, References_priv, Index_priv, Alter_priv, Show_db_priv, Super_priv, Create_tmp_table_priv, Lock_tables_priv, Execute_priv, Repl_slave_priv, Repl_client_priv
FROM mysql.user
WHERE user IN ('user_0d_1', 'user_0d_2')
  AND host = 'localhost';
