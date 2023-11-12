create table Users
(
    id              int null comment '自动创建的用户id',
    username        varchar(50) null comment '用户名（与服务器对应）',
    email           varchar(120) null comment '电子邮件地址',
    role            varchar(30) null comment '用户角色，分为管理员/网管和普通用户',
    hashed_password varchar(100) null comment '密码（哈希后）'
) comment '用于保存用户信息';


