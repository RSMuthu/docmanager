import styles from '../../static/css/404.module.css'

function Page () {
    return (
        <div className={styles['page-not-found']} >
            <div className={styles['not-found']}>
                <div className={styles['not-found-404']}>
                    { /* This weill be acting like a centeralised background text */ }
                    <h1>404</h1>
                </div>
                <h2>We are sorry, Page not found!</h2>
                <p>the page you are looking for, is currently unavailable</p>
            </div>
        </div>
    )
}
export default Page
